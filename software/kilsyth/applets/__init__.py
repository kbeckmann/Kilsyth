# This is based on https://github.com/whitequark/Glasgow/blob/master/software/glasgow/applet/__init__.py
from migen import *

class KilsythApplet(Module):
    all = {}

    def __init_subclass__(cls, name, **kwargs):
        super().__init_subclass__(**kwargs)

        if name in cls.all:
            raise ValueError("Applet {!r} already exists".format(name))

        cls.all[name] = cls
        cls.name = name

    help = "applet help missing"
    description = "applet description missing"

    def build(self, device):
        raise NotImplementedError

from . import blinky
from . import spi_flash_mitm
from . import sx1257
