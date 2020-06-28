from migen import *
from migen.genlib.fifo import SyncFIFO, AsyncFIFO, AsyncFIFOBuffered
import os, sys, time, random, string
import asyncio
from threading import Thread

from .. import KilsythApplet
from ...gateware import *

from ...host import *

class LogicAnalyzerApplet(KilsythApplet, name="la"):
    description = "Logic analyzer"
    help = "Streams raw IO"

    @classmethod
    def add_build_arguments(cls, parser):
        parser.add_argument(
            "-f", "--frequency", type=float, default=100,
            help="Frequency of data acquisition")

        parser.add_argument(
            "-o", "--output-file", type=str, default="out.bin",
            help="Capture to file")

    def __init__(self, device, args):
        self.device = device

        led = device.request('user_led')
        ft600_pins = device.request('ft600')
        clk16 = device.request('clk16')


        self.clock_domains.cd_por = ClockDomain()
        self.clock_domains.cd_sys = ClockDomain(reset_less=False)
        self.cd_sys.clk = ft600_pins.clk
        device.add_period_constraint(ft600_pins.clk.backtrace[-1][0], 1000. / 100)

        self.clock_domains.cd_clk16 = ClockDomain(reset_less=False)
        self.cd_clk16.clk = clk16

        clk200 = Signal()
        self.clock_domains.cd_clk200 = ClockDomain(reset_less=False)
        self.cd_clk200.clk = clk200
        # device.add_period_constraint(clk200, 1000. / 200)

        clk400 = Signal()
        self.clock_domains.cd_clk400 = ClockDomain(reset_less=False)
        self.cd_clk400.clk = clk400
        # device.add_period_constraint(clk400, 1000. / 400)

        # Add PLL 100 MHz => 200MHz, 400MHz
        self.specials += Instance("EHXPLLL",

                # Clock in.
                i_CLKI=ft600_pins.clk,

                # Generated clock outputs.
                o_CLKOP=clk400, # 400 MHz
                o_CLKOS=clk200, # 200 MHz

                # Status.
                #o_LOCK=self._pll_lock,

                # PLL parameters...
                p_PLLRST_ENA="DISABLED",
                p_INTFB_WAKE="DISABLED",
                p_STDBY_ENABLE="DISABLED",
                p_DPHASE_SOURCE="DISABLED",
                p_PLL_LOCK_MODE=0,
                p_CLKOS_TRIM_DELAY="0",
                p_CLKOS_TRIM_POL="FALLING",
                p_CLKOP_TRIM_DELAY="0",
                p_CLKOP_TRIM_POL="FALLING",
                p_OUTDIVIDER_MUXD="DIVD",
                p_CLKOS3_ENABLE="DISABLED",
                p_OUTDIVIDER_MUXC="DIVC",
                p_CLKOS2_ENABLE="DISABLED",
                p_OUTDIVIDER_MUXB="DIVB",
                p_CLKOS_ENABLE="ENABLED",
                p_OUTDIVIDER_MUXA="DIVA",
                p_CLKOP_ENABLE="ENABLED",

                # 100 -> 200
                p_CLKI_DIV=1,
                p_CLKOP_DIV=1,
                p_CLKOP_CPHASE=0,
                p_CLKOP_FPHASE=0,
                p_CLKOS_DIV=2,
                p_CLKOS_CPHASE=0,
                p_CLKOS_FPHASE=0,
                p_CLKFB_DIV=4,

                p_FEEDBK_PATH="CLKOP",

                # Internal feedback.
                i_CLKFB=clk400,

                # Control signals.
                i_RST=0,
                i_PHASESEL0=0,
                i_PHASESEL1=0,
                i_PHASEDIR=1,
                i_PHASESTEP=1,
                i_PHASELOADREG=1,
                i_STDBY=0,
                i_PLLWAKESYNC=0,

                # Output Enables.
                i_ENCLKOP=0,
                i_ENCLKOS=0,
                i_ENCLKOS2=0,
                i_ENCLKOS3=0,

                # Synthesis attributes.
                # a_FREQUENCY_PIN_CLKI="16.000000",
                # a_FREQUENCY_PIN_CLKOP="400.000000",
                # a_ICP_CURRENT="12",
                # a_LPF_RESISTOR="8"
        )

        # Sample 2 channels per clock
        xdr = 4
        channels = 2
        wide = device.request("wide")
        q0 = Signal(channels)
        q1 = Signal(channels)
        q2 = Signal(channels)
        q3 = Signal(channels)

        for bit in range(channels):
            self.specials += Instance("IDDRX2F",
                i_SCLK=clk400,
                i_ECLK=clk200,
                i_RST=0,
                i_D=wide[bit],
                o_Q0=q0[bit], o_Q1=q1[bit], o_Q2=q2[bit], o_Q3=q3[bit]
            )


        depth = 1024 * 8


        # Make it small, don't care
        fifo_rx = ClockDomainsRenamer({
            "write": "sys",
            "read":  "sys",
        })(AsyncFIFOBuffered(16, 4))
        self.submodules += fifo_rx

        fifo_tx = ClockDomainsRenamer({
            "write": "sys",
            "read":  "sys",
        })(AsyncFIFOBuffered(16, depth))
        self.submodules += fifo_tx


        # debug = led[-3:]
        debug = Signal(3)
        self.submodules.ft600 = FT600(ft600_pins, fifo_rx, fifo_tx, debug)

        gearbox_factor = 16 // (channels * xdr)
        gearbox = Signal(16)
        self.sync += gearbox.eq(Cat(gearbox[channels * xdr:], q0, q1, q2, q3))
        # self.sync += gearbox.eq(Cat(gearbox[channels:], wide[:channels]))

        gearbox_tick = Signal(max=100, reset=gearbox_factor - 1)
        self.sync += gearbox_tick.eq(gearbox_tick - 1)
        self.sync += If(gearbox_tick == 0,
            gearbox_tick.eq(gearbox_factor - 1)
        )

        # Light up an LED for 0.5 seconds every time we overflow the fifo
        overflow_cnt = Signal(32, reset=50000000)
        self.sync += If(overflow_cnt != 0,
            overflow_cnt.eq(overflow_cnt - 1)
        )
        self.comb += led.eq(overflow_cnt != 0)
        self.sync += If(~fifo_tx.writable,
            overflow_cnt.eq(50000000)
        )

        self.sync += [
            fifo_tx.din.eq(gearbox),
            fifo_tx.we.eq(gearbox_tick == 0),
        ]


    def consumer_fn(self, ft60x, filename):
        print("consumer")
        size = 4096
        bytesRead = 0
        bytesReadTotal = 0

        t0 = time.time()
        packet = 0

        f = open(filename, "wb")
        while (True):
            output = ft60x.read(size)
            if len(output) == 0:
                break

            packet += 1

            f.write(output)

            bytesRead += len(output)
            bytesReadTotal += len(output)
            if bytesRead % 10000000 < 4096:
                diff = time.time() - t0
                t0 = time.time()
                print("read %d bytes (%.2f MB/s)" % (bytesRead, bytesRead/1024./1024./diff))
                bytesRead = 0
        print("read  %d bytes" % bytesReadTotal)
        f.close()
        return bytesReadTotal


    async def run(self, args):
        print("Init ft60x driver")
        self.ftd3xx = FTD3xxWrapper()

        read_bytes = self.consumer_fn(self.ftd3xx, args.output_file)

        print("""

        Post process with:
        gcc software/kilsyth/applets/la/unpack.c -o software/kilsyth/applets/la/unpack.elf;
        software/kilsyth/applets/la/unpack.elf out.bin out2.bin
        sigrok-cli -I binary:numchannels=2:samplerate=400000000 -i out2.bin -o out.sr

        """)
