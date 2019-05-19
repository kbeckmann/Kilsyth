from migen import *
import argparse
import sys, os

TESTING = False

class TSTripleFake():
    def __init__(self, width):
        self.oe = Signal()
        self.o = Signal(width)
        self.i = Signal(width)

# How to use:
# cd software/ft600_test/linux-x86_64
# make
# LD_LIBRARY_PATH=. ./streamer 0 1 0 dump.raw
# sox -t raw -e unsigned -b 8 -c 2 -r 48000 dump.raw  -t raw -e floating-point -b 32 -c 2 -r 48000 out.raw
# gqrx config: file=/home/konrad/dev/Kilsyth/software/ft600_test/linux-x86_64/out.raw,freq=868e6,rate=500e3,repeat=true,throttle=true
#

class RXSampler(Module):
    # pmod0.pin2 => CLK_OUT
    # pmod0.pin5 => I_OUT
    # pmod0.pin6 => Q_OUT
    # out_i = Signal(8)
    # out_q = Signal(8)
    # data_ready = out Signal()
    # data_consumed = input Signal()
    def __init__(self, pmod0, out_i, out_q, data_ready, data_consumed):
        sample_i = Signal(8)
        sample_q = Signal(8)
        counter = Signal(16)

        # TODO: fix clock domain crossing properly...
        self.comb += [
            If (counter == 0,
                data_ready.eq(1)
            ).Else(
                data_ready.eq(0)
            )
        ]
 
        self.sync += [
            If (counter == 72, # gives 500kHz bandwidth with a 36MHz clock
                sample_i.eq(pmod0.pin5),
                sample_q.eq(pmod0.pin6),
                out_i.eq(sample_i),
                out_q.eq(sample_q),
                counter.eq(0),
            ).Else(
                sample_i.eq(sample_i + pmod0.pin5),
                sample_q.eq(sample_q + pmod0.pin6),
                counter.eq(counter + 1),
            )

        ]

class FT600Pipe(Module):
    def __init__(self, leds, ft600, pmod0):
        self.clock_domains.cd_por = ClockDomain()
        self.clock_domains.cd_sys = ClockDomain(reset_less=False)
        self.clock_domains.cd_sx1257 = ClockDomain(reset_less=True)
        self.cd_sys.clk = ft600.clk
        self.cd_sx1257.clk = pmod0.pin2

        out_i = Signal(8)
        out_q = Signal(8)
        data_ready = Signal()
        data_consumed = Signal()
        rxsamples = ClockDomainsRenamer({"sys": "sx1257"})(RXSampler(pmod0, out_i, out_q, data_ready, data_consumed))
        self.submodules += rxsamples

        counter = Signal(32)

        if TESTING:
            self.ft_be = TSTripleFake(2)
            self.ft_data = TSTripleFake(16)
        else:
            ft_be_triple = TSTriple(2)
            self.ft_be = ft_be_triple.get_tristate(ft600.be)
            self.specials += self.ft_be

            ft_data_triple = TSTriple(16)
            self.ft_data = ft_data_triple.get_tristate(ft600.data)
            self.specials += self.ft_data

        self.comb += [
            leds[0].eq(counter[0]),
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
            NextValue(leds[5], 1),
            NextValue(leds[6], 0),
            NextValue(leds[7], 0),
            NextState("WAIT-FOR-SAMPLE")
        )

        self.fsm.act(
            "WAIT-FOR-SAMPLE",
            NextValue(leds[5], 0),
            NextValue(leds[6], 1),
            NextValue(leds[7], 0),
            NextValue(ft600.wr_n, 1),

            NextValue(self.ft_data.oe, 0),
            NextValue(self.ft_be.oe, 0),
            NextValue(self.ft_be.o, 0b00),

            If (data_ready,
                data_consumed.eq(1),
                NextState("WRITE-WORD")
            )
        )

        self.fsm.act(
            "WRITE-WORD",
            NextValue(leds[5], 0),
            NextValue(leds[6], 0),
            NextValue(leds[7], 1),
            NextValue(ft600.wr_n, 0),

            NextValue(self.ft_data.o, (out_i << 8) | out_q),
            NextValue(self.ft_data.oe, 1),

            NextValue(self.ft_be.oe, 1),
            NextValue(self.ft_be.o, 0b11),
            NextState("WAIT-FOR-SAMPLE")
        )

    def testbench(self, leds, ft600):
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
        yield
        yield
        yield
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

    target = os.environ["TARGET"] if "TARGET" in os.environ else "lfe5u45"
    plat = kilsyth.Platform(toolchain='trellis', target=target)
    plat.add_period_constraint("ft600", 1000. / target_clock_mhz)
    leds = [plat.request('user_led', i) for i in range(8)]
    ft600 = plat.request('ft600')
    pmod0 = plat.request('pmod0')
 
    ft600pipe = FT600Pipe(leds, ft600, pmod0)

    if TESTING:
        run_simulation(ft600pipe, ft600pipe.testbench(leds, ft600), vcd_name="out.vcd")
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
