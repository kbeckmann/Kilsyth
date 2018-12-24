from migen import *
import sys

class Blinky(Module):
    def __init__(self, led):
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

if __name__ == '__main__':
    import kilsyth
    plat = kilsyth.Platform(toolchain='trellis')
    led = plat.request('user_led')
    blinky = Blinky(led)
    if len(sys.argv) == 2 and sys.argv[1] == "test":
        run_simulation(blinky, blinky.testbench(), vcd_name="out.vcd")
        print("Passed")
    else:
        plat.build(blinky, toolchain_path='/usr/local/share/trellis', idcode="0x21111043")
