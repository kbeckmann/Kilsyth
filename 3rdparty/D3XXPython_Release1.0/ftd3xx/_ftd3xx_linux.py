import sys
from ctypes import *
from defines import *


STRING = c_char_p
DWORD = c_int
ULONG = c_ulong
WORD = c_ushort
BYTE = c_ubyte
BOOL = c_bool
BOOLEAN = c_char
LPCSTR = STRING
HANDLE = c_void_p
LONG = c_long
UINT = c_uint
LPSTR = STRING

_libname = 'libftd3xx.so'
_libraries = {}
_libraries[_libname] = CDLL(_libname)

USHORT = c_ushort
SHORT = c_short
UCHAR = c_ubyte
WCHAR = c_wchar
LPBYTE = POINTER(c_ubyte)
CHAR = c_char
LPBOOL = POINTER(c_int)
PUCHAR = POINTER(c_ubyte)
PCHAR = STRING
PVOID = c_void_p
INT = c_int
LPTSTR = STRING
LPDWORD = POINTER(DWORD)
LPWORD = POINTER(WORD)
PULONG = POINTER(ULONG)
LPVOID = PVOID
VOID = None
ULONGLONG = c_ulonglong
FT_HANDLE = PVOID
FT_STATUS = ULONG
FT_DEVICE = ULONG



FT_ListDevices = _libraries[_libname].FT_ListDevices
FT_ListDevices.restype = FT_STATUS
# FT_ListDevices(pArg1, pArg2, Flags)
FT_ListDevices.argtypes = [PVOID, PVOID, DWORD]
FT_ListDevices.__doc__ = \
"""FT_STATUS FT_ListDevices(PVOID pArg1, PVOID pArg2, DWORD Flags)"""

class _FT_DEVICE_LIST_INFO_NODE(Structure):
    pass
_FT_DEVICE_LIST_INFO_NODE._fields_ = [
    ('Flags', ULONG),
    ('Type', ULONG),
    ('ID', ULONG),
    ('LocId', DWORD),
    ('SerialNumber', c_char * 16),
    ('Description', c_char * 32),
    ('ftHandle', FT_HANDLE),
]
FT_DEVICE_LIST_INFO_NODE = _FT_DEVICE_LIST_INFO_NODE
PFT_DEVICE_LIST_INFO_NODE = POINTER(_FT_DEVICE_LIST_INFO_NODE)

FT_CreateDeviceInfoList = _libraries[_libname].FT_CreateDeviceInfoList
FT_CreateDeviceInfoList.restype = FT_STATUS
# FT_CreateDeviceInfoList(lpdwNumDevs)
FT_CreateDeviceInfoList.argtypes = [LPDWORD]
FT_CreateDeviceInfoList.__doc__ = \
"""FT_STATUS FT_CreateDeviceInfoList(LPDWORD lpdwNumDevs)"""

FT_GetDeviceInfoList = _libraries[_libname].FT_GetDeviceInfoList
FT_GetDeviceInfoList.restype = FT_STATUS
# FT_GetDeviceInfoList(pDest, lpdwNumDevs)
FT_GetDeviceInfoList.argtypes = [PFT_DEVICE_LIST_INFO_NODE, LPDWORD]
FT_GetDeviceInfoList.__doc__ = \
"""FT_STATUS FT_GetDeviceInfoList(FT_DEVICE_LIST_INFO_NODE* pDest, LPDWORD lpdwNumDevs)"""

FT_GetDeviceInfoDetail = _libraries[_libname].FT_GetDeviceInfoDetail
FT_GetDeviceInfoDetail.restype = FT_STATUS
# FT_GetDeviceInfoDetail(dwIndex, lpdwFlags, lpdwType, lpdwID, lpdwLocId, lpSerialNumber, lpDescription, pftHandle)
FT_GetDeviceInfoDetail.argtypes = [DWORD, LPDWORD, LPDWORD, LPDWORD, LPDWORD, LPVOID, LPVOID, POINTER(FT_HANDLE)]
FT_GetDeviceInfoDetail.__doc__ = \
"""FT_STATUS FT_GetDeviceInfoDetail(DWORD dwIndex, LPDWORD lpdwFlags, LPDWORD lpdwType, LPDWORD lpdwID, LPDWORD lpdwLocId, LPVOID lpSerialNumber, LPVOID lpDescription, FT_HANDLE * pftHandle)"""

FT_Create = _libraries[_libname].FT_Create
FT_Create.restype = FT_STATUS
# FT_Create(pArg1, Flags, pHandle)
FT_Create.argtypes = [PVOID, DWORD, POINTER(FT_HANDLE)]
FT_Create.__doc__ = \
"""FT_STATUS FT_Create(PVOID pArg1, DWORD Flags, FT_HANDLE * pHandle)"""

FT_Close = _libraries[_libname].FT_Close
FT_Close.restype = FT_STATUS
# FT_Close(ftHandle)
FT_Close.argtypes = [FT_HANDLE]
FT_Close.__doc__ = \
"""FT_STATUS FT_Close(FT_HANDLE ftHandle)"""

FT_FlushPipe = _libraries[_libname].FT_FlushPipe
FT_FlushPipe.restype = FT_STATUS
# FT_FlushPipe(ftHandle, ucPipeID)
FT_FlushPipe.argtypes = [FT_HANDLE, UCHAR]
FT_FlushPipe.__doc__ = \
"""FT_STATUS FT_FlushPipe(FT_HANDLE ftHandle, UCHAR ucPipeID)"""

FT_GetVIDPID = _libraries[_libname].FT_GetVIDPID
FT_GetVIDPID.restype = FT_STATUS
# FT_GetVIDPID(ftHandle, puwVID, puwPID)
FT_GetVIDPID.argtypes = [FT_HANDLE, POINTER(USHORT), POINTER(USHORT)]
FT_GetVIDPID.__doc__ = \
"""FT_STATUS FT_GetVIDPID(FT_HANDLE ftHandle, PUSHORT puwVID, PUSHORT puwPID)"""

FT_GetLibraryVersion = _libraries[_libname].FT_GetLibraryVersion
FT_GetLibraryVersion.restype = FT_STATUS
# FT_GetLibraryVersion(lpdwVersion)
FT_GetLibraryVersion.argtypes = [LPDWORD]
FT_GetLibraryVersion.__doc__ = \
"""FT_STATUS FT_GetLibraryVersion(LPDWORD lpdwVersion)"""

FT_GetDriverVersion = _libraries[_libname].FT_GetDriverVersion
FT_GetDriverVersion.restype = FT_STATUS
# FT_GetDriverVersion(ftHandle, lpdwVersion)
FT_GetDriverVersion.argtypes = [FT_HANDLE, LPDWORD]
FT_GetDriverVersion.__doc__ = \
"""FT_STATUS FT_GetDriverVersion(FT_HANDLE ftHandle, LPDWORD lpdwVersion)"""

FT_GetFirmwareVersion = _libraries[_libname].FT_GetFirmwareVersion
FT_GetFirmwareVersion.restype = FT_STATUS
# FT_GetFirmwareVersion(ftHandle, lpdwVersion)
FT_GetFirmwareVersion.argtypes = [FT_HANDLE, LPDWORD]
FT_GetFirmwareVersion.__doc__ = \
"""FT_STATUS FT_GetFirmwareVersion(FT_HANDLE ftHandle, LPDWORD lpdwVersion)"""

class _FT_DEVICE_DESCRIPTOR(Structure):
    pass
_FT_DEVICE_DESCRIPTOR._fields_ = [
    ('bLength', UCHAR),
    ('bDescriptorType', UCHAR),
    ('bcdUSB', USHORT),
    ('bDeviceClass', UCHAR),
    ('bDeviceSubClass', UCHAR),
    ('bDeviceProtocol', UCHAR),
    ('bMaxPacketSize0', UCHAR),
    ('idVendor', USHORT),
    ('idProduct', USHORT),
    ('bcdDevice', USHORT),
    ('iManufacturer', UCHAR),
    ('iProduct', UCHAR),
    ('iSerialNumber', UCHAR),
    ('bNumConfigurations', UCHAR),
]
FT_DEVICE_DESCRIPTOR = _FT_DEVICE_DESCRIPTOR
PFT_DEVICE_DESCRIPTOR = POINTER(_FT_DEVICE_DESCRIPTOR)

FT_GetDeviceDescriptor = _libraries[_libname].FT_GetDeviceDescriptor
FT_GetDeviceDescriptor.restype = FT_STATUS
# FT_GetDeviceDescriptor(ftHandle, ptDescriptor)
FT_GetDeviceDescriptor.argtypes = [FT_HANDLE, PFT_DEVICE_DESCRIPTOR]
FT_GetDeviceDescriptor.__doc__ = \
"""FT_STATUS FT_GetDeviceDescriptor(FT_HANDLE ftHandle, PFT_DEVICE_DESCRIPTOR ptDescriptor)"""

class _FT_CONFIGURATION_DESCRIPTOR(Structure):
    pass
_FT_CONFIGURATION_DESCRIPTOR._fields_ = [
    ('bLength', UCHAR),
    ('bDescriptorType', UCHAR),
    ('wTotalLength', USHORT),
    ('bNumInterfaces', UCHAR),
    ('bConfigurationValue', UCHAR),
    ('iConfiguration', UCHAR),
    ('bmAttributes', UCHAR),
    ('MaxPower', UCHAR),
]
FT_CONFIGURATION_DESCRIPTOR = _FT_CONFIGURATION_DESCRIPTOR
PFT_CONFIGURATION_DESCRIPTOR = POINTER(_FT_CONFIGURATION_DESCRIPTOR)

FT_GetConfigurationDescriptor = _libraries[_libname].FT_GetConfigurationDescriptor
FT_GetConfigurationDescriptor.restype = FT_STATUS
# FT_GetConfigurationDescriptor(ftHandle, ptDescriptor)
FT_GetConfigurationDescriptor.argtypes = [FT_HANDLE, PFT_CONFIGURATION_DESCRIPTOR]
FT_GetConfigurationDescriptor.__doc__ = \
"""FT_STATUS FT_GetConfigurationDescriptor(FT_HANDLE ftHandle, PFT_CONFIGURATION_DESCRIPTOR ptDescriptor)"""

class _FT_INTERFACE_DESCRIPTOR(Structure):
    pass
_FT_INTERFACE_DESCRIPTOR._fields_ = [
    ('bLength', UCHAR),
    ('bDescriptorType', UCHAR),
    ('bInterfaceNumber', UCHAR),
    ('bAlternateSetting', UCHAR),
    ('bNumEndpoints', UCHAR),
    ('bInterfaceClass', UCHAR),
    ('bInterfaceSubClass', UCHAR),
    ('bInterfaceProtocol', UCHAR),
    ('iInterface', UCHAR),
]
FT_INTERFACE_DESCRIPTOR = _FT_INTERFACE_DESCRIPTOR
PFT_INTERFACE_DESCRIPTOR = POINTER(_FT_INTERFACE_DESCRIPTOR)

FT_GetInterfaceDescriptor = _libraries[_libname].FT_GetInterfaceDescriptor
FT_GetInterfaceDescriptor.restype = FT_STATUS
# FT_GetInterfaceDescriptor(ftHandle, ucInterfaceIndex, ptDescriptor)
FT_GetInterfaceDescriptor.argtypes = [FT_HANDLE, UCHAR, PFT_INTERFACE_DESCRIPTOR]
FT_GetInterfaceDescriptor.__doc__ = \
"""FT_STATUS FT_GetInterfaceDescriptor(FT_HANDLE ftHandle, UCHAR ucInterfaceIndex, PFT_INTERFACE_DESCRIPTOR ptDescriptor)"""

class _FT_STRING_DESCRIPTOR(Structure):
    pass
_FT_STRING_DESCRIPTOR._fields_ = [
    ('bLength', UCHAR),
    ('bDescriptorType', UCHAR),
    ('szString', WCHAR * 256),
]
FT_STRING_DESCRIPTOR = _FT_STRING_DESCRIPTOR
PFT_STRING_DESCRIPTOR = POINTER(_FT_STRING_DESCRIPTOR)

FT_GetDescriptor = _libraries[_libname].FT_GetDescriptor
FT_GetDescriptor.restype = FT_STATUS
# FT_GetDescriptor(ftHandle, ucDescriptorType, ucIndex, pucBuffer, ulBufferLength, pulLengthTransferred)
FT_GetDescriptor.argtypes = [FT_HANDLE, UCHAR, UCHAR, PFT_STRING_DESCRIPTOR, ULONG, PULONG]
FT_GetDescriptor.__doc__ = \
"""FT_STATUS FT_GetDescriptor(FT_HANDLE ftHandle, UCHAR ucDescriptorType, UCHAR ucIndex, PFT_STRING_DESCRIPTOR pucBuffer, ULONG ulBufferLength, PULONG pulLengthTransferred)"""

class _FT_PIPE_INFORMATION(Structure):
    pass
_FT_PIPE_INFORMATION._fields_ = [
    ('PipeType', ULONG),
    ('PipeId', UCHAR),
    ('MaximumPacketSize', USHORT),
    ('Interval', UCHAR),
]
FT_PIPE_INFORMATION = _FT_PIPE_INFORMATION
PFT_PIPE_INFORMATION = POINTER(_FT_PIPE_INFORMATION)

FT_GetPipeInformation = _libraries[_libname].FT_GetPipeInformation
FT_GetPipeInformation.restype = FT_STATUS
# FT_GetPipeInformation(ftHandle, ucInterfaceIndex, ucPipeIndex, ptPipeInformation)
FT_GetPipeInformation.argtypes = [FT_HANDLE, UCHAR, UCHAR, PFT_PIPE_INFORMATION]
FT_GetPipeInformation.__doc__ = \
"""FT_STATUS FT_GetPipeInformation(FT_HANDLE ftHandle, UCHAR ucInterfaceIndex, UCHAR ucPipeIndex, PFT_PIPE_INFORMATION ptPipeInformation)"""

class _FT_SETUP_PACKET(Structure):
    pass
_FT_SETUP_PACKET._fields_ = [
    ('RequestType', UCHAR),
    ('Request', UCHAR),
    ('Value', USHORT),	
    ('Index', USHORT),
    ('Length', USHORT),
]
FT_SETUP_PACKET = _FT_SETUP_PACKET
PFT_SETUP_PACKET = POINTER(_FT_SETUP_PACKET)

FT_ControlTransfer = _libraries[_libname].FT_ControlTransfer
FT_ControlTransfer.restype = FT_STATUS
# FT_ControlTransfer(ftHandle, tSetupPacket, pucBuffer, ulBufferLength, pulLengthTransferred)
FT_ControlTransfer.argtypes = [FT_HANDLE, FT_SETUP_PACKET, PUCHAR, ULONG, PULONG]
FT_ControlTransfer.__doc__ = \
"""FT_STATUS FT_ControlTransfer(FT_HANDLE ftHandle, FT_SETUP_PACKET tSetupPacket, PUCHAR pucBuffer, ULONG ulBufferLength, PULONG pulLengthTransferred)"""

class _FT_60XCONFIGURATION(Structure):
    pass
_FT_60XCONFIGURATION._fields_ = [
    ('VendorID', USHORT),
	('ProductID', USHORT),
	('StringDescriptors', UCHAR * 128),	
    ('bInterval', UCHAR),
    ('PowerAttributes', UCHAR),
    ('PowerConsumption', USHORT),
    ('Reserved2', UCHAR),
    ('FIFOClock', UCHAR),
    ('FIFOMode', UCHAR),
    ('ChannelConfig', UCHAR),
    ('OptionalFeatureSupport', USHORT),
    ('BatteryChargingGPIOConfig', UCHAR),
    ('FlashEEPROMDetection', UCHAR),	
    ('MSIO_Control', ULONG),
    ('GPIO_Control', ULONG),
]
FT_60XCONFIGURATION = _FT_60XCONFIGURATION
PFT_60XCONFIGURATION = POINTER(_FT_60XCONFIGURATION)

FT_GetChipConfiguration = _libraries[_libname].FT_GetChipConfiguration
FT_GetChipConfiguration.restype = FT_STATUS
# FT_GetChipConfiguration(ftHandle, pvConfiguration)
FT_GetChipConfiguration.argtypes = [FT_HANDLE, PFT_60XCONFIGURATION]
FT_GetChipConfiguration.__doc__ = \
"""FT_STATUS FT_GetChipConfiguration(FT_HANDLE ftHandle, PVOID pvConfiguration)"""

FT_SetChipConfiguration = _libraries[_libname].FT_SetChipConfiguration
FT_SetChipConfiguration.restype = FT_STATUS
# FT_SetChipConfiguration(ftHandle, pvConfiguration)
FT_SetChipConfiguration.argtypes = [FT_HANDLE, PFT_60XCONFIGURATION]
FT_SetChipConfiguration.__doc__ = \
"""FT_STATUS FT_SetChipConfiguration(FT_HANDLE ftHandle, PVOID pvConfiguration)"""

FT_ResetDevicePort = _libraries[_libname].FT_ResetDevicePort
FT_ResetDevicePort.restype = FT_STATUS
# FT_ResetDevicePort(ftHandle)
FT_ResetDevicePort.argtypes = [FT_HANDLE]
FT_ResetDevicePort.__doc__ = \
"""FT_STATUS FT_ResetDevicePort(FT_HANDLE ftHandle)"""

FT_EnableGPIO = _libraries[_libname].FT_EnableGPIO
FT_EnableGPIO.restype = FT_STATUS
# FT_EnableGPIO(ftHandle, u32Mask, u32Dir)
FT_EnableGPIO.argtypes = [FT_HANDLE, ULONG, ULONG]
FT_EnableGPIO.__doc__ = \
"""FT_STATUS FT_EnableGPIO(FT_HANDLE ftHandle, ULONG u32Mask, ULONG u32Dir)"""

FT_WriteGPIO = _libraries[_libname].FT_WriteGPIO
FT_WriteGPIO.restype = FT_STATUS
# FT_WriteGPIO(ftHandle, u32Mask, u32Data)
FT_WriteGPIO.argtypes = [FT_HANDLE, ULONG, ULONG]
FT_WriteGPIO.__doc__ = \
"""FT_STATUS FT_WriteGPIO(FT_HANDLE ftHandle, ULONG u32Mask, ULONG u32Data)"""

FT_ReadGPIO = _libraries[_libname].FT_ReadGPIO
FT_ReadGPIO.restype = FT_STATUS
# FT_ReadGPIO(ftHandle, pu32Data)
FT_ReadGPIO.argtypes = [FT_HANDLE, PULONG]
FT_ReadGPIO.__doc__ = \
"""FT_STATUS FT_ReadGPIO(FT_HANDLE ftHandle, PULONG pu32Data)"""

FT_SetGPIOPull = _libraries[_libname].FT_SetGPIOPull
FT_SetGPIOPull.restype = FT_STATUS
# FT_SetGPIOPull(ftHandle, u32Mask, u32Pull)
FT_SetGPIOPull.argtypes = [FT_HANDLE, ULONG, ULONG]
FT_SetGPIOPull.__doc__ = \
"""FT_STATUS FT_SetGPIOPull(FT_HANDLE ftHandle, ULONG u32Mask, ULONG u32Pull)"""

class _FT_PIPE_TRANSFER_CONF(Structure):
    pass
_FT_PIPE_TRANSFER_CONF._fields_ = [
    ('fPipeNotUsed', BOOL),
    ('fNonThreadSafeTransfer', BOOL),
    ('bURBCount', BYTE),
    ('wURBBufferCount', WORD),
    ('dwURBBufferSize', DWORD),
    ('dwStreamingSize', DWORD),
]
FT_PIPE_TRANSFER_CONF = _FT_PIPE_TRANSFER_CONF
PFT_PIPE_TRANSFER_CONF = POINTER(_FT_PIPE_TRANSFER_CONF)

class _FT_TRANSFER_CONF(Structure):
    pass
_FT_TRANSFER_CONF._fields_ = [
    ('wStructSize', WORD),
    ('pipe', FT_PIPE_TRANSFER_CONF * 2),
    ('fStopReadingOnURBUnderrun', BOOL),	
    ('fReserved1', BOOL),
    ('fKeepDeviceSideBufferAfterReopen', BOOL),
]
FT_TRANSFER_CONF = _FT_TRANSFER_CONF
PFT_TRANSFER_CONF = POINTER(_FT_TRANSFER_CONF)

FT_SetTransferParams = _libraries[_libname].FT_SetTransferParams
FT_SetTransferParams.restype = FT_STATUS
# FT_SetTransferParams(pConf, dwFifoID)
FT_SetTransferParams.argtypes = [PFT_TRANSFER_CONF, DWORD]
FT_SetTransferParams.__doc__ = \
"""FT_STATUS FT_SetTransferParams(FT_TRANSFER_CONF *pConf, DWORD dwFifoID)"""

FT_WritePipeEx = _libraries[_libname].FT_WritePipeEx
FT_WritePipeEx.restype = FT_STATUS
# FT_WritePipeEx(ftHandle, ucFifoID, pucBuffer, ulBufferLength, pulBytesTransferred, dwTimeoutInMs)
FT_WritePipeEx.argtypes = [FT_HANDLE, UCHAR, LPVOID, ULONG, PULONG, ULONG]
FT_WritePipeEx.__doc__ = \
"""FT_STATUS FT_WritePipeEx(FT_HANDLE ftHandle, UCHAR ucFifoID, LPVOID pucBuffer, ULONG ulBufferLength, PULONG pulBytesTransferred, DWORD dwTimeoutInMs)"""

FT_ReadPipeEx = _libraries[_libname].FT_ReadPipeEx
FT_ReadPipeEx.restype = FT_STATUS
# FT_ReadPipeEx(ftHandle, ucFifoID, pucBuffer, ulBufferLength, pulBytesTransferred, dwTimeoutInMs)
FT_ReadPipeEx.argtypes = [FT_HANDLE, UCHAR, LPVOID, ULONG, PULONG, ULONG]
FT_ReadPipeEx.__doc__ = \
"""FT_STATUS FT_ReadPipeEx(FT_HANDLE ftHandle, UCHAR ucFifoID, LPVOID pucBuffer, ULONG ulBufferLength, PULONG pulBytesTransferred, DWORD dwTimeoutInMs)"""

FT_GetReadQueueStatus = _libraries[_libname].FT_GetReadQueueStatus
FT_GetReadQueueStatus.restype = FT_STATUS
# FT_GetReadQueueStatus(ftHandle, ucFifoID, lpdwAmountInQueue)
FT_GetReadQueueStatus.argtypes = [FT_HANDLE, UCHAR, PULONG]
FT_GetReadQueueStatus.__doc__ = \
"""FT_STATUS FT_GetReadQueueStatus(FT_HANDLE ftHandle, UCHAR ucFifoID, LPDWORD lpdwAmountInQueue)"""

FT_GetWriteQueueStatus = _libraries[_libname].FT_GetWriteQueueStatus
FT_GetWriteQueueStatus.restype = FT_STATUS
# FT_GetWriteQueueStatus(ftHandle, ucFifoID, lpdwAmountInQueue)
FT_GetWriteQueueStatus.argtypes = [FT_HANDLE, UCHAR, PULONG]
FT_GetWriteQueueStatus.__doc__ = \
"""FT_STATUS FT_GetWriteQueueStatus(FT_HANDLE ftHandle, UCHAR ucFifoID, LPDWORD lpdwAmountInQueue)"""

FT_GetUnsentBuffer = _libraries[_libname].FT_GetUnsentBuffer
FT_GetUnsentBuffer.restype = FT_STATUS
# FT_GetUnsentBuffer(ftHandle, ucFifoID, byBuffer, lpdwBufferLength)
FT_GetUnsentBuffer.argtypes = [FT_HANDLE, UCHAR, LPVOID, PULONG]
FT_GetUnsentBuffer.__doc__ = \
"""FT_STATUS FT_GetUnsentBuffer(FT_HANDLE ftHandle, UCHAR ucFifoID, BYTE *byBuffer, LPDWORD lpdwBufferLength)"""


