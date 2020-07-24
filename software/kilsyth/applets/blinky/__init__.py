from nmigen import *

from .. import Applet


class Blinky(Elaboratable):
    def __init__(self, led, timer_width=24):
        self.led = led
        self.timer = Signal(timer_width)

    def elaborate(self, platform):
        m = Module()

        m.d.sync += self.timer.eq(self.timer + 1)
        m.d.comb += self.led.eq(self.timer[-1])

        return m

class BlinkyApplet(Applet, applet_name="blinky"):
    description = "Blinks some LEDs"
    help = "Blinks some LEDs"

    def __init__(self, args):
        pass

    def elaborate(self, platform):
        led = platform.request("led", 0)

        m = Module()

        m.submodules.blinky = Blinky(led.o)

        return m
