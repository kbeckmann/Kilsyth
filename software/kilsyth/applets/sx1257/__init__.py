from migen import *
import os, sys

from .. import KilsythApplet

class SX1257(KilsythApplet, name="sx1257"):
    description = "SX1257 PMOD integration"
    help = "CQ CQ, MF"

    def __init__(self, device):
        self.device = device
        pmod0 = device.request('pmod0')

        self.clock_domains.cd_por = ClockDomain()
        self.clock_domains.cd_sys = ClockDomain(reset_less=False)
        self.cd_sys.clk = pmod0.pin5

        led = device.request('user_led')

        self.div = Signal(32)
        self.sync += self.div.eq(self.div + 1)

        self.counter = Signal(32, reset=2**24)

        # Sigma-delta modulator
        SD_Bits = 8
        SD_In = Signal(SD_Bits)
        SD_Out = Signal()
        SD_Acc = Signal(SD_Bits + 1)
        self.sync += SD_Acc.eq(SD_Acc[0:SD_Bits] + SD_In)
        self.comb += SD_Out.eq(SD_Acc[SD_Bits])
        # ---------


        # LFSR
        self.degree = 32
        # self.taps   = (32, 23, 13, 11, 7) # Creates actual noise
        self.taps   = (13, 7) # Creates a nice repeatable pattern
        self.lfsr_value = Signal(self.degree, reset=1)
        feedback = 1
        for tap in self.taps:
            feedback ^= self.lfsr_value[tap - 1]
        # self.sync += self.lfsr_value.eq((self.lfsr_value << 1) | feedback)
        self.sync += self.lfsr_value.eq((self.lfsr_value << 1) | feedback)
        # ----


        self.submodules.fsm = FSM(reset_state="INIT")
        self.fsm.act(
            "INIT",
            NextValue(led, 1),
            NextValue(pmod0.pin6, 0),
            NextValue(pmod0.pin7, 0),
            # NextValue(SD_In, self.div >> 20), # As close to silence as possible
            # NextValue(SD_In, SD_In + 1),
            NextValue(SD_In, self.lfsr_value[0:8]),
            # NextValue(SD_In, SD_In + self.div[12:12+5]),
            # NextValue(SD_In, self.div[2] * 68),
            NextValue(self.counter, 2**8),
            # NextValue(self.counter, 2**8),
            # If(self.div[22],
                NextState("FOO")
            # )
        )

        self.fsm.act(
            "FOO",
            NextValue(self.counter, self.counter - 1),
            NextValue(led, 2),
            NextValue(pmod0.pin6, SD_Out),
            NextValue(pmod0.pin7, SD_Out),
            If(
                self.counter == 0,
                NextState("INIT")
            )
        )


    def build(self):
        self.device.build(self, toolchain_path='/usr/share/trellis')

