from migen import *

class Blinky(Module):
    def __init__(self, led):
        self.div = Signal(23)
        self.sync += self.div.eq(self.div + 1)
        self.comb += led.eq(self.div[22])

if __name__ == '__main__':
    import kilsyth
    plat = kilsyth.Platform(toolchain='trellis')
    led = plat.request('user_led')
    blinky = Blinky(led)
    plat.build(blinky, toolchain_path='/usr/local/share/trellis', idcode="0x21111043")
