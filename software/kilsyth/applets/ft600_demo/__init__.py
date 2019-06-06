from migen import *
from migen.genlib.fifo import SyncFIFO, AsyncFIFO, AsyncFIFOBuffered
import os, sys

from .. import KilsythApplet
from ...gateware.ft600 import *

class FT600Demo(KilsythApplet, name="ft600_demo"):
    description = "FT600 TX demo"
    help = "Sends an increasing counter to the ft600 interface"

    def __init__(self, device):
        self.device = device

        led = device.request('user_led')
        ft600_pins = device.request('ft600')
        clk16 = device.request('clk16')

        device.add_period_constraint("ft600", 1000. / 100)

        self.clock_domains.cd_por = ClockDomain()
        self.clock_domains.cd_sys = ClockDomain(reset_less=False)

        # Posedge
        self.comb += self.cd_sys.clk.eq(ft600_pins.clk)

        # Negedge
        # self.comb += self.cd_sys.clk.eq(~ft600_pins.clk)

        self.clock_domains.cd_clk16 = ClockDomain(reset_less=False)
        self.cd_clk16.clk = clk16

        depth = 1024 * 16

        fifo_rx = SyncFIFO(16, depth)
        self.submodules += fifo_rx

        fifo_tx = ClockDomainsRenamer({
            "write": "sys",
            "read":  "sys",
        })(AsyncFIFO(16, depth))
        self.submodules += fifo_tx

        # fifo_tx = SyncFIFO(16, depth)
        # self.submodules += fifo_tx


        debug = Signal(8)
        self.submodules.ft600 = FT600(ft600_pins, fifo_rx, fifo_tx, debug)

        overflow = Signal()
        self.comb += [
            led[0].eq(~fifo_tx.writable),
            led[1].eq(overflow),
        ]

        if False:
            # Write as fast as possible
            # Constantly write to the FIFO,
            # Increase the counter on each clk
            # This works 100% perfectly
            counter = Signal(8)
            self.comb += [
                fifo_tx.din.eq(
                    ((counter + 1) << 8) |
                    ((counter    )     )
                ),
            ]
            self.sync += [
                If (~fifo_tx.writable,
                    overflow.eq(1),
                    fifo_tx.we.eq(0),
                ).Else(
                    fifo_tx.we.eq(1),
                    counter.eq(counter + 2)
                ),
            ]
        else:
            # Write every nth clock cycle
            counter = Signal(32)
            counter2 = Signal(8)
            self.comb += [
                fifo_tx.din.eq(
                    ((counter2 + 1) << 8) |
                    ((counter2    )     )
                ),
                If(counter == 0,
                    fifo_tx.we.eq(1),
                ).Else(
                    fifo_tx.we.eq(0),
                ),
            ]


            # xxd -p -c 256 dump.raww | sort | uniq -c | sort -n

            cnt_max = int(100e6 / 10000)
            cnt_max = 99

            # Going faster than this leads to issues:
            # cnt_max = 4

            self.sync += [
                If (~fifo_tx.writable,
                    overflow.eq(1)
                ),

                If (counter == cnt_max,
                    counter.eq(0),
                    counter2.eq(counter2 + 2)
                ).Else(
                    counter.eq(counter + 1)
                )
            ]

    def build(self):
        self.device.build(self, toolchain_path='/usr/share/trellis')
