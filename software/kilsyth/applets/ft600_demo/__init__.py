from nmigen import *
from nmigen.lib.fifo import AsyncFIFOBuffered

import os, sys, time, random, string, struct
import asyncio
from threading import Thread

from .. import Applet
from ...gateware import *

from ...host import *


SOURCE = "source"
SINK = "sink"
LOOPBACK = "loopback"
_all_modes = [SOURCE, SINK, LOOPBACK]

SOURCE_COUNTER_BITS = 16

class FT600Demo(Elaboratable):
    def __init__(self, leds, pins, mode, count=0):
        self.leds = leds
        self.pins = pins
        self.mode = mode
        self.count = count

        timer_width = 24
        self.timer = Signal(timer_width)

    def elaborate(self, platform):
        pins = self.pins
        leds = self.leds
        mode = self.mode
        count = self.count

        m = Module()

        m.domains += ClockDomain("clk100")
        m.d.comb += ClockSignal(domain="clk100").eq(pins.clk)

        fifo_width = 16
        depth = 1024 * 2 + 1

        m.submodules.fifo_rx = fifo_rx = AsyncFIFOBuffered(
            width=fifo_width,
            depth=depth,
            exact_depth=True,
            w_domain="clk100",
            r_domain="clk100",
        )

        m.submodules.fifo_tx = fifo_tx = AsyncFIFOBuffered(
            width=fifo_width,
            depth=depth,
            exact_depth=True,
            w_domain="clk100",
            r_domain="clk100",
        )

        debug = leds[-3:]
        m.submodules.ft600 = DomainRenamer("clk100")(FT600(pins, fifo_rx, fifo_tx, debug))

        if mode == SOURCE:
            # Test TX only
            counter = Signal(SOURCE_COUNTER_BITS)
            with m.If(fifo_tx.w_rdy):
                m.d.comb += [
                    fifo_tx.w_data.eq(Cat(counter[8:], counter[:8])),
                    fifo_tx.w_en.eq(1),
                ]
                m.d.clk100 += counter.eq(counter + 1)
        elif mode == SINK:
            # Test RX only
            counter = Signal(32)
            m.d.comb += fifo_rx.r_en.eq(counter == 0)

            with m.If(counter == count):
                m.d.clk100 += counter.eq(0)
            with m.Else():
                m.d.clk100 += counter.eq(counter + 1)
        elif mode == LOOPBACK:
            # Loopback
            m.d.comb += fifo_tx.w_data.eq(fifo_rx.r_data),
            with m.If(fifo_tx.w_rdy & fifo_rx.r_rdy):
                m.d.comb += fifo_tx.w_en.eq(1)
                m.d.comb += fifo_rx.r_en.eq(1)

        return m


class FT600DemoApplet(Applet, applet_name="ft600_demo"):
    description = "FT600 TX demo"
    help = "Sends an increasing counter to the ft600 interface"

    @classmethod
    def add_build_arguments(cls, parser):
        parser.add_argument(
            "-c", "--count", metavar="COUNT", type=int, default=0,
            help="Skip COUNT cycles when reading/writing (default: 0)")

        parser.add_argument(
            "--mode", choices=_all_modes, required=True,
            help="Set operation mode")

    def __init__(self, args):
        self.args = args

    def elaborate(self, platform):
        m = Module()

        leds = Cat([platform.request("led", i).o for i in range(8)])
        ft600_pins = platform.request("ft600", 0)

        m.submodules.ft600_demo = FT600Demo(leds, ft600_pins, self.args.mode)

        return m

    def producer_fn(self, ft60x, data, total_size):
        print("producer")
        size = 4096
        totalBytesWritten = 0
        bytesWrittenTemp = 0
        tstart = t0 = time.time()

        for x in range(0, total_size // size):
            start = (x * size) % len(data)
            end = ((x + 1) * size) % len(data)
            end = len(data) if end == 0 else end

            bytesWritten = ft60x.write(data[start:end])
            if bytesWritten == 0:
                break
            totalBytesWritten += bytesWritten
            bytesWrittenTemp += bytesWritten

            if bytesWrittenTemp > 1024*1024*100:
                diff = time.time() - t0
                t0 = time.time()
                print("wrote %d bytes (%.2f MB/s)" % (bytesWrittenTemp, bytesWrittenTemp / 1024. / 1024. / diff))
                bytesWrittenTemp = 0

        diff = time.time() - tstart
        print("wrote %d bytes in %d seconds (%.2f MB/s)" % (totalBytesWritten, diff, totalBytesWritten / 1024. / 1024. / diff))


    def consumer_fn(self, ft60x, data, mode):
        print("consumer")

        size = 4096
        bytesRead = 0
        bytesReadTotal = 0

        t0 = time.time()
        packet = 0
        while (True):
            output = ft60x.read(size)
            if len(output) == 0:
                break

            start = (packet * size) % len(data)
            end = ((packet + 1) * size) % len(data)
            end = len(data) if end == 0 else end

            if output != data[start:end]:
                print("Mismatch")
                print("Expected:")
                print(data[start:end])
                print("Actual:")
                print(output)
                return 0

            packet += 1

            bytesRead += len(output)
            bytesReadTotal += len(output)
            if bytesRead % 10000000 < 4096:
                diff = time.time() - t0
                t0 = time.time()
                print("read %d bytes (%.2f MB/s)" % (bytesRead, bytesRead/1024./1024./diff))
                bytesRead = 0
        print("read %d bytes" % bytesReadTotal)
        return bytesReadTotal


    async def run(self, args):
        print("Init ft60x driver")
        self.ftd3xx = FTD3xxWrapper()


        if args.mode == LOOPBACK:
            print("Generate random data")
            size = 4096 * 1024
            total_size = size * 100
            data = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(size)).encode('latin1')

            print("Start loopback")
            producer = Thread(target=self.producer_fn, args=(self.ftd3xx, data, total_size))
            producer.start()

            read_bytes = self.consumer_fn(self.ftd3xx, data, args.mode)
            if read_bytes != total_size:
                raise Exception("Test failed..")
        elif args.mode == SINK:
            print("Generate sequence data")
            counter_n = 2 ** SOURCE_COUNTER_BITS
            data = struct.pack(">%dH" % counter_n, *range(0, counter_n))

            print("Start sink mode (pc -> fpga)")
            total_size = 1024 * 1024 * 1024
            producer = Thread(target=self.producer_fn, args=(self.ftd3xx, data, total_size))
            producer.start()
        elif args.mode == SOURCE:
            print("Generate sequence data")
            counter_n = 2 ** SOURCE_COUNTER_BITS
            data = struct.pack(">%dH" % counter_n, *range(0, counter_n))

            print("Start source mode (fpga -> pc)")
            read_bytes = self.consumer_fn(self.ftd3xx, data, args.mode)

        print("Test ok.")
