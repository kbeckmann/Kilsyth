from migen import *
import argparse
import sys, os

class FT600Pipe(Module):
    def __init__(self, clk, leds, ft600):
        self.clock_domains.cd_por = ClockDomain()
        self.clock_domains.cd_sys = ClockDomain(reset_less=False)
        self.cd_sys.clk = ft600.clk

        self.counter = Signal(32)

        timer = Signal(32)

        ft_be_triple = TSTriple(2)
        ft_be = ft_be_triple.get_tristate(ft600.be)
        self.specials += ft_be

        ft_data_triple = TSTriple(16)
        ft_data = ft_data_triple.get_tristate(ft600.data)
        self.specials += ft_data

        width = 16
        depth = 2048
        self.specials.mem = Memory(width, depth)
        wrport = self.mem.get_port(write_capable=True)
        rdport = self.mem.get_port(has_re=False)
        self.specials += wrport, rdport

        words_received = Signal(16, reset=0)
        words_received_1 = Signal(16, reset=0) # store (words_received - 1) separately
        read_word_at = Signal(16, reset=0)

        self.comb += [
            leds[0].eq(self.counter[0]),
            # rdport.adr.eq(0), # To read a constant address..
            rdport.adr.eq(read_word_at),
        ]
 
        txe_n_r = Signal(reset=1)
        rxf_n_r = Signal(reset=1)
        self.sync += [
            self.counter.eq(self.counter + 1),
            txe_n_r.eq(ft600.txe_n),
            rxf_n_r.eq(ft600.rxf_n),
        ]

        self.submodules.fsm = FSM(reset_state="WAIT-INPUT")
        self.fsm.act(
            "WAIT-INPUT",
            NextValue(leds[2], 1),
            NextValue(ft600.oe_n, 1),
            NextValue(ft600.rd_n, 1),
            NextValue(ft600.wr_n, 1),
            NextValue(ft_be.oe, 0),
            NextValue(ft_data.oe, 0),
            NextValue(wrport.we, 0),

            If(
                (ft600.txe_n == 0) & (words_received != 0) & (read_word_at != words_received_1),
                NextValue(leds[2], 0),

                # Just a safegueard to see if we leak data
                NextValue(ft_data.o, 0xdead),
                NextValue(ft_data.oe, 1),

                NextState("WRITE-WORD"),
            ).Elif(
                (ft600.rxf_n == 0) & (words_received == 0),
                NextValue(ft600.oe_n, 0), # This must happen 1 clk before rd_n<=0

                NextValue(read_word_at, 0),
                NextValue(leds[2], 0),
                NextState("READ-WORD"),
            )
        )
        self.fsm.act(
            "READ-WORD",
            NextValue(leds[4], 1),
            NextValue(ft600.oe_n, 0),
            NextValue(ft600.rd_n, 0),
            If(
                (ft600.rxf_n == 1),
                NextValue(leds[4], 0),
                NextValue(words_received_1, words_received - 1),
                NextValue(wrport.we, 0),
                NextState("WAIT-INPUT")
            ).Else(
                NextValue(words_received, words_received + 1),
                NextValue(wrport.we, 1),
                NextValue(wrport.adr, words_received),
                NextValue(wrport.dat_w, ft_data.i),
            )
        )
        self.fsm.act(
            "WRITE-WORD",
            NextValue(leds[6], 1),
            NextValue(ft600.wr_n, 0),

            # NextValue(rdport.adr, read_word_at), # This happens in self.comb
            NextValue(ft_data.o, rdport.dat_r),
            NextValue(ft_data.oe, 1),

            NextValue(ft_be.oe, 1),
            NextValue(ft_be.o, 0b11),
            If(
                (ft600.txe_n == 1) | (read_word_at == words_received_1),
                NextValue(leds[6], 0),
                NextValue(words_received, 0),
                NextState("WAIT-INPUT")
            ).Else(
                NextValue(read_word_at, read_word_at + 1),
            )
        )

    def testbench(self, clk, leds, ft600):
        # yield
        # yield
        yield ft600.txe_n.eq(1)
        yield ft600.rxf_n.eq(1)
        yield ft600.be.eq(0)
        yield
        yield
        yield
        yield
        yield
        # FT writes 4 words to the bus master (fpga)
        yield ft600.rxf_n.eq(0)
        yield ft600.be.eq(0b11)
        yield
        # clk 0
        yield
        # clk 1
        yield
        # clk 2
        yield
        # clk 3
        yield ft600.rxf_n.eq(1)
        yield
        yield
        yield
        yield ft600.txe_n.eq(0)
        yield
        yield
        yield
        yield
        yield
        yield ft600.txe_n.eq(1)
        yield
        yield
        yield


def run_applet(applet):
    # Ignore applet for now
    import FT600Driver
    driver = FT600Driver.FT600Driver()

    print(driver.FT_GetDriverVersion())
    print(driver.FT_GetLibraryVersion())
    driver.get_device_lists()
    driver.set_channel_config(False, FT600Driver.CONFIGURATION_FIFO_CLK_100)



def build_gateware(test):
    import kilsyth
    target = os.environ["TARGET"] if "TARGET" in os.environ else "lfe5u12"
    plat = kilsyth.Platform(toolchain='trellis', target=target)
    plat.add_period_constraint("ft600", 10.)
    clk = plat.request("clk16")
    leds = [plat.request('user_led', i) for i in range(8)]
    ft600 = plat.request('ft600')
 
    ft600pipe = FT600Pipe(clk, leds, ft600)

    if test:
        run_simulation(ft600pipe, ft600pipe.testbench(clk, leds, ft600), vcd_name="out.vcd")
        print("Passed")
    else:
        plat.build(ft600pipe, toolchain_path='/usr/share/trellis', idcode=plat.idcode)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Kilsyth FT600 integration')
    parser.add_argument('--test', action='store_true', help='Run gateware tests')
    parser.add_argument('--build', action='store_true', help='Builds gateware')
    parser.add_argument('--run', help='Runs applet')

    args = parser.parse_args()
    # print(args)
    
    if args.test:
        build_gateware(True)
    elif args.build:
        build_gateware(False)
    elif args.run:
        run_applet(args.run)
