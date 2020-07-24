from nmigen import *
from nmigen.build import *
from nmigen.lib.fifo import *

import os, sys, time, random, string
import asyncio
from threading import Thread

from .. import Applet
from ...gateware import *

from ...host import *

class LogicAnalyzerApplet(Applet, applet_name="la"):
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

    def __init__(self, args):
        self.args = args

    def elaborate(self, platform):
        m = Module()

        platform.add_resources([
            Resource("lvds", 0, Pins("A4 C4 A2", dir="i"), # 15+/19-, 17+/18-, 7+/8-, 
                    Attrs(IO_TYPE="LVDS", DIFFRESISTOR="100")),
            Resource("lvds_clk", 0, Pins("B1", dir="i"),   # 5+/6-
                    Attrs(IO_TYPE="LVDS", DIFFRESISTOR="100")),
        ])


        leds = Cat([platform.request("led", i).o for i in range(8)])
        ft600_pins = platform.request("ft600", 0)

        m.domains += ClockDomain("ftclk")
        m.d.comb += ClockSignal(domain="ftclk").eq(ft600_pins.clk)

        pll_config = [
            ECP5PLLConfig("clk200", 200),
            ECP5PLLConfig("clk100", 100),
        ]

        m.submodules.pll = ECP5PLL(
            pll_config,
            clock_signal_name="ftclk",
            clock_signal_freq=100e6)

        # Sample 2 channels per clock
        xdr = 4
        channels = 2
        lvds = platform.request("lvds")
        q0 = Signal(channels)
        q1 = Signal(channels)
        q2 = Signal(channels)
        q3 = Signal(channels)

        # On each 100MHz clock
        for bit in range(channels):
            m.submodules += Instance("IDDRX2F",
                i_SCLK=ClockSignal("clk100"),
                i_ECLK=ClockSignal("clk200"),
                i_RST=0,
                i_D=lvds[bit],
                o_Q0=q0[bit], o_Q1=q1[bit], o_Q2=q2[bit], o_Q3=q3[bit]
            )


        fifo_width = 16
        depth = 1024 * 4 + 1

        # Make it small, don't care
        m.submodules.fifo_rx = fifo_rx = AsyncFIFOBuffered(
            width=fifo_width,
            depth=5,
            exact_depth=True,
            w_domain="clk100",
            r_domain="ftclk",
        )

        m.submodules.fifo_tx = fifo_tx = AsyncFIFOBuffered(
            width=fifo_width,
            depth=depth,
            exact_depth=True,
            w_domain="ftclk",
            r_domain="clk100",
        )

        debug = leds[-3:]
        m.submodules.ft600 = DomainRenamer("ftclk")(FT600(ft600_pins, fifo_rx, fifo_tx, debug))

        gearbox_factor = 16 // (channels * xdr)
        gearbox = Signal(16)
        m.d.clk100 += gearbox.eq(Cat(gearbox[channels * xdr:], q0, q1, q2, q3))

        gearbox_tick = Signal(range(100), reset=gearbox_factor - 1)
        m.d.clk100 += gearbox_tick.eq(gearbox_tick - 1)
        with m.If(gearbox_tick == 0):
            m.d.clk100 += gearbox_tick.eq(gearbox_factor - 1)

        # Light up an LED for 0.5 seconds every time we overflow the fifo
        overflow_cnt = Signal(32, reset=50000000)
        with m.If(overflow_cnt != 0):
            m.d.clk100 += overflow_cnt.eq(overflow_cnt - 1)

        m.d.comb += leds[0].eq(overflow_cnt != 0)

        with m.If(~fifo_tx.w_rdy):
            m.d.clk100 += overflow_cnt.eq(50000000)

        m.d.clk100 += [
            fifo_tx.w_data.eq(gearbox),
            fifo_tx.w_en.eq(gearbox_tick == 0),
        ]

        return m



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
