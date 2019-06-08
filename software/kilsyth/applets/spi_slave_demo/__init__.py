from migen import *
import os, sys

from .. import KilsythApplet

class SpiSlaveDemoImpl(Module):
    def __init__(self, mosi, miso, sck, nss, leds):
        buf = Signal(8)

        self.comb += leds.eq(buf)

        self.submodules.fsm = FSM(reset_state="IDLE")
        self.fsm.act(
            "IDLE",
            If (nss == 0,
                NextState("READ"),
                NextValue(buf, 0),
            )
        )

        self.fsm.act(
            "READ",
            If (nss == 1,
                NextState("IDLE"),
            ).Else(
                NextValue(buf, (buf << 1) | mosi),
            ),
        )    

class SpiSlaveDemo(KilsythApplet, name="spi_slave_demo"):
    help = "SPI Slave Demo"
    description = """
SPI Slave Demo
Sets registers over SPI
"""

    def __init__(self, device):
        self.device = device

        leds = device.request('user_led')
        wide = device.request('wide')

        mosi = wide[0]
        miso = wide[1]
        sck = wide[2]
        nss = wide[3]

        # Setup the "spi" clock domain
        self.clock_domains.cd_spi = ClockDomain(reset_less=False)
        self.comb += self.cd_spi.clk.eq(sck)

        # This wrapper renames the "sys" clock domain in SpiSlaveDemoImpl to "spi"
        slave = ClockDomainsRenamer({
            "sys": "spi",
        })(SpiSlaveDemoImpl(mosi, miso, sck, nss, leds))
        self.submodules += slave

    def build(self):
        self.device.build(self, toolchain_path='/usr/share/trellis')
