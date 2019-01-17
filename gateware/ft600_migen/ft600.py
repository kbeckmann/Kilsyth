from migen import *
import argparse
import sys, os

TESTING = False

class TSTripleFake():
    def __init__(self, width):
        self.oe = Signal()
        self.o = Signal(width)
        self.i = Signal(width)

class FT600Pipe(Module):
    def __init__(self, clk, leds, ft600):
        self.clock_domains.cd_por = ClockDomain()
        self.clock_domains.cd_sys = ClockDomain(reset_less=False)
        self.cd_sys.clk = ft600.clk

        counter = Signal(32)
        timer = Signal(32)
        prefetch_cnt = Signal(max=2)

        if TESTING:
            self.ft_be = TSTripleFake(2)
        else:
            ft_be_triple = TSTriple(2)
            self.ft_be = ft_be_triple.get_tristate(ft600.be)
            self.specials += self.ft_be

        if TESTING:
            self.ft_data = TSTripleFake(16)
        else:
            ft_data_triple = TSTriple(16)
            self.ft_data = ft_data_triple.get_tristate(ft600.data)
            self.specials += self.ft_data

        width = 16
        depth = 2048
        self.specials.mem = Memory(width, depth)
        wrport = self.mem.get_port(write_capable=True)
        rdport = self.mem.get_port(has_re=False)
        self.specials += wrport, rdport

        words_received = Signal(16, reset=0)
        read_word_at = Signal(16, reset=0)

        self.comb += [
            leds[0].eq(counter[0]),
            rdport.adr.eq(read_word_at),
        ]
 
        self.sync += [
            counter.eq(counter + 1),
        ]

        self.submodules.fsm = FSM(reset_state="INIT")
        self.fsm.act(
            "INIT",
            NextValue(ft600.oe_n, 1),
            NextValue(ft600.rd_n, 1),
            NextValue(ft600.wr_n, 1),
            NextValue(self.ft_be.oe, 0),
            NextValue(self.ft_data.oe, 0),
            NextValue(wrport.we, 0),
            If(
                counter == 3,
                NextState("WAIT-INPUT")
            )
        )

        self.fsm.act(
            "WAIT-INPUT",
            NextValue(leds[2], 1),
            NextValue(ft600.oe_n, 1),
            NextValue(ft600.rd_n, 1),
            NextValue(ft600.wr_n, 1),
            NextValue(self.ft_be.oe, 0),
            NextValue(self.ft_data.oe, 0),
            NextValue(wrport.we, 0),

            If(
                (ft600.txe_n == 0) & (words_received != 0),
                NextValue(leds[2], 0),
                NextValue(prefetch_cnt, 0),
                NextState("WRITE-WORD-PREFETCH"),
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
                NextValue(wrport.we, 0),
                NextState("WAIT-INPUT")
            ).Else(
                NextValue(words_received, words_received + 1),
                NextValue(wrport.we, 1),
                NextValue(wrport.adr, words_received),
                NextValue(wrport.dat_w, self.ft_data.i),
            )
        )
        self.fsm.act(
            "WRITE-WORD-PREFETCH",
            # This state makes sure the BRAM fetch is getting started. Ignoring words_received currently though..
            NextValue(read_word_at, read_word_at + 1),
            NextValue(prefetch_cnt, prefetch_cnt + 1),
            If (prefetch_cnt == 1,
                NextState("WRITE-WORD"),
            )
        )
        self.fsm.act(
            "WRITE-WORD",
            NextValue(leds[6], 1),
            NextValue(ft600.wr_n, 0),

            # NextValue(rdport.adr, read_word_at),
            NextValue(self.ft_data.o, rdport.dat_r),
            NextValue(self.ft_data.oe, 1),

            NextValue(self.ft_be.oe, 1),
            NextValue(self.ft_be.o, 0b11),
            If(
                (ft600.txe_n == 1) | (read_word_at == words_received),
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
        yield self.ft_be.i.eq(0)
        yield
        yield
        yield
        yield
        yield

        # FT will write 4 words to the bus master (fpga)
        # This should immitate Figure 4.6 in the datasheet as close as possible.
        yield ft600.rxf_n.eq(0)

        # Simulate hardware waiting for both oe_n and rd_n going low
        while ((yield ft600.oe_n) or (yield ft600.rd_n)):
            yield

        # clk 0
        yield self.ft_be.i.eq(0b11)
        yield self.ft_data.i.eq(0x1122)
        yield
        # clk 1
        yield self.ft_data.i.eq(0x3344)
        yield
        # clk 2
        yield self.ft_data.i.eq(0x5566)
        yield
        # clk 3
        yield self.ft_data.i.eq(0x7788)
        yield
        # clk 4
        yield self.ft_data.i.eq(0x99AA)
        yield
        # clk 4
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



def build_gateware(testing):
    # So ugly but I don't care
    global TESTING
    TESTING = testing

    import kilsyth

    target_clock_mhz = 100

    target = os.environ["TARGET"] if "TARGET" in os.environ else "lfe5u12"
    plat = kilsyth.Platform(toolchain='trellis', target=target)
    plat.add_period_constraint("ft600", 1000. / target_clock_mhz)
    clk = plat.request("clk16")
    leds = [plat.request('user_led', i) for i in range(8)]
    ft600 = plat.request('ft600')
 
    ft600pipe = FT600Pipe(clk, leds, ft600)

    if TESTING:
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
