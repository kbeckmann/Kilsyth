from migen import *
from migen.genlib.fifo import _FIFOInterface, AsyncFIFO, SyncFIFOBuffered
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


class IQSampler(Module):
    # pmod0.pin2 => CLK_OUT
    # pmod0.pin5 => I_OUT
    # pmod0.pin6 => Q_OUT
    # fifo = AsyncFifo()
    def __init__(self, pmod0, fifo):
        counter = Signal(3)
        sample_i = Signal(8)
        sample_q = Signal(8)

        self.comb += [
            fifo.din.eq(((sample_q) << 8) | sample_i),
            If((counter == 7) & fifo.writable,
                # if fifo.writable is false we will drop a sample
                fifo.we.eq(1),
            ).Else(
                fifo.we.eq(0),
            ),
        ]

        self.sync += [
            # LSB first
            # sample_i.eq((sample_i << 1) | pmod0.pin5),
            # sample_q.eq((sample_q << 1) | pmod0.pin6),

            # MSB first
            sample_i.eq((sample_i >> 1) | (pmod0.pin5 << 7)),
            sample_q.eq((sample_q >> 1) | (pmod0.pin6 << 7)),

            counter.eq(counter + 1),
        ]

class IQSamplerBad(Module):
    # pmod0.pin2 => CLK_OUT
    # pmod0.pin5 => I_OUT
    # pmod0.pin6 => Q_OUT
    # fifo = AsyncFifo()
    def __init__(self, pmod0, fifo):
        # Sample with 150kHz bandwidth assuming a 36MHz clock
        # 150kHz leads to a cnt_max of 240, samples are still <256
        cnt_max = 36000000 // 150000

        counter = Signal(max=cnt_max+1)
        sample_i = Signal(8)
        sample_q = Signal(8)

        self.comb += [
            fifo.din.eq(((sample_q) << 8) | sample_i),
            If((counter == cnt_max) & fifo.writable,
                # if fifo.writable is false we will drop a sample
                fifo.we.eq(1),
            ).Else(
                fifo.we.eq(0),
            ),
        ]

        self.sync += [
            If (counter == cnt_max,
                sample_i.eq(pmod0.pin5),
                sample_q.eq(pmod0.pin6),
                counter.eq(0),
            ).Else(
                sample_i.eq(sample_i + pmod0.pin5),
                sample_q.eq(sample_q + pmod0.pin6),
                counter.eq(counter + 1),
            )
        ]

class IQSamplerFake(Module):
    # Use this to test that we can count properly and not drop samples.
    def __init__(self, pmod0, fifo):
        counter = Signal(16)
        counter2 = Signal(8)

        self.comb += [
            fifo.din.eq(((counter2+1) << 8) | counter2),
            If((counter == 0) & fifo.writable,
                fifo.we.eq(1),
            ).Else(
                fifo.we.eq(0),
            ),
        ]

        self.sync += [
            # 72 = 500kHz bandwidth with a 36MHz clock
            If (counter == 72,
                counter.eq(0),
                counter2.eq(counter2 + 2)
            ).Else(
                counter.eq(counter + 1)
            )
        ]

class FT600Pipe(Module):
    def __init__(self, leds, ft600, pmod0):
        self.clock_domains.cd_por = ClockDomain()
        self.clock_domains.cd_sys = ClockDomain(reset_less=False)
        self.clock_domains.cd_sx1257 = ClockDomain(reset_less=True)
        self.cd_sys.clk = ft600.clk
        self.cd_sx1257.clk = pmod0.pin2

        # This can probably be a lot smaller
        depth = 256
        fifo = ClockDomainsRenamer({
            "write": "sx1257",
            "read":  "sys",
        })(AsyncFIFO(16, depth))
        self.submodules += fifo

        rxsamples = ClockDomainsRenamer({"sys": "sx1257"})(IQSampler(pmod0, fifo))
        # rxsamples = ClockDomainsRenamer({"sys": "sx1257"})(IQSamplerFake(pmod0, fifo))
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
            NextState("WAIT")
        )

        self.fsm.act(
            "WAIT",
            NextValue(leds[5], 0),
            NextValue(leds[6], 1),
            NextValue(leds[7], 0),
            NextValue(ft600.wr_n, 1),

            NextValue(self.ft_data.oe, 0),
            NextValue(self.ft_be.oe, 0),
            NextValue(self.ft_be.o, 0b00),

            If ((fifo.readable) & (~ft600.txe_n),
                NextValue(fifo.re, 1),
                NextState("WRITE")
            )
        )

        self.fsm.act(
            "WRITE",
            NextValue(leds[5], 0),
            NextValue(leds[6], 0),
            NextValue(leds[7], 1),
            NextValue(ft600.wr_n, 0),

            NextValue(self.ft_data.o, fifo.dout),
            NextValue(self.ft_data.oe, 1),

            NextValue(self.ft_be.oe, 1),
            NextValue(self.ft_be.o, 0b11),

            If ((~fifo.readable) | (ft600.txe_n),
                # There is nothing to read
                # or we are not allowed to write to ft600.
                # Time to wait.
                NextValue(fifo.re, 0),
                NextState("WAIT")
            )
        )

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
    
    if args.test:
        build_gateware(True)
    elif args.build:
        build_gateware(False)
