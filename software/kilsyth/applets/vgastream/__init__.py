from nmigen import *
from nmigen.build import *
from nmigen.lib.fifo import *

from pergola.util.ecp5pll import *
from pergola.gateware.vga import *
from pergola.gateware.vga_testimage import *
from pergola.gateware.gearbox import *

import os, sys, time, random, string
import asyncio
from threading import Thread

from .. import Applet
from ...gateware import *

from ...host import *


vga_configs = {
    "640x480p60": VGAParameters(
            h_front=16,
            h_sync=96,
            h_back=44,
            h_active=640,
            v_front=10,
            v_sync=2,
            v_back=31,
            v_active=480,
        )
}

class VGAStreamApplet(Applet, applet_name="vgastream"):
    description = "VGA streamer"
    help = "Streams vga frames"

    @classmethod
    def add_build_arguments(cls, parser):
        parser.add_argument(
            "-o", "--output-file", type=str, default="out.bin",
            help="Capture to file")

    def __init__(self, args):
        self.args = args

    def elaborate(self, platform):
        m = Module()

        leds = Cat([platform.request("led", i).o for i in range(8)])
        ft600_pins = platform.request("ft600", 0)

        m.domains += ClockDomain("ftclk")
        m.d.comb += ClockSignal(domain="ftclk").eq(ft600_pins.clk)

        pll_config = [
            # ECP5PLLConfig("clk200", 200),
            # ECP5PLLConfig("clk100", 100),
            ECP5PLLConfig("vga", 25),
        ]

        m.submodules.pll = ECP5PLL(
            pll_config,
            clock_signal_name="ftclk",
            clock_signal_freq=100e6)

        fifo_width = 16
        depth = 1024 * 4 + 1

        # Make it small, don't care
        m.submodules.fifo_rx = fifo_rx = AsyncFIFOBuffered(
            width=fifo_width,
            depth=5,
            exact_depth=True,
            w_domain="ftclk",
            r_domain="vga",
        )

        m.submodules.fifo_pixels = fifo_pixels = AsyncFIFOBuffered(
            width=fifo_width,
            depth=depth,
            exact_depth=True,
            w_domain="vga",
            r_domain="ftclk",
        )

        # This FIFO acts as a mux
        m.submodules.fifo_tx = fifo_tx = DomainRenamer("ftclk")(SyncFIFO(
            width=fifo_width,
            depth=2,
            fwft=True,
        ))

        # Ping/pong buffers
        m.submodules.fifo_a = fifo_a = DomainRenamer("ftclk")(SyncFIFOBuffered(
            width=fifo_width,
            depth=4096 * 8 // fifo_width,
        ))

        m.submodules.fifo_b = fifo_b = DomainRenamer("ftclk")(SyncFIFOBuffered(
            width=fifo_width,
            depth=4096 * 8 // fifo_width,
        ))

        # debug = leds[-3:]
        debug = Signal(3)
        m.submodules.ft600 = DomainRenamer("ftclk")(FT600(ft600_pins, fifo_rx, fifo_tx, debug))

        # Test
        # m.d.comb += fifo_tx.w_en.eq(fifo_tx.w_rdy)
        # m.d.comb += fifo_tx.w_data.eq(0x1337)

        # Ping/pong buffer
        with m.FSM(reset="BUF_A", domain="ftclk") as fsm:
            with m.State("BUF_A"):
                # fifo_a is active: Write to a, read from b.
                m.d.comb += [
                    fifo_a.w_data.eq(fifo_pixels.r_data),
                    fifo_a.w_en.eq(fifo_a.w_rdy & fifo_pixels.r_rdy),
                    fifo_pixels.r_en.eq(fifo_a.w_rdy & fifo_pixels.r_rdy),

                    fifo_tx.w_en.eq(fifo_tx.w_rdy & fifo_b.r_rdy),
                    fifo_b.r_en.eq(fifo_tx.w_rdy & fifo_b.r_rdy),
                    fifo_tx.w_data.eq(fifo_b.r_data),
                ]
                # Swap active buffers when a is full and b is empty
                with m.If(~fifo_a.w_rdy & ~fifo_b.r_rdy):
                    m.next = "BUF_B"
            with m.State("BUF_B"):
                m.d.comb += [
                    fifo_b.w_data.eq(fifo_pixels.r_data),
                    fifo_b.w_en.eq(fifo_b.w_rdy & fifo_pixels.r_rdy),
                    fifo_pixels.r_en.eq(fifo_b.w_rdy & fifo_pixels.r_rdy),

                    fifo_tx.w_en.eq(fifo_tx.w_rdy & fifo_a.r_rdy),
                    fifo_a.r_en.eq(fifo_tx.w_rdy & fifo_a.r_rdy),
                    fifo_tx.w_data.eq(fifo_a.r_data),
                ]
                # Swap active buffers when b is full and a is empty
                with m.If(~fifo_b.w_rdy & ~fifo_a.r_rdy):
                    m.next = "BUF_A"

        ############
        # VGA signal generator
        ############

        vga_output = Record([
            ('hs', 1),
            ('vs', 1),
            ('blank', 1),
        ])

        r = Signal(8)
        g = Signal(8)
        b = Signal(8)

        m.submodules.vga = DomainRenamer("vga")(VGAOutputSubtarget(
            output=vga_output,
            vga_parameters=vga_configs["640x480p60"],
        ))

        vs = vga_output.vs
        v_en = m.submodules.vga.v_en
        h_en = m.submodules.vga.h_en

        # m.submodules.imagegen = DomainRenamer("vga")(StaticTestImageGenerator(
        #     vsync=vga_output.vs,
        #     h_ctr=m.submodules.vga.h_ctr,
        #     v_ctr=m.submodules.vga.v_ctr,
        #     r=r,
        #     g=g,
        #     b=b,
        # ))

        m.submodules.imagegen = DomainRenamer("vga")(TestImageGenerator(
            vsync=vga_output.vs,
            h_ctr=m.submodules.vga.h_ctr,
            v_ctr=m.submodules.vga.v_ctr,
            r=r,
            g=g,
            b=b,
            speed=0))

        ############################

        # TODO: We need to store RGB(24b) in 16 bits chunks
        # Convert to RGB565 for now.
        m.d.comb += fifo_pixels.w_data.eq(Cat(r[-5:], g[-6:], b[-5:]))
        m.d.comb += fifo_pixels.w_en.eq(fifo_pixels.w_rdy & h_en & v_en)

        # Light up an LED for 0.5 seconds every time we overflow the fifo
        overflow_cnt = Signal(32, reset=1000000)
        with m.If(overflow_cnt != 0):
            m.d.vga += overflow_cnt.eq(overflow_cnt - 1)

        m.d.ftclk += leds[-1].eq(overflow_cnt != 0)

        with m.If(~fifo_pixels.w_rdy):
            m.d.vga += overflow_cnt.eq(1000000)

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
