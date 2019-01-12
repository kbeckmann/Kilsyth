import ctypes
from ctypes import *

CONFIGURATION_FIFO_CLK_100 = 0
CONFIGURATION_FIFO_CLK_66  = 1
CONFIGURATION_FIFO_CLK_50  = 2
CONFIGURATION_FIFO_CLK_40  = 3

FT_OPEN_BY_SERIAL_NUMBER = 0x00000001
FT_OPEN_BY_DESCRIPTION   = 0x00000002
FT_OPEN_BY_LOCATION      = 0x00000004
FT_OPEN_BY_GUID          = 0x00000008
FT_OPEN_BY_INDEX         = 0x00000010

FT_DEVICE_UNKNOWN = 3
FT_DEVICE_600 = 600
FT_DEVICE_601 = 601
FT_DEVICE_602 = 602
FT_DEVICE_603 = 603


class FT_DEVICE_LIST_INFO_NODE(Structure):
    _fields_ = [
        ("Flags", c_uint),
        ("Type", c_uint),
        ("ID", c_uint),
        ("LocId", c_uint),
        ("SerialNumber", c_char * 32),
        ("Description", c_char * 32),
        ("ftHandle", c_void_p),
    ]

class FT_60XCONFIGURATION(Structure):
    _fields_ = [
        # Device Descriptor
        ("VendorID", c_ushort),
        ("ProductID", c_ushort),
        # String Descriptors
        ("StringDescriptors", c_char * 128),
        # Configuration Descriptor
        ("Reserved1", c_char),
        ("PowerAttributes", c_char),
        ("PowerConsumption", c_short),
        # Data Transfer Configuration
        ("Reserved2", c_char),
        ("FIFOClock", c_char),
        ("FIFOMode", c_char),
        ("ChannelConfig", c_char),
        # Optional Feature Support
        ("OptionalFeatureSupport", c_short),
        ("BatteryChargingGPIOConfig", c_char),
        ("FlashEEPROMDetection", c_char), # Read-only
        # MSIO and GPIO Configuration
        ("MSIO_Control", c_uint),
        ("GPIO_Control", c_uint),
    ]


class FT600Driver():
    def __init__(self, *args, **kwargs):
        # self.lib = cdll.LoadLibrary(find_library('ftd3xx'))
        self.lib = cdll.LoadLibrary('../../software/ft600_test/linux-x86_64/libftd3xx.so')

        self.lib.FT_GetDriverVersion.argtypes = [c_void_p, POINTER(c_uint)]
        self.lib.FT_GetDriverVersion.restype = c_uint

        self.lib.FT_GetLibraryVersion.argtypes = [c_void_p]
        self.lib.FT_GetLibraryVersion.restype = c_uint

        self.lib.FT_CreateDeviceInfoList.argtypes = [POINTER(c_uint)]
        self.lib.FT_CreateDeviceInfoList.restype = c_uint

        self.lib.FT_GetDeviceInfoList.argtypes = [POINTER(FT_DEVICE_LIST_INFO_NODE * 16), POINTER(c_uint)]
        self.lib.FT_GetDeviceInfoList.restype = c_uint

        self.lib.FT_Create.argtypes = [c_void_p, c_uint, POINTER(c_void_p)]
        self.lib.FT_Create.restype = c_uint

        self.lib.FT_Close.argtypes = [c_void_p]
        self.lib.FT_Close.restype = c_uint

        self.lib.FT_GetDeviceInfoDetail.argtypes = [c_uint, POINTER(c_uint), POINTER(c_uint), POINTER(c_uint), POINTER(c_uint), c_void_p, c_void_p, c_void_p]
        self.lib.FT_GetDeviceInfoDetail.restype = c_uint





    def FT_GetDriverVersion(self):
        ret = c_uint()
        self.lib.FT_GetDriverVersion(None, byref(ret))
        ret = ret.value
        return (
            (ret>>24) & 0xFF,
            (ret>>16) & 0xFF,
            ret & 0xFFFF
        )

    def FT_GetLibraryVersion(self):
        ret = c_uint()
        self.lib.FT_GetDriverVersion(None, byref(ret))
        self.lib.FT_GetLibraryVersion(byref(ret))
        ret = ret.value
        return (
            (ret>>24) & 0xFF,
            (ret>>16) & 0xFF,
            ret & 0xFFFF
        )

    def get_device_lists(self):
        count = c_uint()
        if self.lib.FT_CreateDeviceInfoList(byref(count)) != 0:
            raise Exception()
        if count.value != 1:
            raise Exception("Only one device must be connected!")
        
        nodes = (FT_DEVICE_LIST_INFO_NODE * 16)()
        if self.lib.FT_GetDeviceInfoList(nodes, byref(count)) != 0:
            raise Exception()

        print("Found %d device(s)." % count.value)
        for i in range(count.value):
            node = nodes[i]
            print("Flags: 0x%08lx" % node.Flags)
            print("Type:  0x%08lx" % node.Type)
            print("ID:    0x%08lx" % node.ID)
            print("LocId: 0x%08lx" % node.LocId)
            print("SerialNumber: %s" % node.SerialNumber)
            print("Description: %s" % node.Description)
        return nodes

    def set_channel_config(self, is_600_mode, clock):
        dwType = c_uint()
        handle = c_void_p()

        if self.lib.FT_Create(0, FT_OPEN_BY_INDEX, byref(handle)) != 0:
            raise Exception()

        if self.lib.FT_GetDeviceInfoDetail(0, None, byref(dwType), None, None, None, None, None) != 0:
            raise Exception()
        
        if dwType.value != FT_DEVICE_600 and dwType != FT_DEVICE_601:
            raise Exception("Unsupported hardware")

        self.lib.FT_Close(handle)
