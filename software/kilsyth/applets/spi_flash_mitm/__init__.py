from migen import *
import os, sys

from .. import KilsythApplet

class SpiFlashMitm(KilsythApplet, name="spi_flash_mitm"):
    description = "SPI flash mitm proxy"
    help = "TODO"

    # PMOD0 -> SPI flash:
    # 1:
    # 2: IO3
    # 3: IO1
    # 4: ~CS
    # 5:
    # 6: CLK
    # 7: IO2
    # 8: IO0

    def __init__(self, device, args):
        self.device = device
        pmod0 = device.request('pmod0')

        self.clock_domains.cd_por = ClockDomain()
        self.clock_domains.cd_sys = ClockDomain(reset_less=False)
        self.cd_sys.clk = pmod0.pin6

        led = device.request('user_led')

        self.div = Signal(32)
        self.sync += self.div.eq(self.div + 1)
        self.comb += [
            led.eq(self.div),
            # led[0].eq(pmod0.pin1),
            # led[1].eq(pmod0.pin2),
            # led[2].eq(pmod0.pin3),
            # led[3].eq(pmod0.pin4),
            # led[4].eq(pmod0.pin5),
            # led[5].eq(pmod0.pin6),
            # led[6].eq(pmod0.pin7),
            # led[7].eq(pmod0.pin8),
        ]


        # self.submodules.fsm = FSM(reset_state="INIT")
        # self.fsm.act(
        #     "INIT",
        #     NextState("FOO")
        # )

        # self.fsm.act(
        #     "FOO",
        #     NextState("INIT")
        # )
