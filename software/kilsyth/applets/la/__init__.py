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

        depth = 1024 * 2

        if False:
            fifo_rx = SyncFIFO(16, depth)
            self.submodules += fifo_rx

            fifo_tx = SyncFIFO(16, depth)
            self.submodules += fifo_tx
        else:
            # AsyncFIFO requires a depth of at least 8 to be able to run at max speed 
            fifo_rx = ClockDomainsRenamer({
                "write": "sys",
                "read":  "sys",
            })(AsyncFIFO(16, depth))
            self.submodules += fifo_rx

            fifo_tx = ClockDomainsRenamer({
                "write": "sys",
                "read":  "sys",
            })(AsyncFIFO(16, depth))
            self.submodules += fifo_tx


        debug = led[-3:]
        self.submodules.ft600 = FT600(ft600_pins, fifo_rx, fifo_tx, debug)

        wide = device.request("wide")

        self.comb += [
            fifo_tx.din.eq(wide[0:16]),
            fifo_tx.we.eq(1),
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

        print("Post process with e.g. sigrok-cli -I binary:numchannels=16:samplerate=100000000 -i out.bin -o out.sr")
