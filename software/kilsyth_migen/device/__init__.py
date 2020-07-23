from migen.build.lattice import LatticePlatform

class KilsythDevice(LatticePlatform):
    all = {}

    def __init_subclass__(cls, name, **kwargs):
        super().__init_subclass__(**kwargs)

        if name == None:
            return

        if name in cls.all:
            raise ValueError("Device {!r} already exists".format(name))

        cls.all[name] = cls
        cls.name = name

    help = "device help missing"
    description = "device description missing"

from . import rev_a
