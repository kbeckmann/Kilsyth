from migen import *
from migen.genlib.fifo import SyncFIFO, AsyncFIFO, AsyncFIFOBuffered
import os, sys, time, random, string
import asyncio
from threading import Thread

from .. import KilsythApplet
from ...gateware import *

from ...host import *

class FT600Demo(KilsythApplet, name="ft600_demo"):
    description = "FT600 TX demo"
    help = "Sends an increasing counter to the ft600 interface"

    __all_modes = ["source", "sink", "loopback"]

    @classmethod
    def add_build_arguments(cls, parser):
        parser.add_argument(
            "-c", "--count", metavar="COUNT", type=int, default=0,
            help="Skip COUNT cycles when reading/writing (default: 0)")

        parser.add_argument(
            dest="mode", metavar="MODE", type=str, choices=cls.__all_modes,
            help="run benchmark mode MODE (one of {})".format(" ".join(cls.__all_modes)))

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

        if args.mode == "source":
            # Test TX only
            # Write counter every nth clock cycle
            counter = Signal(32)
            counter2 = Signal(8)
            self.comb += [
                fifo_tx.din.eq(
                    ((counter2 + 1) << 8) |
                    ((counter2    )     )
                ),
                fifo_tx.we.eq(counter == 0),
            ]

            self.sync += [
                If (counter == args.count,
                    counter.eq(0),
                    counter2.eq(counter2 + 2)
                ).Else(
                    counter.eq(counter + 1)
                )
            ]
        elif args.mode == "sink":
            # Test RX only
            counter = Signal(32)
            self.comb += [
                fifo_rx.re.eq(counter == 0),
            ]

            self.sync += [
                If (counter == args.count,
                    counter.eq(0),
                ).Else(
                    counter.eq(counter + 1)
                )
            ]
        elif args.mode == "loopback":
            # Loopback
            self.comb += [
                fifo_tx.din.eq(fifo_rx.dout),
                If(fifo_tx.writable & fifo_rx.readable,
                    fifo_tx.we.eq(1),
                    fifo_rx.re.eq(1),
                )
            ]


    def producer_fn(self, ft60x, data, total_size):
        print("producer")
        size = 4096
        totalBytesWritten = 0

        for x in range(0, total_size // size):
            start = (x * size) % len(data)
            end = ((x + 1) * size) % len(data)
            end = len(data) if end == 0 else end

            bytesWritten = ft60x.write(data[start:end])
            if bytesWritten == 0:
                break
            totalBytesWritten += bytesWritten
        print("wrote %d bytes" % totalBytesWritten)


    def consumer_fn(self, ft60x, data):
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
                print("Mismatch in loopback")
                return 0

            packet += 1

            bytesRead += len(output)
            bytesReadTotal += len(output)
            if bytesRead % 10000000 < 4096:
                diff = time.time() - t0
                t0 = time.time()
                print("read %d bytes (%.2f MB/s)" % (bytesRead, bytesRead/1024./1024./diff))
                bytesRead = 0
        print("read  %d bytes" % bytesReadTotal)
        return bytesReadTotal


    async def run(self):
        print("Init ft60x driver")
        self.ftd3xx = FTD3xxWrapper()

        print("Generate random data")
        size = 4096 * 1024
        total_size = size * 100
        data = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(size)).encode('latin1')

        print("Start loopback")
        producer = Thread(target=self.producer_fn, args=(self.ftd3xx, data, total_size))
        producer.start()
        
        read_bytes = self.consumer_fn(self.ftd3xx, data)
        if read_bytes != total_size:
            raise Exception("Test failed..")

        print("Test ok.")
