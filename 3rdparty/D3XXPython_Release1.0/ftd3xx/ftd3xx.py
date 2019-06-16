import sys
if sys.platform == 'win32':
    from ._ftd3xx_win32 import *
elif sys.platform == 'linux':
    from ._ftd3xx_linux import *
import ctypes as c
import threading
import time
from .defines import *

msgs = [
	'FT_OK',
	'FT_INVALID_HANDLE',
	'FT_DEVICE_NOT_FOUND',
	'FT_DEVICE_NOT_OPENED',
	'FT_IO_ERROR',
	'FT_INSUFFICIENT_RESOURCES',
	'FT_INVALID_PARAMETER',
	'FT_INVALID_BAUD_RATE',
	'FT_DEVICE_NOT_OPENED_FOR_ERASE',
	'FT_DEVICE_NOT_OPENED_FOR_WRITE',
	'FT_FAILED_TO_WRITE_DEVICE',
	'FT_EEPROM_READ_FAILED',
	'FT_EEPROM_WRITE_FAILED',
	'FT_EEPROM_ERASE_FAILED',
	'FT_EEPROM_NOT_PRESENT',
	'FT_EEPROM_NOT_PROGRAMMED',
	'FT_INVALID_ARGS',
	'FT_NOT_SUPPORTED',
	'FT_NO_MORE_ITEMS',
	'FT_TIMEOUT',
	'FT_OPERATION_ABORTED',
	'FT_RESERVED_PIPE',
	'FT_INVALID_CONTROL_REQUEST_DIRECTION',
	'FT_INVALID_CONTROL_REQUEST_TYPE',
	'FT_IO_PENDING',
	'FT_IO_INCOMPLETE',
	'FT_HANDLE_EOF',
	'FT_BUSY',
	'FT_NO_SYSTEM_RESOURCES',
	'FT_DEVICE_LIST_NOT_READY',
	'FT_DEVICE_NOT_CONNECTED',
	'FT_INCORRECT_DEVICE_PATH',
	'FT_OTHER_ERROR']

bRaiseExceptionOnError = []



class DeviceError(Exception):
    """Exception class for status messages"""
    def __init__(self, msgnum):
        self.message = msgs[msgnum]
    def __str__(self):
        return self.message

def call_ft(function, *args):
    """Call an FTDI function and check the status. Raise exception on error"""
    status = function(*args)
    if len(bRaiseExceptionOnError) > 0:
        if status != FT_OK:
            raise DeviceError(status)
    return status

def raiseExceptionOnError(bEnable):
    """Enable or disable exception handling"""
    origValue = len(bRaiseExceptionOnError) > 0
    if bEnable == True:
        if len(bRaiseExceptionOnError) == 0:	
            bRaiseExceptionOnError.append(True)
    else:
        if len(bRaiseExceptionOnError) > 0:
            bRaiseExceptionOnError.get()
    return origValue
	
def getStrError(status):
    """Return string equivalent for error status"""
    return msgs[status]
	
def listDevices(flags=FT_OPEN_BY_DESCRIPTION):
    """Return a list of serial numbers(default), descriptions or
    locations (Windows only) of the connected FTDI devices depending on value of flags"""
    n = DWORD()
    call_ft(FT_ListDevices, c.byref(n), None, DWORD(FT_LIST_NUMBER_ONLY))
    devcount = n.value
    if devcount:
        if  flags == FT_OPEN_BY_INDEX:
            flags = FT_OPEN_BY_DESCRIPTION	    
        # since ctypes has no pointer arithmetic.
        bd = [c.c_buffer(FT_MAX_DESCRIPTION_SIZE) for i in range(devcount)] + [None]
        # array of pointers to those strings, initially all NULL
        ba = (c.c_char_p *(devcount + 1))()
        for i in range(devcount):
            ba[i] = c.cast(bd[i], c.c_char_p)
        call_ft(FT_ListDevices, ba, c.byref(n), DWORD(FT_LIST_ALL|flags))
        return [res for res in ba[:devcount]]
    else:
        return None
		
def createDeviceInfoList():
    """Create the internal device info list and return number of entries"""
    numDevices = DWORD()
    call_ft(FT_CreateDeviceInfoList, c.byref(numDevices))
    return numDevices.value

def getDeviceInfoList():
    """Get device info list and return number of entries"""
    numDevices = DWORD()
    call_ft(FT_ListDevices, c.byref(numDevices), None, DWORD(FT_LIST_NUMBER_ONLY))
    numDevices = numDevices.value
    if numDevices == 0:
        return None
    """Use getDeviceInfoDetail instead"""
    deviceList = []
    for i in range(numDevices):
        device = FT_DEVICE_LIST_INFO_NODE()
        deviceInfo = getDeviceInfoDetail(i)
        device.Flags = deviceInfo['Flags']
        device.ID = deviceInfo['ID']
        device.LocId = deviceInfo['LocId']
        device.SerialNumber = deviceInfo['SerialNumber']
        device.Description = deviceInfo['Description']
        deviceList.append(device)
    return deviceList

def getDeviceInfoDetail(devnum=0):
    """Get an entry from the internal device info list."""
    f = DWORD()
    t = DWORD()
    i = DWORD()
    l = DWORD()
    h = FT_HANDLE()
    n = c.c_buffer(FT_MAX_DESCRIPTION_SIZE)
    d = c.c_buffer(FT_MAX_DESCRIPTION_SIZE)
    call_ft(FT_GetDeviceInfoDetail, DWORD(devnum),
        c.byref(f), c.byref(t), c.byref(i), c.byref(l), n, d, c.byref(h))
    if sys.platform == 'linux':
        """Linux creates a handle to the device so close it. D3XX Linux driver issue."""
        call_ft(FT_Close, h)
    return {'Flags': f.value, 
        'Type': t.value,
        'ID': i.value, 
        'LocId': l.value, 
        'SerialNumber': n.value,
        'Description': d.value}
			
def create(id_str, flags=FT_OPEN_BY_INDEX):
    """Open a handle to a usb device by serial number, description or
    index depending on value of flags and return an FTD3XX instance for it"""
    h = FT_HANDLE()
    status = call_ft(FT_Create, id_str, DWORD(flags), c.byref(h))
    if (status != FT_OK): 
        return None
    return FTD3XX(h)

def setTransferParams(conf, fifo):
    """Set transfer parameters for Linux only"""
    if sys.platform == 'linux':
        call_ft(FT_SetTransferParams, c.byref(conf), fifo)
    return None	



class FTD3XX(object):
    """Class for communicating with an FTDI device"""
    def __init__(self, handle):
        """Create an instance of the FTD3XX class with the given device handle
        and populate the device info in the instance dictionary. Set
        update to False to avoid a slow call to createDeviceInfoList."""
        self.handle = handle
        self.status = 0
        return None
		
    def close(self, noreset=False):
        """Close the device handle"""
        self.status = call_ft(FT_Close, self.handle)
        return None

    def getLastError(self):
        """Return status"""
        return self.status
		
    def flushPipe(self, pipe):
        """Flush pipe"""
        self.status = call_ft(FT_FlushPipe, self.handle, UCHAR(pipe))
        return None

    def getDeviceInfo(self):
        """Returns a dictionary describing the device. """
        deviceType = DWORD()
        deviceId = DWORD()
        desc = c.c_buffer(FT_MAX_DESCRIPTION_SIZE)
        serial = c.c_buffer(FT_MAX_DESCRIPTION_SIZE)
        self.status = call_ft(FT_GetDeviceInfo, self.handle, c.byref(deviceType), c.byref(deviceId), serial, desc, None)
        return {'Type': deviceType.value, 
            'ID': deviceId.value,
            'Description': desc.value, 
            'Serial': serial.value}

    def getDeviceDescriptor(self):
        """Returns a dictionary describing the device descriptor. """
        devDesc = FT_DEVICE_DESCRIPTOR()
        self.status = call_ft(FT_GetDeviceDescriptor, self.handle, c.byref(devDesc))
        return devDesc

    def getStringDescriptor(self, index):
        """Returns a string descriptor. """
        strDesc = FT_STRING_DESCRIPTOR()
        lenTransferred = ULONG()
        self.status = call_ft(FT_GetDescriptor, self.handle, UCHAR(FT_STRING_DESCRIPTOR_TYPE), UCHAR(index), c.pointer(strDesc), c.sizeof(strDesc), c.byref(lenTransferred))
        return strDesc

    def getConfigurationDescriptor(self):
        """Returns a dictionary describing the configuration descriptor. """
        cfgDesc = FT_CONFIGURATION_DESCRIPTOR()
        self.status = call_ft(FT_GetConfigurationDescriptor, self.handle, c.byref(cfgDesc))
        return cfgDesc
	
    def getInterfaceDescriptor(self, interfaceIndex):
        """Returns a dictionary describing the interface descriptor for the specified index. """
        ifDesc = FT_INTERFACE_DESCRIPTOR()
        self.status = call_ft(FT_GetInterfaceDescriptor, self.handle, UCHAR(interfaceIndex), c.byref(ifDesc))
        return ifDesc				
		
    def getPipeInformation(self, interfaceIndex, pipeIndex):
        """Returns a dictionary describing the pipe infromationfor the specified indexes. """
        pipeDesc = FT_PIPE_INFORMATION()
        self.status = call_ft(FT_GetPipeInformation, self.handle, UCHAR(interfaceIndex), UCHAR(pipeIndex), c.byref(pipeDesc))
        return pipeDesc
	
    def getChipConfiguration(self):
        """Returns a dictionary describing the chip configuration. """
        chipCfg = FT_60XCONFIGURATION()
        self.status = call_ft(FT_GetChipConfiguration, self.handle, c.byref(chipCfg))
        return chipCfg
	
    def setChipConfiguration(self, chipCfg):
        """Sets a chip configuration. """
        self.status = call_ft(FT_SetChipConfiguration, self.handle, c.byref(chipCfg))
        return None
	
    def getVIDPID(self):
        """Get the VID and PID of the device"""
        vid = USHORT()
        pid = USHORT()
        self.status = call_ft(FT_GetVIDPID, self.handle, c.byref(vid), c.byref(pid))
        return (vid.value, pid.value)
	
    def getLibraryVersion(self):
        """Get the version of the user driver library"""
        libraryVer = DWORD()
        self.status = call_ft(FT_GetLibraryVersion, c.byref(libraryVer))
        return libraryVer.value
		
    def getDriverVersion(self):
        """Get the version of the kernel driver"""
        driverVer = DWORD()
        self.status = call_ft(FT_GetDriverVersion, self.handle, c.byref(driverVer))
        return driverVer.value
	
    def getFirmwareVersion(self):
        """Get the version of the firmware"""
        firmwareVer = DWORD()
        self.status = call_ft(FT_GetFirmwareVersion, self.handle, c.byref(firmwareVer))
        return firmwareVer.value
	
    def resetDevicePort(self):
        """Reset port where device is connected"""
        self.status = call_ft(FT_ResetDevicePort, self.handle)
        return None
			
    def enableGPIO(self, mask, direction):
        """Enable GPIO"""
        self.status = call_ft(FT_EnableGPIO, self.handle, ULONG(mask), ULONG(direction))
        return None
		
    def writeGPIO(self, mask, data):
        """Write GPIO"""
        self.status = call_ft(FT_WriteGPIO, self.handle, ULONG(mask), ULONG(data))
        return None
		
    def readGPIO(self):
        """Read GPIO"""
        gpio = ULONG()
        self.status = call_ft(FT_ReadGPIO, self.handle, c.byref(gpio))
        return gpio.value

    def setGPIOPull(self, mask, pull):
        """Set GPIO pull"""
        self.status = call_ft(FT_SetGPIOPull, self.handle, ULONG(mask), ULONG(pull))
        return None

    # OS-dependent functions
    # If Windows	
    if sys.platform == 'win32':

        def writePipe(self, pipe, data, datalen):
            """Send the data to the device."""
            bytesTransferred = ULONG()
            self.status = call_ft(FT_WritePipe, self.handle, UCHAR(pipe), data, ULONG(datalen), c.byref(bytesTransferred), None)
            return bytesTransferred.value

        def readPipe(self, pipe, data, datalen):
            """Recv the data to the device."""
            bytesTransferred = ULONG()
            self.status = call_ft(FT_ReadPipe, self.handle, UCHAR(pipe), data, ULONG(datalen), c.byref(bytesTransferred), None)
            return bytesTransferred.value

        def readPipeEx(self, pipe, datalen, raw=True):
            """Recv the data to the device."""
            bytesTransferred = ULONG()
            data = c.c_buffer(datalen)
            self.status = call_ft(FT_ReadPipe, self.handle, UCHAR(pipe), data, ULONG(datalen), c.byref(bytesTransferred), None)
            return {'bytesTransferred' : bytesTransferred.value,
                'bytes' : data.raw[:bytesTransferred.value] if raw==True else data.value[:bytesTransferred.value]}
			
        def setPipeTimeout(self, pipeid, timeoutMS):
            """Set pipe timeout"""
            self.status = call_ft(FT_SetPipeTimeout, self.handle, UCHAR(pipeid), ULONG(timeoutMS))
            return None		
	
        def getPipeTimeout(self, pipeid):
            """Get pipe timeout"""
            timeoutMS = ULONG()
            self.status = call_ft(FT_GetPipeTimeout, self.handle, UCHAR(pipeid), c.byref(timeoutMS))
            return timeoutMS.value
			
        def setStreamPipe(self, pipe, size):
            """Set stream pipe for continous transfer of fixed size"""
            self.status = call_ft(FT_SetStreamPipe, self.handle, BOOLEAN(0), BOOLEAN(0), UCHAR(pipe), ULONG(size))
            return None

        def clearStreamPipe(self, pipe):
            """Clear stream pipe for continous transfer of fixed size"""
            self.status = call_ft(FT_ClearStreamPipe, self.handle, BOOLEAN(0), BOOLEAN(0), UCHAR(pipe))
            return None
		
        def abortPipe(self, pipe):
            """Abort ongoing transfers for the specifed pipe"""
            self.status = call_ft(FT_AbortPipe, self.handle, UCHAR(pipe))
            return None

        def cycleDevicePort(self):
            """Cycle port where device is connected"""
            self.status = call_ft(FT_CycleDevicePort, self.handle)
            return None	

        def setSuspendTimeout(self, timeout):
            """Set suspend timeout"""
            self.status = call_ft(FT_SetSuspendTimeout, self.handle, ULONG(timeout))
            return None		
	
        def getSuspendTimeout(self):
            """Get suspend timeout"""
            timeout = ULONG()
            self.status = call_ft(FT_GetSuspendTimeout, self.handle, c.byref(timeout))
            return timeout.value
		
    # OS-dependent functions
    # If Linux
    elif sys.platform == 'linux':
	
        def writePipe(self, channel, data, datalen, timeout=1000):
            """Send the data to the device."""
            bytesTransferred = ULONG()
            self.status = call_ft(FT_WritePipeEx, self.handle, UCHAR(channel), data, ULONG(datalen), c.byref(bytesTransferred), timeout)
            return bytesTransferred.value

        def readPipe(self, channel, data, datalen, timeout=1000):
            """Recv the data to the device."""
            bytesTransferred = ULONG()
            self.status = call_ft(FT_ReadPipeEx, self.handle, UCHAR(channel), data, ULONG(datalen), c.byref(bytesTransferred), timeout)
            return bytesTransferred.value

        def readPipeEx(self, channel, datalen, timeout=1000, raw=False):
            """Recv the data to the device."""
            bytesTransferred = ULONG()
            data = c.c_buffer(datalen)
            self.status = call_ft(FT_ReadPipeEx, self.handle, UCHAR(channel), data, ULONG(datalen), c.byref(bytesTransferred), timeout)
            return {'bytesTransferred' : bytesTransferred.value,
                'bytes' : data.value[:bytesTransferred.value] if raw==False else data.raw[:bytesTransferred.value]}
				
        def getReadQueueStatus(self, channel):
            """Get the current bytes in the read queue."""		
            bytesInQueue = ULONG()
            self.status = call_ft(FT_GetReadQueueStatus, self.handle, channel, c.byref(bytesInQueue))
            return bytesInQueue	

        def getWriteQueueStatus(self, channel):
            """Get the current bytes in the write queue."""		
            bytesInQueue = ULONG()
            self.status = call_ft(FT_GetWriteQueueStatus, self.handle, channel, c.byref(bytesInQueue))
            return bytesInQueue	

        def getUnsentBuffer(self, channel):
            """Get the current bytes not yet sent to device."""
            # get size only	
            bytesTransferred = ULONG()
            self.status = call_ft(FT_GetUnsentBuffer, self.handle, None, c.byref(bytesTransferred))
            if (bytesTransferred == 0):
                return {'bytesTransferred' : 0,
                    'bytes' : None}
					
            # get and buffer
            data = c.c_buffer(bytesTransferred)
            bytesTransferred = 0
            self.status = call_ft(FT_GetUnsentBuffer, self.handle, data, c.byref(bytesTransferred))			
            return {'bytesTransferred' : bytesTransferred.value,
                'bytes' : data.raw[:bytesTransferred.value] if raw==True else data.value[:bytesTransferred.value]}



__all__ = [ 'call_ft',
    'listDevices',
    'createDeviceInfoList',
    'getDeviceInfoDetail',
    'getDeviceInfoList',
    'getStrError',
    'setTransferParams',
    'create',
    'FTD3XX',
    'raiseExceptionOnError',
    'DeviceError']
