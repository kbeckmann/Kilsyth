import sys
from ctypes import *
from defines import *


STRING = c_char_p
from ctypes.wintypes import DWORD
from ctypes.wintypes import ULONG
from ctypes.wintypes import WORD
from ctypes.wintypes import BYTE
from ctypes.wintypes import BOOL
from ctypes.wintypes import BOOLEAN
from ctypes.wintypes import LPCSTR
from ctypes.wintypes import HANDLE
from ctypes.wintypes import LONG
from ctypes.wintypes import UINT
from ctypes.wintypes import LPSTR
from ctypes.wintypes import FILETIME

_libname = 'ftd3xx.dll'
_libraries = {}
_libraries[_libname] = WinDLL(_libname)

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

FT_GetDeviceInfo = _libraries[_libname].FT_GetDeviceInfo
FT_GetDeviceInfo.restype = FT_STATUS
# FT_GetDeviceInfo(ftHandle, lpftDevice, lpdwID, SerialNumber, Description, Dummy)
FT_GetDeviceInfo.argtypes = [FT_HANDLE, POINTER(FT_DEVICE), LPDWORD, PCHAR, PCHAR, LPVOID]
FT_GetDeviceInfo.__doc__ = \
"""FT_STATUS FT_GetDeviceInfo(FT_HANDLE ftHandle, FT_DEVICE * lpftDevice, LPDWORD lpdwID, PCHAR SerialNumber, PCHAR Description, LPVOID Dummy)"""

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

FT_GetDeviceInfo = _libraries[_libname].FT_GetDeviceInfo
FT_GetDeviceInfo.restype = FT_STATUS
# FT_GetDeviceInfo(ftHandle, lpftDevice, lpdwID, SerialNumber, Description, Dummy)
FT_GetDeviceInfo.argtypes = [FT_HANDLE, POINTER(FT_DEVICE), LPDWORD, PCHAR, PCHAR, LPVOID]
FT_GetDeviceInfo.__doc__ = \
"""FT_STATUS FT_GetDeviceInfo(FT_HANDLE ftHandle, FT_DEVICE * lpftDevice, LPDWORD lpdwID, PCHAR SerialNumber, PCHAR Description, LPVOID Dummy)"""

class _OVERLAPPED(Structure):
    pass
_OVERLAPPED._fields_ = [
    ('Internal', DWORD),
    ('InternalHigh', DWORD),
    ('Offset', DWORD),
    ('OffsetHigh', DWORD),
    ('hEvent', HANDLE),
]
LPOVERLAPPED = POINTER(_OVERLAPPED)
OVERLAPPED = _OVERLAPPED

FT_WritePipe = _libraries[_libname].FT_WritePipe
FT_WritePipe.restype = FT_STATUS
# FT_WritePipe(ftHandle, ucPipeID, pucBuffer, ulBufferLength, pulBytesTransferred, pOverlapped)
FT_WritePipe.argtypes = [FT_HANDLE, UCHAR, LPVOID, ULONG, PULONG, LPOVERLAPPED]
FT_WritePipe.__doc__ = \
"""FT_STATUS FT_WritePipe(FT_HANDLE ftHandle, UCHAR ucPipeID, LPVOID pucBuffer, ULONG ulBufferLength, PULONG pulBytesTransferred, LPOVERLAPPED pOverlapped)"""

FT_ReadPipe = _libraries[_libname].FT_ReadPipe
FT_ReadPipe.restype = FT_STATUS
# FT_ReadPipe(ftHandle, ucPipeID, pucBuffer, ulBufferLength, pulBytesTransferred, pOverlapped)
FT_ReadPipe.argtypes = [FT_HANDLE, UCHAR, LPVOID, ULONG, PULONG, LPOVERLAPPED]
FT_ReadPipe.__doc__ = \
"""FT_STATUS FT_ReadPipe(FT_HANDLE ftHandle, UCHAR ucPipeID, LPVOID pucBuffer, ULONG ulBufferLength, PULONG pulBytesTransferred, LPOVERLAPPED pOverlapped)"""

FT_GetOverlappedResult = _libraries[_libname].FT_GetOverlappedResult
FT_GetOverlappedResult.restype = FT_STATUS
# FT_GetOverlappedResult(ftHandle, pOverlapped, pulBytesTransferred, bWait)
FT_GetOverlappedResult.argtypes = [FT_HANDLE, LPOVERLAPPED, PULONG, BOOL]
FT_GetOverlappedResult.__doc__ = \
"""FT_STATUS FT_GetOverlappedResult(FT_HANDLE ftHandle, LPOVERLAPPED pOverlapped, PULONG pulBytesTransferred, BOOL bWait)"""

FT_InitializeOverlapped = _libraries[_libname].FT_InitializeOverlapped
FT_InitializeOverlapped.restype = FT_STATUS
# FT_InitializeOverlapped(ftHandle, pOverlapped)
FT_InitializeOverlapped.argtypes = [FT_HANDLE, LPOVERLAPPED]
FT_InitializeOverlapped.__doc__ = \
"""FT_STATUS FT_InitializeOverlapped(FT_HANDLE ftHandle, LPOVERLAPPED pOverlapped)"""

FT_ReleaseOverlapped = _libraries[_libname].FT_ReleaseOverlapped
FT_ReleaseOverlapped.restype = FT_STATUS
# FT_ReleaseOverlapped(ftHandle, pOverlapped)
FT_ReleaseOverlapped.argtypes = [FT_HANDLE, LPOVERLAPPED]
FT_ReleaseOverlapped.__doc__ = \
"""FT_STATUS FT_ReleaseOverlapped(FT_HANDLE ftHandle, LPOVERLAPPED pOverlapped)"""

FT_AbortPipe = _libraries[_libname].FT_AbortPipe
FT_AbortPipe.restype = FT_STATUS
# FT_AbortPipe(ftHandle, ucPipeID)
FT_AbortPipe.argtypes = [FT_HANDLE, UCHAR]
FT_AbortPipe.__doc__ = \
"""FT_STATUS FT_AbortPipe(FT_HANDLE ftHandle, UCHAR ucPipeID)"""

FT_SetPipeTimeout = _libraries[_libname].FT_SetPipeTimeout
FT_SetPipeTimeout.restype = FT_STATUS
# FT_SetPipeTimeout(ftHandle, ucPipeID, TimeoutInMs)
FT_SetPipeTimeout.argtypes = [FT_HANDLE, UCHAR, ULONG]
FT_SetPipeTimeout.__doc__ = \
"""FT_STATUS FT_SetPipeTimeout(FT_HANDLE ftHandle, UCHAR ucPipeID, ULONG TimeoutInMs)"""

FT_GetPipeTimeout = _libraries[_libname].FT_GetPipeTimeout
FT_GetPipeTimeout.restype = FT_STATUS
# FT_GetPipeTimeout(ftHandle, ucPipeID, pTimeoutInMs)
FT_GetPipeTimeout.argtypes = [FT_HANDLE, UCHAR, PULONG]
FT_GetPipeTimeout.__doc__ = \
"""FT_STATUS FT_GetPipeTimeout(FT_HANDLE ftHandle, UCHAR ucPipeID, PULONG pTimeoutInMs)"""

FT_SetStreamPipe = _libraries[_libname].FT_SetStreamPipe
FT_SetStreamPipe.restype = FT_STATUS
# FT_SetStreamPipe(ftHandle, bAllWritePipes, bAllReadPipes, ucPipeID, ulStreamSize)
FT_SetStreamPipe.argtypes = [FT_HANDLE, BOOLEAN, BOOLEAN, UCHAR, ULONG]
FT_SetStreamPipe.__doc__ = \
"""FT_STATUS FT_SetStreamPipe(FT_HANDLE ftHandle, BOOLEAN bAllWritePipes, BOOLEAN bAllReadPipes, UCHAR ucPipeID, ULONG ulStreamSize)"""

FT_ClearStreamPipe = _libraries[_libname].FT_ClearStreamPipe
FT_ClearStreamPipe.restype = FT_STATUS
# FT_ClearStreamPipe(ftHandle, bAllWritePipes, bAllReadPipes, ucPipeID)
FT_ClearStreamPipe.argtypes = [FT_HANDLE, BOOLEAN, BOOLEAN, UCHAR]
FT_ClearStreamPipe.__doc__ = \
"""FT_STATUS FT_ClearStreamPipe(FT_HANDLE ftHandle, BOOLEAN bAllWritePipes, BOOLEAN bAllReadPipes, UCHAR ucPipeID)"""

class _FT_NOTIFICATION_CALLBACK_INFO_DATA(Structure):
    pass
_FT_NOTIFICATION_CALLBACK_INFO_DATA._fields_ = [
    ('ulRecvNotificationLength', ULONG),
    ('ucEndpointNo', UCHAR),
]
FT_NOTIFICATION_CALLBACK_INFO_DATA = _FT_NOTIFICATION_CALLBACK_INFO_DATA
PFT_NOTIFICATION_CALLBACK_INFO_DATA = POINTER(_FT_NOTIFICATION_CALLBACK_INFO_DATA)
FT_NOTIFICATION_CALLBACK = CFUNCTYPE(PVOID, ULONG, PFT_NOTIFICATION_CALLBACK_INFO_DATA)

FT_SetNotificationCallback = _libraries[_libname].FT_SetNotificationCallback
FT_SetNotificationCallback.restype = FT_STATUS
# FT_SetNotificationCallback(ftHandle, pCallback, pvCallbackContext)
FT_SetNotificationCallback.argtypes = [FT_HANDLE, FT_NOTIFICATION_CALLBACK, PVOID]
FT_SetNotificationCallback.__doc__ = \
"""FT_STATUS FT_SetNotificationCallback(FT_HANDLE ftHandle, FT_NOTIFICATION_CALLBACK pCallback, PVOID pvCallbackContext)"""

FT_ClearNotificationCallback = _libraries[_libname].FT_ClearNotificationCallback
FT_ClearNotificationCallback.restype = FT_STATUS
# FT_ClearNotificationCallback(ftHandle)
FT_ClearNotificationCallback.argtypes = [FT_HANDLE]
FT_ClearNotificationCallback.__doc__ = \
"""FT_STATUS FT_ClearNotificationCallback(FT_HANDLE ftHandle)"""

FT_CycleDevicePort = _libraries[_libname].FT_CycleDevicePort
FT_CycleDevicePort.restype = FT_STATUS
# FT_CycleDevicePort(ftHandle)
FT_CycleDevicePort.argtypes = [FT_HANDLE]
FT_CycleDevicePort.__doc__ = \
"""FT_STATUS FT_CycleDevicePort(FT_HANDLE ftHandle)"""

FT_SetSuspendTimeout = _libraries[_libname].FT_SetSuspendTimeout
FT_SetSuspendTimeout.restype = FT_STATUS
# FT_SetSuspendTimeout(ftHandle, Timeout)
FT_SetSuspendTimeout.argtypes = [FT_HANDLE, ULONG]
FT_SetSuspendTimeout.__doc__ = \
"""FT_STATUS FT_SetSuspendTimeout(FT_HANDLE ftHandle, ULONG Timeout)"""

FT_GetSuspendTimeout = _libraries[_libname].FT_GetSuspendTimeout
FT_GetSuspendTimeout.restype = FT_STATUS
# FT_GetSuspendTimeout(ftHandle, pTimeout)
FT_GetSuspendTimeout.argtypes = [FT_HANDLE, PULONG]
FT_GetSuspendTimeout.__doc__ = \
"""FT_STATUS FT_GetSuspendTimeout(FT_HANDLE ftHandle, PULONG pTimeout)"""


