from migen import *
import os, sys

from .. import KilsythApplet

class SpiFlashMitm(KilsythApplet, name="spi_flash_mitm"):
    description = "SPI flash mitm proxy"
    help = "TODO"

    # PMOD0 -> SPI flash master:
    # 1:
    # 2: IO3
    # 3: IO1 / DO
    # 4: ~CS
    # 5:
    # 6: CLK
    # 7: IO2
    # 8: IO0 / DI

    # Actual SPI flash:
    # WIDE => SPI flash chip
    # 1: 1 ~CS
    # 2: 8 VCC
    # 3: 2 IO1 / DO
    # 4: 7 IO3
    # 5: 3 IO2
    # 6: 6 CLK
    # 7: 4 GND
    # 8: 5 IO0 / DI

    def __init__(self, device):
        self.device = device
        pmod0 = device.request('pmod0')

        spi_flash = device.request('spi_flash')

        self.clock_domains.cd_por = ClockDomain()
        self.clock_domains.cd_sys = ClockDomain(reset_less=False)
        self.cd_sys.clk = pmod0.pin4

        led = device.request('user_led')

        self.div = Signal(8, reset=1)
        self.sync += [
            # If(~pmod0.pin4,
                self.div.eq(self.div + 1)
            # )
        ]
        self.comb += [
            led.eq(self.div),

            spi_flash.pin1.eq(pmod0.pin4), # ~CS
            spi_flash.pin2.eq(1),          # VCC
            pmod0.pin3.eq(spi_flash.pin3), # DO
            spi_flash.pin4.eq(pmod0.pin2), # IO3

#            spi_flash.pin5.eq(pmod0.pin7), # IO2
            pmod0.pin7.eq(spi_flash.pin5), # IO2

            spi_flash.pin6.eq(pmod0.pin6), # CLK
            spi_flash.pin7.eq(0),          # GND
            spi_flash.pin8.eq(pmod0.pin8), # DI

            
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


    def build(self):
        self.device.build(self, toolchain_path='/usr/share/trellis')
