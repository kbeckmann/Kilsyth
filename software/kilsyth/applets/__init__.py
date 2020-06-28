# This is based on https://github.com/whitequark/Glasgow/blob/master/software/glasgow/applet/__init__.py
from migen import *

class KilsythApplet(Module):
    all = {}

    # Applet may override these and add arguments to the parser
    @classmethod
    def add_build_arguments(cls, parser):
        pass

    @classmethod
    def add_run_arguments(cls, parser):
        pass

    @classmethod
    def add_test_arguments(cls, parser):
        pass

    def __init_subclass__(cls, name, **kwargs):
        super().__init_subclass__(**kwargs)

        if name in cls.all:
            raise ValueError("Applet {!r} already exists".format(name))

        cls.all[name] = cls
        cls.name = name

    help = "applet help missing"
    description = "applet description missing"

    def build(self):
        self.device.build(self, toolchain_path='/usr/share/trellis')

    async def run(self):
        pass

from . import blinky
from . import ft600_demo
from . import la
from . import spi_flash_mitm
from . import spi_slave_demo
from . import sx1257
