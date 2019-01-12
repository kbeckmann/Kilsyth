import ctypes
from ctypes import *

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


class FT600Driver():
    def __init__(self, *args, **kwargs):
        # self.lib = cdll.LoadLibrary(find_library('ftd3xx'))
        self.lib = cdll.LoadLibrary('../../software/ft600_test/linux-x86_64/libftd3xx.so')

        self.lib.FT_GetDriverVersion.argtypes = [c_void_p, POINTER(c_ulong)]
        self.lib.FT_GetDriverVersion.restype = c_ulong

        self.lib.FT_GetLibraryVersion.argtypes = [c_void_p]
        self.lib.FT_GetLibraryVersion.restype = c_ulong

        self.lib.FT_CreateDeviceInfoList.argtypes = [POINTER(c_ulong)]
        self.lib.FT_CreateDeviceInfoList.restype = c_ulong

        self.lib.FT_GetDeviceInfoList.argtypes = [POINTER(FT_DEVICE_LIST_INFO_NODE * 16), POINTER(c_ulong)]
        self.lib.FT_GetDeviceInfoList.restype = c_ulong





    def FT_GetDriverVersion(self):
        ret = c_ulong()
        self.lib.FT_GetDriverVersion(None, byref(ret))
        ret = ret.value
        return (
            (ret>>24) & 0xFF,
            (ret>>16) & 0xFF,
            ret & 0xFFFF
        )

    def FT_GetLibraryVersion(self):
        ret = c_ulong()
        self.lib.FT_GetDriverVersion(None, byref(ret))
        self.lib.FT_GetLibraryVersion(byref(ret))
        ret = ret.value
        return (
            (ret>>24) & 0xFF,
            (ret>>16) & 0xFF,
            ret & 0xFFFF
        )

    def get_device_lists(self):
        count = c_ulong()
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
            print("ftHandle:", node.ftHandle)
