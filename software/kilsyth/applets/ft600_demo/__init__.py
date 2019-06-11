from migen import *
from migen.genlib.fifo import SyncFIFO, AsyncFIFO, AsyncFIFOBuffered
import os, sys

from .. import KilsythApplet
from ...gateware.ft600 import *

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
