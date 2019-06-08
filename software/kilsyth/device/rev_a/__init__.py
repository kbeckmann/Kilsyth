from migen.build.generic_platform import *
from migen.build.lattice import LatticePlatform
from .. import *

_io = [
    ("clk16", 0, Pins("G3"), IOStandard("LVCMOS33")),
    # user_led 0 is actually connected to WIDE:33, but it's N/C.
    # Place jumper between 33 and 31 to use user led 0
    ("user_led", 0, Pins(
        "WIDE:31",
        "WIDE:34",
        "WIDE:35",
        "WIDE:36",
        "WIDE:37",
        "WIDE:38",
        "WIDE:39",
        "WIDE:40",
    ), IOStandard("LVCMOS33")),

    ("ft600", 0,
        Subsignal("clk", Pins("H2")),
        Subsignal("data", Pins("P4 P3 P2 P1 N4 N3 N2 N1 M3 M1 L3 L2 L1 K4 K3 K2")),
        Subsignal("be", Pins("K1 J5")),
        Subsignal("rd_n", Pins("M4")),
        Subsignal("wr_n", Pins("J1")),
        Subsignal("gpio1", Pins("G5")),
        Subsignal("txe_n", Pins("J4")),
        Subsignal("rxf_n", Pins("J3")),
        Subsignal("oe_n", Pins("H1")),
    ),

    ("pmod0", 0, 
        Subsignal("pin1", Pins("PMOD0:1")),
        Subsignal("pin2", Pins("PMOD0:2")),
        Subsignal("pin3", Pins("PMOD0:3")),
        Subsignal("pin4", Pins("PMOD0:4")),
        Subsignal("pin5", Pins("PMOD0:7")),
        Subsignal("pin6", Pins("PMOD0:8")),
        Subsignal("pin7", Pins("PMOD0:9")),
        Subsignal("pin8", Pins("PMOD0:10")),
    ),

    ("pmod1", 0, 
        Subsignal("pin1", Pins("PMOD1:1")),
        Subsignal("pin2", Pins("PMOD1:2")),
        Subsignal("pin3", Pins("PMOD1:3")),
        Subsignal("pin4", Pins("PMOD1:4")),
        Subsignal("pin5", Pins("PMOD1:7")),
        Subsignal("pin6", Pins("PMOD1:8")),
        Subsignal("pin7", Pins("PMOD1:9")),
        Subsignal("pin8", Pins("PMOD1:10")),
    ),

    ("pmod2", 0, 
        Subsignal("pin1", Pins("PMOD2:1")),
        Subsignal("pin2", Pins("PMOD2:2")),
        Subsignal("pin3", Pins("PMOD2:3")),
        Subsignal("pin4", Pins("PMOD2:4")),
        Subsignal("pin5", Pins("PMOD2:7")),
        Subsignal("pin6", Pins("PMOD2:8")),
        Subsignal("pin7", Pins("PMOD2:9")),
        Subsignal("pin8", Pins("PMOD2:10")),
    ),

    ("wide", 0, Pins(
        " ".join(["WIDE:%d" % x for x in range(1, 30)])
    ), IOStandard("LVCMOS33")),

]

_connectors = [
    ("WIDE",
        "None",  # 0: No pin0
        # Bank 7
        "F3",    # 1
        "F2",
        "E2",
        "E1",
        "C1",
        "D1",
        "A2",
        "B1",
        "C2",
        "B2",    # 10
        "A3",
        "D2",
        "C3",
        "B3",
        "A4",
        "D3",
        "C4",
        "B4",
        "A5",
        "E4",    # 20
        "C5",
        "B5",
        "A6",
        "D5",
        # Bank 0
        "C6",    # 25
        "B6",
        "C7",
        "A7",
        "B8",
        "A8",    # 30
        "A9",    # 31: LED 0 if jumper is placed
        "C8",
        "None",  # 33: LED 0 (N/C)
        "B9",    # 34: LED 1
        "B10",   # 35: LED 2
        "A10",   # 36: LED 3
        "A11",   # 37: LED 4
        "C10",   # 38: LED 5
        "B11",   # 39: LED 6
        "C11",   # 40: LED 7
    ),
    ("PMOD0",
        "None",  # 0: N/C
        "A12",   # 1: PMOD1
        "D12",   # 2: PMOD2
        "A13",   # 3: PMOD3
        "D13",   # 4: PMOD4
        "None",  # 5: GND
        "None",  # 6: 3.3V
        "B12",   # 7: PMOD5
        "C12",   # 8: PMOD6
        "B13",   # 9: PMOD7
        "C13",   # 10: PMOD8
        "None",  # 11: GND
        "None",  # 12: 3.3v
    ),
    ("PMOD1",
        "None",  # 0: N/C
        "A14",   # 1: PMOD1
        "B15",   # 2: PMOD2
        "C15",   # 3: PMOD3
        "B16",   # 4: PMOD4
        "None",  # 5: GND
        "None",  # 6: 3.3V
        "C14",   # 7: PMOD5
        "D15",   # 8: PMOD6
        "A16",   # 9: PMOD7
        "C16",   # 10: PMOD8
        "None",  # 11: GND
        "None",  # 12: 3.3v
    ),
    ("PMOD2",
        "None",  # 0: N/C
        "A17",   # 1: PMOD1
        "C17",   # 2: PMOD2
        "B18",   # 3: PMOD3
        "B20",   # 4: PMOD4
        "None",  # 5: GND
        "None",  # 6: 3.3V
        "B17",   # 7: PMOD5
        "A18",   # 8: PMOD6
        "A19",   # 9: PMOD7
        "B19",   # 10: PMOD8
        "None",  # 11: GND
        "None",  # 12: 3.3v
    ),
]

class KilsythRevA(KilsythDevice, name=None):
    help = "Kilsyth RevA"
    description = "Kilsyth RevA"

    # Super must set this
    idcode = None
    device = None

    default_clk_name = "clk16"
    default_clk_period = 62.5

    def __init__(self, *args, **kwargs):
        LatticePlatform.__init__(self, self.device, _io, _connectors,
                                    toolchain='trellis', *args, **kwargs)

    def build(self, *args, **kwargs):
        KilsythDevice.build(self, idcode=self.idcode, *args, **kwargs)

class KilsythRevA12(KilsythRevA, name="rev_a_12"):
    help = "Kilsyth RevA LFE5U-12F"
    description = "Kilsyth RevA LFE5U-12F"
    idcode = "0x21111043"
    device = "LFE5U-25F-6BG381C"

class KilsythRevA25(KilsythRevA, name="rev_a_25"):
    help = "Kilsyth RevA LFE5U-25F"
    description = "Kilsyth RevA LFE5U-25F"
    idcode = "0x41111043"
    device = "LFE5U-25F-6BG381C"

class KilsythRevA45(KilsythRevA, name="rev_a_45"):
    help = "Kilsyth RevA LFE5U-45F"
    description = "Kilsyth RevA LFE5U-45F"
    idcode = "0x41112043"
    device = "LFE5U-45F-6BG381C"

class KilsythRevA85(KilsythRevA, name="rev_a_85"):
    help = "Kilsyth RevA LFE5U-85F"
    description = "Kilsyth RevA LFE5U-85F"
    idcode = "0x41113043"
    device = "LFE5U-85F-6BG381C"
