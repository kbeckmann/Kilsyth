from migen import *
import os, sys

from .. import KilsythApplet

class Blinky(KilsythApplet, name="blinky"):
    description = "blinks some LEDs"
    help = "Blinks some LEDs"

    def __init__(self, device, args):
        self.device = device

        led = device.request('user_led')

        self.div = Signal(23)
        self.sync += self.div.eq(self.div + 1)
        self.comb += led.eq(self.div[22])

    def testbench(self):
        assert (yield self.div[0]) == 0
        yield
        assert (yield self.div[0]) == 1
        yield
        assert (yield self.div[0]) == 0
        yield
        assert (yield self.div[0]) == 1
        yield

    # def test(self, device):
    #     led = device.request('user_led')
    #     blinky = Blinky(led)
    #     if len(sys.argv) == 2 and sys.argv[1] == "test":
    #         run_simulation(blinky, blinky.testbench(), vcd_name="out.vcd")
    #         print("Passed")
    #     else:
    #         device.build(blinky, toolchain_path='/usr/share/trellis')


# if __name__ == '__main__':
