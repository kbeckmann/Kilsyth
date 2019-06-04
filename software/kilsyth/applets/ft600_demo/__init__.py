from migen import *
from migen.genlib.fifo import AsyncFIFO
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

        self.clock_domains.cd_por = ClockDomain()
        self.clock_domains.cd_sys = ClockDomain(reset_less=False)
        self.cd_sys.clk = ft600_pins.clk

        depth = 8
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

        debug = Signal(8)
        self.submodules.ft600 = FT600(ft600_pins, fifo_rx, fifo_tx, debug)


        counter = Signal(16)
        counter2 = Signal(8)
        overflow = Signal()

        self.comb += [
            # fifo_tx.din.eq(((counter2+1)[:8] << 8) | counter2),
            fifo_tx.din.eq((counter2 << 8) | counter2),
            # fifo_tx.din.eq(counter2),
            led.eq(overflow),
            If((counter == 0),
                fifo_tx.we.eq(1),
            ).Else(
                fifo_tx.we.eq(0),
            ),
        ]

        self.sync += [
            If (~fifo_tx.writable,
                overflow.eq(1)
            ),
            If (counter == 100,
                counter.eq(0),
                # counter2.eq(counter2 + 2)
                counter2.eq(counter2 + 1)
            ).Else(
                counter.eq(counter + 1)
            )
        ]

    def build(self):
        self.device.build(self, toolchain_path='/usr/share/trellis')
