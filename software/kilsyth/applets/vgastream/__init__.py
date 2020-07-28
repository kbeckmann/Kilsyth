from nmigen import *
from nmigen.build import *
from nmigen.lib.fifo import *

from pergola.util.ecp5pll import *
from pergola.gateware.dvid2vga import *
from pergola.gateware.vga import *
from pergola.gateware.vga_testimage import *
from pergola.gateware.gearbox import *

import os, sys, time, random, string, struct, random
import asyncio
from threading import Thread

import v4l2
import fcntl

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

    VSYNC_BITS = 64
    # VSYNC_MAGIC = random.randint(0, (2 ** VSYNC_BITS) - 1)
    VSYNC_MAGIC = 0xf22b7860ceba5ae9

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

        #### DVID in
        pixel_freq_mhz = 25
        platform.add_resources([
            Resource("lvds", 0, Pins("A2 A4 C4", dir="i"), # 7+/8-, 15+/19-, 17+/18-, 
                     Attrs(IO_TYPE="LVDS", DIFFRESISTOR=100)
                     ),
            Resource("lvds_clk", 0, Pins("C1", dir="i"),   # 5+/6-
                     Attrs(IO_TYPE="LVDS", DIFFRESISTOR=100),
                     Clock(pixel_freq_mhz * 1e6)),
        ])

        platform.add_resources([
            Resource("pmod1_lvds", 0, Pins("J1 L1 N1", dir="i"),
                     Attrs(IO_TYPE="LVDS", DIFFRESISTOR=100)),
            Resource("pmod1_lvds_clk", 0, Pins("G1", dir="i"),
                     Attrs(IO_TYPE="LVDS", DIFFRESISTOR=100),
                     Clock(pixel_freq_mhz * 1e6)),
        ])

        xdr = 1
        dvid_in = platform.request("lvds", 0, xdr=xdr)

        if xdr == 1:
            pll_config = [
                ECP5PLLConfig("shift", pixel_freq_mhz * 10.),
                ECP5PLLConfig("sync", pixel_freq_mhz),
            ]
        elif xdr == 2:
            pll_config = [
                ECP5PLLConfig("shift", pixel_freq_mhz * 10. / 2.),
                ECP5PLLConfig("sync", pixel_freq_mhz),
            ]
        elif xdr == 4:
            pll_config = [
                ECP5PLLConfig("shift_fast", pixel_freq_mhz * 10. / 2.),
                ECP5PLLConfig("shift", pixel_freq_mhz * 10. / 2. / 2.),
                ECP5PLLConfig("sync", pixel_freq_mhz),
            ]

        m.submodules.pll = ECP5PLL(
            pll_config,
            clock_signal_name="lvds_clk",
            clock_signal_freq=pixel_freq_mhz * 1e6)

        dvid_in_d0 = Signal(xdr)
        dvid_in_d1 = Signal(xdr)
        dvid_in_d2 = Signal(xdr)

        if xdr == 1:
            m.d.comb += [
                dvid_in.i_clk.eq(ClockSignal("shift")),
                dvid_in_d0.eq(dvid_in.i[0]),
                dvid_in_d1.eq(dvid_in.i[1]),
                dvid_in_d2.eq(dvid_in.i[2]),
            ]
        elif xdr == 2:
            m.d.comb += [
                dvid_in.i_clk.eq(ClockSignal("shift")),
                dvid_in_d0.eq(Cat(dvid_in.i0[0], dvid_in.i1[0])),
                dvid_in_d1.eq(Cat(dvid_in.i0[1], dvid_in.i1[1])),
                dvid_in_d2.eq(Cat(dvid_in.i0[2], dvid_in.i1[2])),
            ]
        elif xdr == 4:
            m.d.comb += [
                dvid_in.i_clk.eq(ClockSignal("shift")),
                dvid_in.i_fclk.eq(ClockSignal("shift_fast")),
                dvid_in_d0.eq(Cat(dvid_in.i0[0], dvid_in.i1[0], dvid_in.i2[0], dvid_in.i3[0])),
                dvid_in_d1.eq(Cat(dvid_in.i0[1], dvid_in.i1[1], dvid_in.i2[1], dvid_in.i3[1])),
                dvid_in_d2.eq(Cat(dvid_in.i0[2], dvid_in.i1[2], dvid_in.i2[2], dvid_in.i3[2])),
            ]


        decoded_r = Signal(8)
        decoded_g = Signal(8)
        decoded_b = Signal(8)
        decoded_de0 = Signal()
        decoded_hsync = Signal()
        decoded_vsync = Signal()
        decoded_de1 = Signal()
        decoded_ctl0 = Signal()
        decoded_ctl1 = Signal()
        decoded_de2 = Signal()
        decoded_ctl2 = Signal()
        decoded_ctl3 = Signal()

        m.submodules.dvid2vga = dvid2vga = DVID2VGA(
            in_d0=dvid_in_d0,
            in_d1=dvid_in_d1,
            in_d2=dvid_in_d2,

            out_r=decoded_r,
            out_g=decoded_g,
            out_b=decoded_b,
            out_de0=decoded_de0,
            out_hsync=decoded_hsync,
            out_vsync=decoded_vsync,
            out_de1=decoded_de1,
            out_ctl0=decoded_ctl0,
            out_ctl1=decoded_ctl1,
            out_de2=decoded_de2,
            out_ctl2=decoded_ctl2,
            out_ctl3=decoded_ctl3,

            xdr=xdr
        )

        ####

        # LED 0 will blink if there is a DVID clock source
        led_counter = Signal(24)
        m.d.sync += led_counter.eq(led_counter + 1)
        m.d.sync += leds[0].eq(led_counter[-1])

        fifo_width = 16
        depth = 1024 * 8 + 1
        # depth = 1024 * 16 + 1

        # Make it small, don't care
        m.submodules.fifo_rx = fifo_rx = AsyncFIFOBuffered(
            width=fifo_width,
            depth=5,
            exact_depth=True,
            w_domain="ftclk",
            r_domain="sync",
        )

        m.submodules.fifo_pixels = fifo_pixels = AsyncFIFOBuffered(
            width=fifo_width,
            depth=depth,
            exact_depth=True,
            w_domain="sync",
            r_domain="ftclk",
        )

        # This FIFO acts as a mux
        m.submodules.fifo_tx = fifo_tx = DomainRenamer("ftclk")(SyncFIFOBuffered(
            width=fifo_width,
            depth=1024,
        ))

        # Ping/pong buffers
        m.submodules.fifo_a = fifo_a = DomainRenamer("ftclk")(SyncFIFOBuffered(
            width=fifo_width,
            depth=4096 * 8 // fifo_width, # 4096 bytes
        ))

        m.submodules.fifo_b = fifo_b = DomainRenamer("ftclk")(SyncFIFOBuffered(
            width=fifo_width,
            depth=4096 * 8 // fifo_width, # 4096 bytes
        ))

        # debug = leds[-3:]
        debug = Signal(3)
        m.submodules.ft600 = DomainRenamer("ftclk")(FT600(ft600_pins, fifo_rx, fifo_tx, debug))

        # Ping/pong buffer
        with m.FSM(reset="A", domain="ftclk") as fsm:
            with m.State("A"):
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
                    m.next = "B"
            with m.State("B"):
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
                    m.next = "A"

        ############

        de0_r = Signal()
        hsync_r = Signal()
        vsync_r = Signal()
        vsync_ctr = Signal(self.VSYNC_BITS // 16 + 1)
        vsync_magic = Signal(self.VSYNC_BITS)

        data_seen_ctr = Signal(12)
        sent_vsync = Signal()

        m.d.sync += de0_r.eq(decoded_de0)
        m.d.sync += hsync_r.eq(decoded_hsync)
        m.d.sync += vsync_r.eq(decoded_vsync)
        m.d.sync += data_seen_ctr.eq(data_seen_ctr - 1)

        # This is a very hacky way to detect vblank.
        # It counts number of cycles since active data was seen last time,
        # which happens before/after every row but also when we get vsync.
        # If we haven't seen data in a long while, it's safe to assume
        # that we're in the vblanking area, so we end the frame there.
        # sent_vsync is there so we only send one sync word.

        with m.If(fifo_pixels.w_rdy):
            with m.If(~decoded_de0 & ~data_seen_ctr[11] & ~sent_vsync):
                m.d.sync += vsync_magic.eq(self.VSYNC_MAGIC)
                m.d.sync += vsync_ctr.eq(self.VSYNC_BITS // 16)
                m.d.sync += data_seen_ctr.eq(0)
                m.d.sync += sent_vsync.eq(1)
                

            with m.If(decoded_de0):
                # TODO: We need to store RGB(24b) in 16 bits chunks
                # Convert to RGB565 for now.
                rgb565le = Cat(decoded_b[-5:], decoded_g[-6:], decoded_r[-5:])
                m.d.comb += fifo_pixels.w_data.eq(rgb565le)
                m.d.comb += fifo_pixels.w_en.eq(1)
                m.d.sync += data_seen_ctr.eq(2**12 - 1)
                m.d.sync += sent_vsync.eq(0)

            with m.Elif(vsync_ctr != 0):
                m.d.comb += fifo_pixels.w_data.eq(vsync_magic[:16])
                m.d.comb += fifo_pixels.w_en.eq(1)
                m.d.sync += vsync_magic.eq(vsync_magic[16:])
                m.d.sync += vsync_ctr.eq(vsync_ctr - 1)

        # Light up an LED for 0.5 seconds every time we overflow the fifo
        overflow_cnt = Signal(32, reset=10000000)
        with m.If(overflow_cnt != 0):
            m.d.sync += overflow_cnt.eq(overflow_cnt - 1)

        m.d.sync += leds[-1].eq(overflow_cnt != 0)

        with m.If(~fifo_pixels.w_rdy):
            m.d.sync += overflow_cnt.eq(10000000)

        return m



    def consumer_fn(self, ft60x, f):
        print("consumer")
        size = 4096
        bytesRead = 0
        bytesReadTotal = 0

        t0 = time.time()
        packet = 0
        frame = 0

        vsync = struct.pack("<Q", self.VSYNC_MAGIC)

        # TODO: Keep a static framebuffer and write to it instead
        framebuffer = bytes()

        while (True):
            output = ft60x.read(size)
            if len(output) == 0:
                break

            packet += 1

            offset = output.find(vsync)
            if offset >= 0:
                frame += 1

                framebuffer += output[:offset]
                f.write(framebuffer)
                
                # Frame boundary

                framebuffer = output[offset + self.VSYNC_BITS // 8:]
            else:
                framebuffer += output

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
        # Open camera driver
        fd = open('/dev/video0', 'wb')

        BUFTYPE = v4l2.V4L2_BUF_TYPE_VIDEO_OUTPUT
        MEMTYPE = v4l2.V4L2_MEMORY_MMAP
        FRAME_FORMAT = v4l2.V4L2_PIX_FMT_RGB565

        # Set format
        width = 640
        height = 480
        sizeimage = width * height * 2
        linewidth = 640

        fmt = v4l2.v4l2_format()
        fmt.type = BUFTYPE
        fmt.fmt.pix.width        = width
        fmt.fmt.pix.height       = height
        fmt.fmt.pix.pixelformat  = FRAME_FORMAT
        fmt.fmt.pix.sizeimage    = sizeimage
        fmt.fmt.pix.field        = v4l2.V4L2_FIELD_NONE
        fmt.fmt.pix.bytesperline = linewidth
        fmt.fmt.pix.colorspace   = v4l2.V4L2_COLORSPACE_SRGB

        ret = fcntl.ioctl(fd, v4l2.VIDIOC_S_FMT, fmt)
        print("fcntl.ioctl(fd, v4l2.VIDIOC_S_FMT, fmt) = %d" % ret)

        buffer_size = fmt.fmt.pix.sizeimage
        print("buffer_size = " + str(buffer_size))


        print("Init ft60x driver")
        self.ftd3xx = FTD3xxWrapper()
        read_bytes = self.consumer_fn(self.ftd3xx, fd)

