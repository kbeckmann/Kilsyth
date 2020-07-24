import os
import subprocess

from nmigen.build import *
from nmigen.vendor.lattice_ecp5 import *
from nmigen_boards.resources import *

from ..gateware.ft600 import FT600Resource

__all__ = ["KilsythPlatform"]


class KilsythPlatform(LatticeECP5Platform):
    device      = "LFE5U-45F"
    package     = "BG381"
    speed       = 6

    default_clk = "clk16"
    resources   = [
        Resource("clk16", 0, Pins("G3", dir="i"),
                 Clock(16e6), Attrs(GLOBAL=True, IO_TYPE="LVCMOS33")),

        *LEDResources(pins="A9 B9 B10 A10 A11 C10 B11 C11", invert=False, attrs=Attrs(IO_TYPE="LVCMOS33")),

        FT600Resource(0,
            clk="H2",
            data="P4 P3 P2 P1 N4 N3 N2 N1 M3 M1 L3 L2 L1 K4 K3 K2",
            be="K1 J5",
            rd_n="M4",
            wr_n="J1",
            gpio1="G5",
            txe_n="J4",
            rxf_n="J3",
            oe_n="H1",
        )
    ]
    connectors = []

    def toolchain_program(self, products, name):
        openocd = os.environ.get("OPENOCD", "openocd")
        interface = os.environ.get("INTERFACE", "SiPEED")
        if interface == "SiPEED" or interface == "busblaster":
            if interface == "SiPEED":
                args = ["-c", """
                        interface ftdi
                        ftdi_vid_pid 0x0403 0x6010
                        ftdi_layout_init 0x0018 0x05fb
                        ftdi_layout_signal nSRST -data 0x0010
                    """]
            elif interface == "busblaster":
                args = ["-f", "interface/ftdi/dp_busblaster.cfg"]

            with products.extract("{}.svf".format(name)) as vector_filename:
                subprocess.check_call([openocd,
                    *args,
                    "-c", "transport select jtag; adapter_khz 10000; init; svf -quiet {}; exit".format(vector_filename)
                ])
        else:
            raise Exception("Unsupported interface")
