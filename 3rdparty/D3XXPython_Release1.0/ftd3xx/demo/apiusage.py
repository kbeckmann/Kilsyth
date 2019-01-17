import ftd3xx
import sys
if sys.platform == 'win32':
    import ftd3xx._ftd3xx_win32 as _ft
elif sys.platform == 'linux':
    import ftd3xx._ftd3xx_linux as _ft
import datetime
import time
import binascii
import itertools
import ctypes
import threading
import logging
import os
import platform
import random
import string
import struct



def DemoGetNumDevicesConnected():

    DEVICES = ftd3xx.listDevices()
    return len(DEVICES) if DEVICES is not None else 0


def DemoWaitForDeviceReenumeration():

    # should be called when setChipConfiguration, cycleDevicePort or resetDevicePort is called
    # todo: get optimal sleep times
    origValue = ftd3xx.raiseExceptionOnError(False)
    time.sleep(1)
    while (ftd3xx.listDevices() == None):
        time.sleep(1)
    time.sleep(1)
    ftd3xx.raiseExceptionOnError(origValue)

    if sys.platform == 'linux':
        count = 0
        while count == 0:
            count = ftd3xx.createDeviceInfoList()


def DemoTurnOffPipeThreads():

    # Call before FT_Create when non-transfer functions will be called
    # Only needed for RevA chip (Firmware 1.0.2)
    # Not necessary starting RevB chip (Firmware 1.0.9)

    if sys.platform == 'linux':

        conf = _ft.FT_TRANSFER_CONF();
        conf.wStructSize = ctypes.sizeof(_ft.FT_TRANSFER_CONF);
        conf.pipe[_ft.FT_PIPE_DIR_IN].fPipeNotUsed = True;
        conf.pipe[_ft.FT_PIPE_DIR_OUT].fPipeNotUsed = True;
        conf.pipe.fReserved = False;
        conf.pipe.fKeepDeviceSideBufferAfterReopen = False;
        for i in range(4):
            ftd3xx.setTransferParams(conf, i);

    return True


def DemoEnumerateDevices():

    numDevices = ftd3xx.createDeviceInfoList()
    if (numDevices == 0):
        return False

    # list devices by listDevices(description)
    logging.debug("List devices by listDevices(description)")
    DEVICES = ftd3xx.listDevices(_ft.FT_OPEN_BY_DESCRIPTION)
    if (DEVICES is None):
        return False
    logging.debug("Device count = %d" % len(DEVICES))	
    for i in range(len(DEVICES)):
        logging.debug("DEVICE[%d] = %s" % (i, DEVICES[i].decode('utf-8')))
    DEVICES = 0
    logging.debug("")

    # list devices by listDevices(serial number)
    logging.debug("List devices by listDevices(serial number)")
    DEVICES = ftd3xx.listDevices(_ft.FT_OPEN_BY_SERIAL_NUMBER)
    if (DEVICES is None):
        return False
    logging.debug("Device count = %d" % len(DEVICES))	
    for i in range(len(DEVICES)):
        logging.debug("DEVICE[%d] = %s" % (i, DEVICES[i].decode('utf-8')))
    DEVICES = 0
    logging.debug("")	

    # list devices by getDeviceInfoList()
    logging.debug("List devices by getDeviceInfoList()")
    logging.debug("Device count = %d" % numDevices)	
    DEVICELIST = ftd3xx.getDeviceInfoList()
    for i in range(numDevices):
        logging.debug("DEVICE[%d]" % i)
        logging.debug("\tFlags = %d" % DEVICELIST[i].Flags)
        logging.debug("\tType = %d" % DEVICELIST[i].Type)
        logging.debug("\tID = %#010X" % DEVICELIST[i].ID)
        logging.debug("\tLocId = %d" % DEVICELIST[i].LocId)
        logging.debug("\tSerialNumber = %s" % DEVICELIST[i].SerialNumber.decode('utf-8'))
        logging.debug("\tDescription = %s" % DEVICELIST[i].Description.decode('utf-8'))
    DEVICELIST = 0
    logging.debug("")		

    # list devices by getDeviceInfoDetail()
    logging.debug("List devices by getDeviceInfoDetail()")
    logging.debug("Device count = %d" % numDevices)	
    for i in range(numDevices):
        DEVICE = ftd3xx.getDeviceInfoDetail(i)
        logging.debug("DEVICE[%d]" % i)
        logging.debug("\tFlags = %d" % DEVICE['Flags'])
        logging.debug("\tType = %d" % DEVICE['Type'])
        logging.debug("\tID = %#010X" % DEVICE['ID'])
        logging.debug("\tLocId = %d" % DEVICE['LocId'])
        logging.debug("\tSerialNumber = %s" % DEVICE['SerialNumber'].decode('utf-8'))
        logging.debug("\tDescription = %s" % DEVICE['Description'].decode('utf-8'))
        DEVICE = 0
    logging.debug("")

    return True


def DemoOpenDeviceBy():

    if sys.platform == 'linux':
        DemoTurnOffPipeThreads()

    # get description and serial number of device at index 0
    ftd3xx.createDeviceInfoList()
    DEVICELIST = ftd3xx.getDeviceInfoList()

    # open device by index
    openby = 0
    logging.debug("Open by index [%d]" % openby)
    D3XX = ftd3xx.create(0, _ft.FT_OPEN_BY_INDEX)
    if (D3XX is None):
        logging.debug("ERROR: Please check if another D3XX application is open!")
        return False
    D3XX.close()
    D3XX = 0

    # open device by description
    if sys.platform == 'linux':
        DemoTurnOffPipeThreads()
        ftd3xx.createDeviceInfoList()
        DEVICELIST = ftd3xx.getDeviceInfoList()
    openby = DEVICELIST[0].Description
    logging.debug("Open by description [%s]" % openby.decode('utf-8'))
    D3XX = ftd3xx.create(openby, _ft.FT_OPEN_BY_DESCRIPTION)
    if D3XX is None:
        logging.debug("ERROR: Please check if another D3XX application is open!")
        return False
    D3XX.close()
    D3XX = 0

    # open device by serial number
    if sys.platform == 'linux':
        DemoTurnOffPipeThreads()
        ftd3xx.createDeviceInfoList()
        DEVICELIST = ftd3xx.getDeviceInfoList()
    openby = DEVICELIST[0].SerialNumber
    logging.debug("Open by serial number [%s]" % openby.decode('utf-8'))
    D3XX = ftd3xx.create(openby, _ft.FT_OPEN_BY_SERIAL_NUMBER)
    if D3XX is None:
        logging.debug("ERROR: Please check if another D3XX application is open!")
        return False
    D3XX.close()
    D3XX = 0
	
    return True
	

def DemoVersions():

    if sys.platform == 'linux':
        DemoTurnOffPipeThreads()

    D3XX = ftd3xx.create(0, _ft.FT_OPEN_BY_INDEX)
    if D3XX is None:
        logging.debug("ERROR: Please check if another D3XX application is open!")
        return False
		
    # getLibraryVersion
    ulLibraryVersion = D3XX.getLibraryVersion()
    logging.debug("LibraryVersion = %#08X" % ulLibraryVersion)

    # getDriverVersion
    ulDriverVersion = D3XX.getDriverVersion()
    logging.debug("DriverVersion = %#08X" % ulDriverVersion)

    # getFirmwareVersion
    ulFirmwareVersion = D3XX.getFirmwareVersion()
    logging.debug("FirmwareVersion = %#08X" % ulFirmwareVersion)
	
    D3XX.close()
    D3XX = 0	

    # check driver version
    if (sys.platform == 'win32'):	
        if (ulDriverVersion < 0x01020006):
            logging.debug("ERROR: Old kernel driver version. Please update driver from Windows Update or FTDI website!")
            return False
	
    return True

	
def DemoDescriptors():

    if sys.platform == 'linux':
        DemoTurnOffPipeThreads()

    D3XX = ftd3xx.create(0, _ft.FT_OPEN_BY_INDEX)
    if D3XX is None:
        logging.debug("ERROR: Please check if another D3XX application is open!")
        return False
		
    # getVIDPID
    VID, PID = D3XX.getVIDPID()
    logging.debug("VID = %#04X" % VID)
    logging.debug("PID = %#04X" % PID)
    logging.debug("")

    if sys.platform == 'win32':
        # getDeviceInfo
        DEVINFO = D3XX.getDeviceInfo()
        logging.debug("Type = %d" % DEVINFO['Type'])
        logging.debug("ID = %#08X" % DEVINFO['ID'])
        logging.debug("Serial = %s" % DEVINFO['Serial'].decode('utf-8'))
        logging.debug("Description = %s" % DEVINFO['Description'].decode('utf-8'))	
        logging.debug("")
	
    # getDeviceDescriptor
    DEVDESC = D3XX.getDeviceDescriptor()
    STRDESCMANU = D3XX.getStringDescriptor(DEVDESC.iManufacturer)
    STRDESCPROD = D3XX.getStringDescriptor(DEVDESC.iProduct)
    STRDESCSERN = D3XX.getStringDescriptor(DEVDESC.iSerialNumber)
    logging.debug("Device Descriptor")
    logging.debug("\tbLength = %d" % DEVDESC.bLength)
    logging.debug("\tbDescriptorType = %d" % DEVDESC.bDescriptorType)
    logging.debug("\tbcdUSB = %#04X (%s)" % (DEVDESC.bcdUSB, "USB2" if (DEVDESC.bcdUSB < 0x300) else "USB3"))
    logging.debug("\tbDeviceClass = %#02X" % DEVDESC.bDeviceClass)
    logging.debug("\tbDeviceSubClass = %#02X" % DEVDESC.bDeviceSubClass)
    logging.debug("\tbDeviceProtocol = %#02X" % DEVDESC.bDeviceProtocol)
    logging.debug("\tbMaxPacketSize0 = %#02X (%d)" % (DEVDESC.bMaxPacketSize0, DEVDESC.bMaxPacketSize0))
    logging.debug("\tidVendor = %#04X" % DEVDESC.idVendor)
    logging.debug("\tidProduct = %#04X" % DEVDESC.idProduct)
    logging.debug("\tbcdDevice = %#04X" % DEVDESC.bcdDevice)
    if sys.platform == 'win32':
        logging.debug("\tiManufacturer = %#02X (%s)" % (DEVDESC.iManufacturer, str(STRDESCMANU.szString)))
        logging.debug("\tiProduct = %#02X (%s)" % (DEVDESC.iProduct, str(STRDESCPROD.szString)))
        logging.debug("\tiSerialNumber = %#02X (%s)" % (DEVDESC.iSerialNumber, str(STRDESCSERN.szString)))
    else:
        logging.debug("\tiManufacturer = %#02X" % (DEVDESC.iManufacturer))
        logging.debug("\tiProduct = %#02X" % (DEVDESC.iProduct))
        logging.debug("\tiSerialNumber = %#02X" % (DEVDESC.iSerialNumber))
    logging.debug("\tbNumConfigurations = %#02X" % DEVDESC.bNumConfigurations)	
    logging.debug("")	
	
    # getConfigurationDescriptor
    CFGDESC = D3XX.getConfigurationDescriptor()
    logging.debug("Configuration Descriptor")
    logging.debug("\tbLength = %d" % CFGDESC.bLength)
    logging.debug("\tbDescriptorType = %d" % CFGDESC.bDescriptorType)
    logging.debug("\twTotalLength = %#04X (%d)" % (CFGDESC.wTotalLength, CFGDESC.wTotalLength))
    logging.debug("\tbNumInterfaces = %#02X" % CFGDESC.bNumInterfaces)
    logging.debug("\tbConfigurationValue = %#02X" % CFGDESC.bConfigurationValue)
    logging.debug("\tiConfiguration = %#02X" % CFGDESC.iConfiguration)
	
    bSelfPowered = "Self-powered" if (CFGDESC.bmAttributes & _ft.FT_SELF_POWERED_MASK) else "Bus-powered"
    bRemoteWakeup = "Remote wakeup" if (CFGDESC.bmAttributes & _ft.FT_REMOTE_WAKEUP_MASK) else ""
    logging.debug("\tbmAttributes = %#02X (%s %s)" % (CFGDESC.bmAttributes, bSelfPowered, bRemoteWakeup))
    logging.debug("\tMaxPower = %#02X (%d mA)" % (CFGDESC.MaxPower, CFGDESC.MaxPower))
    logging.debug("")
	
    # getInterfaceDescriptor
    # getPipeInformation
    for i in range(CFGDESC.bNumInterfaces):
        IFDESC = D3XX.getInterfaceDescriptor(i)
        logging.debug("\tInterface Descriptor [%d]" % i)
        logging.debug("\t\tbLength = %d" % IFDESC.bLength)
        logging.debug("\t\tbDescriptorType = %d" % IFDESC.bDescriptorType)
        logging.debug("\t\tbInterfaceNumber = %#02X" % IFDESC.bInterfaceNumber)
        logging.debug("\t\tbAlternateSetting = %#02X" % IFDESC.bAlternateSetting)
        logging.debug("\t\tbNumEndpoints = %#02X" % IFDESC.bNumEndpoints)
        logging.debug("\t\tbInterfaceClass = %#02X" % IFDESC.bInterfaceClass)
        logging.debug("\t\tbInterfaceSubClass = %#02X" % IFDESC.bInterfaceSubClass)
        logging.debug("\t\tbInterfaceProtocol = %#02X" % IFDESC.bInterfaceProtocol)
        logging.debug("\t\tiInterface = %#02X" % IFDESC.iInterface)
        logging.debug("")
		
        for j in range(IFDESC.bNumEndpoints):
            PIPEIF = D3XX.getPipeInformation(i, j)
            logging.debug("\t\tPipe Information [%d]" % j)
            logging.debug("\t\t\tPipeType = %d" % PIPEIF.PipeType)
            logging.debug("\t\t\tPipeId = %#02X" % PIPEIF.PipeId)
            logging.debug("\t\t\tMaximumPacketSize = %#02X" % PIPEIF.MaximumPacketSize)
            logging.debug("\t\t\tInterval = %#02X" % PIPEIF.Interval)	
            logging.debug("")
	
    D3XX.close()
    D3XX = 0	
	
    return True
	
	
def GetInfoFromStringDescriptor(stringDescriptor):

    desc = bytearray(stringDescriptor)
	
    len = int(desc[0])
    Manufacturer = ""
    for i in range(2, len, 2):
        Manufacturer += "{0:c}".format(desc[i])
    desc = desc[len:]

    len = desc[0]
    ProductDescription = ""
    for i in range(2, len, 2):
        ProductDescription += "{0:c}".format(desc[i])
    desc = desc[len:]

    len = desc[0]
    SerialNumber = ""
    for i in range(2, len, 2):
        SerialNumber += "{0:c}".format(desc[i])
    desc = desc[len:]
	
    return {'Manufacturer': Manufacturer,
        'ProductDescription': ProductDescription,
        'SerialNumber': SerialNumber}

		
def SetInfoForStringDescriptor(cfg, manufacturer, productDescription, serialNumber):

    # verify length of strings
    if (len(manufacturer) >= _ft.FT_MAX_MANUFACTURER_SIZE):
        return False	
    if (len(productDescription) >= _ft.FT_MAX_DESCRIPTION_SIZE):
        return False	
    if (len(serialNumber) >= _ft.FT_MAX_SERIAL_NUMBER_SIZE):
        return False	

    # convert strings to bytearrays
    manufacturer = bytearray(manufacturer, 'utf-8')
    productDescription = bytearray(productDescription, 'utf-8')
    serialNumber = bytearray(serialNumber, 'utf-8')
	
    ctypes.memset(cfg.StringDescriptors, 0, 128)
    desc = cfg.StringDescriptors

    # copy manufacturer
    offset = 0
    desc[offset] = len(manufacturer)*2 + 2
    desc[offset + 1] = 0x3
    offset += 2
    for i in range (0, len(manufacturer)):
        desc[int(offset + (i*2))] = manufacturer[i]	
        desc[int(offset + (i*2)+1)] = 0x0	        
	
    # copy product description
    offset += len(manufacturer)*2
    desc[offset] = len(productDescription)*2 + 2
    desc[offset + 1] = 0x3
    offset += 2
    for i in range (0, len(productDescription)):
        desc[int(offset + (i*2))] = productDescription[i]	
        desc[int(offset + (i*2)+1)] = 0x0	        

    # copy serial number
    offset += len(productDescription)*2
    desc[offset] = len(serialNumber)*2 + 2
    desc[offset + 1] = 0x3
    offset += 2
    for i in range (0, len(serialNumber)):
        desc[int(offset + (i*2))] = serialNumber[i]	
        desc[int(offset + (i*2)+1)] = 0x0	        
		
    #for e in desc: print "%x" % e
    return True


def DisplayChipConfiguration(cfg):

    logging.debug("Chip Configuration:")
    logging.debug("\tVendorID = %#06x" % cfg.VendorID)
    logging.debug("\tProductID = %#06x" % cfg.ProductID)
	
    logging.debug("\tStringDescriptors")
    STRDESC = GetInfoFromStringDescriptor(cfg.StringDescriptors)
    logging.debug("\t\tManufacturer = %s" % STRDESC['Manufacturer'])
    logging.debug("\t\tProductDescription = %s" % STRDESC['ProductDescription'])
    logging.debug("\t\tSerialNumber = %s" % STRDESC['SerialNumber'])
	
    logging.debug("\tInterruptInterval = %#04x" % cfg.bInterval)
	
    bSelfPowered = "Self-powered" if (cfg.PowerAttributes & _ft.FT_SELF_POWERED_MASK) else "Bus-powered"
    bRemoteWakeup = "Remote wakeup" if (cfg.PowerAttributes & _ft.FT_REMOTE_WAKEUP_MASK) else ""
    logging.debug("\tPowerAttributes = %#04x (%s %s)" % (cfg.PowerAttributes, bSelfPowered, bRemoteWakeup))
	
    logging.debug("\tPowerConsumption = %#04x" % cfg.PowerConsumption)
    logging.debug("\tReserved2 = %#04x" % cfg.Reserved2)

    fifoClock = ["100 MHz", "66 MHz", "50 MHz", "40 MHz"]
    logging.debug("\tFIFOClock = %#04x (%s)" % (cfg.FIFOClock, fifoClock[cfg.FIFOClock]))
	
    fifoMode = ["245 Mode", "600 Mode"]
    logging.debug("\tFIFOMode = %#04x (%s)" % (cfg.FIFOMode, fifoMode[cfg.FIFOMode]))
	
    channelConfig = ["4 Channels", "2 Channels", "1 Channel", "1 OUT Pipe", "1 IN Pipe"]
    logging.debug("\tChannelConfig = %#04x (%s)" % (cfg.ChannelConfig, channelConfig[cfg.ChannelConfig]))
	
    logging.debug("\tOptionalFeatureSupport = %#06x" % cfg.OptionalFeatureSupport)
    logging.debug("\t\tBatteryChargingEnabled  : %d" % 
        ((cfg.OptionalFeatureSupport & _ft.FT_CONFIGURATION_OPTIONAL_FEATURE_ENABLEBATTERYCHARGING) >> 0) )
    logging.debug("\t\tDisableCancelOnUnderrun : %d" % 
        ((cfg.OptionalFeatureSupport & _ft.FT_CONFIGURATION_OPTIONAL_FEATURE_DISABLECANCELSESSIONUNDERRUN) >> 1) )
	
    logging.debug("\t\tNotificationEnabled     : %d %d %d %d" %
	    (((cfg.OptionalFeatureSupport & _ft.FT_CONFIGURATION_OPTIONAL_FEATURE_ENABLENOTIFICATIONMESSAGE_INCH1) >> 2),
        ((cfg.OptionalFeatureSupport & _ft.FT_CONFIGURATION_OPTIONAL_FEATURE_ENABLENOTIFICATIONMESSAGE_INCH2) >> 3),
        ((cfg.OptionalFeatureSupport & _ft.FT_CONFIGURATION_OPTIONAL_FEATURE_ENABLENOTIFICATIONMESSAGE_INCH3) >> 4),
        ((cfg.OptionalFeatureSupport & _ft.FT_CONFIGURATION_OPTIONAL_FEATURE_ENABLENOTIFICATIONMESSAGE_INCH4) >> 5) ))
		
    logging.debug("\t\tUnderrunEnabled         : %d %d %d %d" %
        (((cfg.OptionalFeatureSupport & _ft.FT_CONFIGURATION_OPTIONAL_FEATURE_DISABLEUNDERRUN_INCH1) >> 6),
        ((cfg.OptionalFeatureSupport & _ft.FT_CONFIGURATION_OPTIONAL_FEATURE_DISABLEUNDERRUN_INCH2) >> 7),
        ((cfg.OptionalFeatureSupport & _ft.FT_CONFIGURATION_OPTIONAL_FEATURE_DISABLEUNDERRUN_INCH3) >> 8),
        ((cfg.OptionalFeatureSupport & _ft.FT_CONFIGURATION_OPTIONAL_FEATURE_DISABLEUNDERRUN_INCH4) >> 9) ))
		
    logging.debug("\t\tEnableFifoInSuspend     : %d" % 
        ((cfg.OptionalFeatureSupport & _ft.FT_CONFIGURATION_OPTIONAL_FEATURE_SUPPORT_ENABLE_FIFO_IN_SUSPEND) >> 10) )
    logging.debug("\t\tDisableChipPowerdown    : %d" % 
        ((cfg.OptionalFeatureSupport & _ft.FT_CONFIGURATION_OPTIONAL_FEATURE_SUPPORT_DISABLE_CHIP_POWERDOWN) >> 11) )
    logging.debug("\tBatteryChargingGPIOConfig = %#02x" % cfg.BatteryChargingGPIOConfig)
	
    logging.debug("\tFlashEEPROMDetection = %#02x (read-only)" % cfg.FlashEEPROMDetection)
    logging.debug("\t\tCustom Config Validity  : %s" % 
        ("Invalid" if (cfg.FlashEEPROMDetection & (1<<_ft.FT_CONFIGURATION_FLASH_ROM_BIT_CUSTOMDATA_INVALID)) else "Valid") )
    logging.debug("\t\tCustom Config Checksum  : %s" % 
        ("Invalid" if (cfg.FlashEEPROMDetection & (1<<_ft.FT_CONFIGURATION_FLASH_ROM_BIT_CUSTOMDATACHKSUM_INVALID)) else "Valid") )
    logging.debug("\t\tGPIO Input              : %s" % 
        ("Used" if (cfg.FlashEEPROMDetection & (1<<_ft.FT_CONFIGURATION_FLASH_ROM_BIT_GPIO_INPUT)) else "Ignore") )
    if (cfg.FlashEEPROMDetection & (1<<_ft.FT_CONFIGURATION_FLASH_ROM_BIT_GPIO_INPUT)):
        logging.debug("\t\tGPIO 0                  : %s" % 
            ("High" if (cfg.FlashEEPROMDetection & (1<<_ft.FT_CONFIGURATION_FLASH_ROM_BIT_GPIO_0)) else "Low") )
        logging.debug("\t\tGPIO 1                  : %s" % 
            ("High" if (cfg.FlashEEPROMDetection & (1<<_ft.FT_CONFIGURATION_FLASH_ROM_BIT_GPIO_1)) else "Low") )
    logging.debug("\t\tConfig Used             : %s" % 
        ("Custom" if (cfg.FlashEEPROMDetection & (1<<_ft.FT_CONFIGURATION_FLASH_ROM_BIT_CUSTOM)) else "Default") )
		
    logging.debug("\tMSIO_Control = %#010x" % cfg.MSIO_Control)
    logging.debug("\tGPIO_Control = %#010x" % cfg.GPIO_Control)
    logging.debug("")


def DemoGetChipConfiguration(bDisplay=True):

    if sys.platform == 'linux':
        DemoTurnOffPipeThreads()

    D3XX = ftd3xx.create(0, _ft.FT_OPEN_BY_INDEX)
    if D3XX is None:
        logging.debug("ERROR: Please check if another D3XX application is open!")
        return False
		
    # get and display current chip configuration
    logging.debug("get current chip configuration")
    cfg = D3XX.getChipConfiguration()
    DisplayChipConfiguration(cfg)

    D3XX.close()
    D3XX = 0

    return True

	
def DemoResetChipConfiguration(bDisplay=True):

    if bDisplay == True:
        logging.debug("reset chip configuration")

    if sys.platform == 'linux':
        DemoTurnOffPipeThreads()
	
    # set default chip configuration
    D3XX = ftd3xx.create(0, _ft.FT_OPEN_BY_INDEX)
    if D3XX is None:
        logging.debug("ERROR: Please check if another D3XX application is open!")
        return False

    # Hack: Reset it to some decent config..
    cfg = D3XX.getChipConfiguration()
    cfg.ProductID = 0x601e
    cfg.bInterval = 0x09
    cfg.PowerAttributes = 0xe0
    cfg.PowerConsumption = 0x60
    cfg.Reserved2 = 0x00
    cfg.FIFOClock = _ft.FT_CONFIGURATION_FIFO_CLK_100
    # cfg.FIFOClock = _ft.FT_CONFIGURATION_FIFO_CLK_66
    # cfg.FIFOClock = _ft.FT_CONFIGURATION_FIFO_CLK_50
    # cfg.FIFOClock = _ft.FT_CONFIGURATION_FIFO_CLK_40
    cfg.FIFOMode = _ft.FT_CONFIGURATION_FIFO_MODE_245
    cfg.ChannelConfig = _ft.FT_CONFIGURATION_CHANNEL_CONFIG_1
    cfg.OptionalFeatureSupport = 0x03c2
    cfg.BatteryChargingGPIOConfig = 0xe4
    cfg.MSIO_Control = 0x00010800

    D3XX.setChipConfiguration(cfg)
    D3XX.close(True)
    D3XX = 0

    # wait until device has reenumerated
    DemoWaitForDeviceReenumeration()
		
    # reopen to display chip configuration
    if bDisplay == True:
        if sys.platform == 'linux':
            DemoTurnOffPipeThreads()
        D3XX = ftd3xx.create(0, _ft.FT_OPEN_BY_INDEX)
        if D3XX is None:
            logging.debug("ERROR: Please check if another D3XX application is open!")
            return False		
        cfg = D3XX.getChipConfiguration()
        DisplayChipConfiguration(cfg)
        D3XX.close()
        D3XX = 0
	
    return True

	
def DemoModifyChipConfiguration():

    if sys.platform == 'linux':
        DemoTurnOffPipeThreads()

    D3XX = ftd3xx.create(0, _ft.FT_OPEN_BY_INDEX)
    if D3XX is None:
        logging.debug("ERROR: Please check if another D3XX application is open!")
        return False
		
    # get and display current chip configuration
    logging.debug("get and modify current chip configuration")
    cfg = D3XX.getChipConfiguration()
    DisplayChipConfiguration(cfg)
	
    # modify chip configuration
    Manufacturer = "ManufacturerMod"
    ProductDescription = "ProductDescriptionMod"
    SerialNumber = "SerialNumberMod"
    newCfg = cfg
    SetInfoForStringDescriptor(newCfg, Manufacturer, ProductDescription, SerialNumber)
    D3XX.setChipConfiguration(newCfg)	
    D3XX.close(True)
    D3XX = 0
	
    # wait until device has reenumerated
    DemoWaitForDeviceReenumeration()
	
    # reopen to display current chip configuration
    logging.debug("get new chip configuration")
    if sys.platform == 'linux':
        DemoTurnOffPipeThreads()
    D3XX = ftd3xx.create(0, _ft.FT_OPEN_BY_INDEX)
    if D3XX is None:
        logging.debug("ERROR: Please check if another D3XX application is open!")
        return False	
    readCfg = D3XX.getChipConfiguration()
    DisplayChipConfiguration(readCfg)
    STRDESC = GetInfoFromStringDescriptor(readCfg.StringDescriptors)
		
    D3XX.close()
    D3XX = 0
	
    return True

	
def DemoSetChipConfiguration():

    if sys.platform == 'linux':
        DemoTurnOffPipeThreads()

    D3XX = ftd3xx.create(0, _ft.FT_OPEN_BY_INDEX)
    if D3XX is None:
        logging.debug("ERROR: Please check if another D3XX application is open!")
        return False
		
    # set chip configuration without using getChipConfiguration()
    logging.debug("set chip configuration without using getChipConfiguration")
	
    cfg = _ft.FT_60XCONFIGURATION()
    Manufacturer = "ManufacturerSet"
    ProductDescription = "ProductDescriptionSet"
    SerialNumber = "SerialNumberSet"
    SetInfoForStringDescriptor(cfg, Manufacturer, ProductDescription, SerialNumber)
    cfg.VendorID = _ft.FT_CONFIGURATION_DEFAULT_VENDORID
    cfg.ProductID = _ft.FT_CONFIGURATION_DEFAULT_PRODUCTID_601
    cfg.bInterval = _ft.FT_CONFIGURATION_DEFAULT_INTERRUPT_INTERVAL
    cfg.PowerAttributes = _ft.FT_CONFIGURATION_DEFAULT_POWERATTRIBUTES
    cfg.PowerConsumption = _ft.FT_CONFIGURATION_DEFAULT_POWERCONSUMPTION
    cfg.Reserved2 = 0
    cfg.FIFOClock = _ft.FT_CONFIGURATION_DEFAULT_FIFOCLOCK
    cfg.FIFOMode = _ft.FT_CONFIGURATION_DEFAULT_FIFOMODE
    cfg.ChannelConfig = _ft.FT_CONFIGURATION_DEFAULT_CHANNELCONFIG
    cfg.OptionalFeatureSupport = _ft.FT_CONFIGURATION_DEFAULT_OPTIONALFEATURE
    cfg.BatteryChargingGPIOConfig = _ft.FT_CONFIGURATION_DEFAULT_BATTERYCHARGING
    cfg.FlashEEPROMDetection = _ft.FT_CONFIGURATION_DEFAULT_FLASHDETECTION
    cfg.MSIO_Control = _ft.FT_CONFIGURATION_DEFAULT_MSIOCONTROL
    cfg.GPIO_Control = _ft.FT_CONFIGURATION_DEFAULT_GPIOCONTROL

    DisplayChipConfiguration(cfg)
    D3XX.setChipConfiguration(cfg)

    D3XX.close(True)
    D3XX = 0
	
    # wait until device has reenumerated
    DemoWaitForDeviceReenumeration()
	
    # reopen to display current chip configuration
    logging.debug("get new chip configuration")
    if sys.platform == 'linux':
        DemoTurnOffPipeThreads()
    D3XX = ftd3xx.create(0, _ft.FT_OPEN_BY_INDEX)
    if D3XX is None:
        logging.debug("ERROR: Please check if another D3XX application is open!")
        return False	
    readCfg = D3XX.getChipConfiguration()
    DisplayChipConfiguration(readCfg)
    D3XX.close()
    D3XX = 0
	
    return True
	

def DemoChipConfiguration():

    # result = DemoGetChipConfiguration()
    # if result == True:
    #     result = DemoSetChipConfiguration()
    # if result == True:
    #     result = DemoResetChipConfiguration()	
    # if result == True:
    #     result = DemoGetChipConfiguration()
    # if result == True:
    #     result = DemoModifyChipConfiguration()
    # if result == True:
    result = DemoResetChipConfiguration()
    # if result == True:
        # result = DemoGetChipConfiguration()

    return result


def DemoTransfer():

    if sys.platform == 'win32':

        # abort transfer test
        result = DemoAbortTransfer()

        # loopback in streaming and non-streaming mode
        if result == True:
            result = DemoLoopback(True)
        if result == True:
            result = DemoLoopback(False)

    elif sys.platform == 'linux':

        result = DemoLoopback()

    return result
	

def DemoLoopback(bStreamingMode=False):

    result = True
    channel = 0
    if sys.platform == 'linux':
        epout = channel	
        epin = channel	
    else:
        epout = 0x02 + channel	
        epin = 0x82 + channel	
    size = 4096
	
    logging.debug("Write/read synchronous loopback of string")
    D3XX = ftd3xx.create(0, _ft.FT_OPEN_BY_INDEX)
    if D3XX is None:
        logging.debug("ERROR: Please check if another D3XX application is open!")
        return False
	
    # enable streaming mode
    if bStreamingMode and sys.platform == 'linux':
        D3XX.setStreamPipe(epout, size)
        D3XX.setStreamPipe(epin, size)	
    
    # if python 2.7.12
    if sys.version_info.major == 2:		
		
        for x in range(0, 10):
	
            buffwrite = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(size))
            bytesWritten = D3XX.writePipe(epout, buffwrite, size)

            bytesRead = 0
            buffread = ""
            while (bytesRead < bytesWritten):
                output = D3XX.readPipeEx(epin, bytesWritten - bytesRead)
                bytesRead += output['bytesTransferred']
                buffread += output['bytes']
			
            # compare data
            compare = True
            if (buffread[:bytesRead] != buffwrite[:bytesWritten]):
                compare = False
            logging.debug("[%d] writePipe [%d] bytes, readPipe [%d] bytes, compare = %s" % 
                (x, bytesWritten, bytesRead, compare))
            if compare == False:
                result = False		
                break

    # elif python 3.5.2
    # version 3 does not support implicit bytes to string conversion	
    elif sys.version_info.major == 3:
	
        # flush old crap out first
        D3XX.readPipeEx(epin, size, raw=True, timeout=0)

        for x in range(0, 10):
	
            buffwrite = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(size))
            # text4k = '0123456789ABCDEF' * (4096 // 16)
            # buffwrite = ('<START %02d>' % x) + text4k[:-29] + '<qwerty_END_asdfgh>'
            # buffwrite = (chr(ord('A') + x) * 10) + text4k[:-20] + (chr(ord('a') + x) * 10)
            # buffwrite = (chr(ord('A') + x) * 10) + text4k[:-20] + (chr(ord('a') + x) * 10)
            buffwrite = buffwrite.encode('latin1')
            bytesWritten = D3XX.writePipe(epout, buffwrite, size)

            bytesRead = 0
            buffread = bytes()
            while (bytesRead < bytesWritten):
                output = D3XX.readPipeEx(epin, bytesWritten - bytesRead, raw=True, timeout=0)
                bytesRead += output['bytesTransferred']
                buffread += output['bytes']

            # compare data
            compare = True
            logging.debug(buffwrite[:bytesWritten])
            logging.debug(buffread[:bytesRead])
            if (buffread[:bytesRead] != buffwrite[:bytesWritten]):
                compare = False
            logging.debug("[%d] writePipe [%d] bytes, readPipe [%d] bytes, compare = %s" % 
                (x, bytesWritten, bytesRead, compare))
            if compare == False:
                result = False		
                break
				
    # disable streaming mode
    if bStreamingMode and sys.platform == 'linux':
        D3XX.clearStreamPipe(epout)
        D3XX.clearStreamPipe(epin)
	
    D3XX.close()
    D3XX = 0
    logging.debug("")
	
    return result
	
	
def DemoAbortThread(arg):

    logging.debug("DemoAbortThread\n")
    time.sleep(1)
    logging.debug("abortPipe")
    arg.abortPipe(0x82)

    return True

	
def DemoAbortTransfer():
	
    logging.debug("Abort transfer")
    D3XX = ftd3xx.create(0, _ft.FT_OPEN_BY_INDEX)
    if D3XX is None:
        logging.debug("ERROR: Please check if another D3XX application is open!")
        return False
		
    thread = threading.Thread(target = DemoAbortThread, args = (D3XX, ))
    thread.start()
	
    # readpipe is blocking when overlapped parameter is not set
    # it will be unblocked by the thread DemoAbortThread 
    logging.debug("readPipe")
    D3XX.setPipeTimeout(0x82, 0)
    D3XX.readPipeEx(0x82, 1024)
    thread.join()

    D3XX.close()
    D3XX = 0
    logging.debug("")

    return True

	
def EnableNotificationFeature(bEnable):

    D3XX = ftd3xx.create(0, _ft.FT_OPEN_BY_INDEX)
    if D3XX is None:
        logging.debug("ERROR: Please check if another D3XX application is open!")
        return False
		
    # get and display current chip configuration
    cfg = D3XX.getChipConfiguration()
    #DisplayChipConfiguration(cfg)

    # enable or disable notification for 1st channel
    if bEnable:
        cfg.OptionalFeatureSupport |= _ft.FT_CONFIGURATION_OPTIONAL_FEATURE_ENABLENOTIFICATIONMESSAGE_INCH1;
        cfg.Interval = _ft.FT_CONFIGURATION_DEFAULT_INTERRUPT_INTERVAL;
    else:
        cfg.OptionalFeatureSupport &= ~_ft.FT_CONFIGURATION_OPTIONAL_FEATURE_ENABLENOTIFICATIONMESSAGE_INCH1;	
    #DisplayChipConfiguration(cfg)
    D3XX.setChipConfiguration(cfg)
    D3XX.close()
    D3XX = 0
	
    # wait until device has reenumerated
    DemoWaitForDeviceReenumeration()

    # display the chip configuration
    D3XX = ftd3xx.create(0, _ft.FT_OPEN_BY_INDEX)
    if D3XX is None:
        logging.debug("ERROR: Please check if another D3XX application is open!")
        return False	
    cfg = D3XX.getChipConfiguration()
    DisplayChipConfiguration(cfg)
    D3XX.close()
    D3XX = 0
    if bEnable and not (cfg.OptionalFeatureSupport & _ft.FT_CONFIGURATION_OPTIONAL_FEATURE_ENABLENOTIFICATIONMESSAGE_INCH1):
        return False	
	
    return True
	



def DemoNotificationTransfer():
	
    logging.debug("enable notification feature on channel 1")
    EnableNotificationFeature(True)
	
    D3XX = ftd3xx.create(0, _ft.FT_OPEN_BY_INDEX)
    if D3XX is None:
        logging.debug("ERROR: Please check if another D3XX application is open!")
        return False
	
    D3XX.setSuspendTimeout(0)
	
    logging.debug("Set notification event")
    eventCondition = threading.Event()
    eventCondition.ulRecvNotificationLength = int(0x0)
    eventCondition.ucEndpointNo = int(0x0)	
    D3XX.setNotificationCallback(eventCondition)
		
    buffwrite = bytearray(4096)
    logging.debug("writePipe %d" % len(buffwrite))
    buffwrite[:] = itertools.repeat(0xAA, len(buffwrite))
    #print binascii.hexlify(buffwrite)
    bytesWritten = D3XX.writePipe(0x02, str(buffwrite), len(buffwrite))
    bytesRead = 0
	
    while (bytesRead < bytesWritten):
        while not eventCondition.is_set():
            eventCondition.wait(1)
        ulRecvNotificationLength = eventCondition.ulRecvNotificationLength
        ucEndpointNo = eventCondition.ucEndpointNo
        #print "ulRecvNotificationLength %d ucEndpointNo %d"  % (ulRecvNotificationLength, ucEndpointNo)
        #readOutput = D3XX.readPipe(ucEndpointNo, ulRecvNotificationLength)
        readOutput = D3XX.readPipe(0x82, 512)
        bytesRead += readOutput['bytesTransferred']
        logging.debug("readPipe %d" % bytesRead)
        buffread = readOutput['bytes']

    logging.debug("clearNotificationCallback")
    D3XX.clearNotificationCallback()	
    D3XX.close()
    D3XX = 0
    logging.debug("")
	
    logging.debug("disable notification feature on channel 1")
    EnableNotificationFeature(False)

    return True


def DemoPipeTimeout():

    if sys.platform == 'linux':
        return True

    logging.debug("Get set pipe timeout")
    D3XX = ftd3xx.create(0, _ft.FT_OPEN_BY_INDEX)
    if D3XX is None:
        logging.debug("ERROR: Please check if another D3XX application is open!")
        return False
		
    pipe = 0x02
	
    # get timeout for pipe 0x02
    timeoutMS = D3XX.getPipeTimeout(pipe)
    logging.debug("default timeout = %d" % timeoutMS)

    # set desired timeout for pipe 0x02
    D3XX.setPipeTimeout(pipe, timeoutMS*2)
    logging.debug("set timeout = %d" % (timeoutMS*2))

    # verify if timeout changed
    timeoutMSNew = D3XX.getPipeTimeout(pipe)
    logging.debug("new timeout = %d" % timeoutMSNew)
    if (timeoutMSNew != timeoutMS*2):
        return False

    # revert to original timeout		
    D3XX.setPipeTimeout(pipe, timeoutMS)
    logging.debug("revert timeout = %d" % timeoutMS)

    D3XX.close()
    D3XX = 0

    return True

	
def DemoSuspendTimeout():

    if sys.platform == 'linux':
        return True

    logging.debug("Get set suspend timeout")
    D3XX = ftd3xx.create(0, _ft.FT_OPEN_BY_INDEX)
    if D3XX is None:
        logging.debug("ERROR: Please check if another D3XX application is open!")
        return False
		
    # get current timeout
    timeout = D3XX.getSuspendTimeout()
    logging.debug("default timeout = %d" % timeout)

    # set the desired timeout
    D3XX.setSuspendTimeout(timeout*2)
    logging.debug("set timeout = %d" % (timeout*2))

    # verify if timeout changed
    timeoutNew = D3XX.getSuspendTimeout()
    logging.debug("new timeout = %d" % timeoutNew)
    if (timeoutNew != timeout*2):
        return False

    # revert to original timeout
    D3XX.setSuspendTimeout(timeout)
    logging.debug("revert timeout = %d" % timeout)

    D3XX.close()
    D3XX = 0

    return True

	
def DemoCyclePort():

    # reset device port
    logging.debug("Reset device port")
    D3XX = ftd3xx.create(0, _ft.FT_OPEN_BY_INDEX)
    if D3XX is None:
        logging.debug("ERROR: Please check if another D3XX application is open!")
        return False
		
    D3XX.resetDevicePort()
    D3XX.close()
    D3XX = 0

    # wait until device has reenumerated
    DemoWaitForDeviceReenumeration()

    if sys.platform == 'win32':

        # cycle device port
        logging.debug("Cycle device port")
        D3XX = ftd3xx.create(0, _ft.FT_OPEN_BY_INDEX)
        if D3XX is None:
            logging.debug("ERROR: Please check if another D3XX application is open!")
            return False		
        D3XX.cycleDevicePort()
        D3XX.close()
        D3XX = 0

        # wait until device has reenumerated
        DemoWaitForDeviceReenumeration()	
	
    return True


def EnableBatteryChargingDetectionFeature(bEnable):

    D3XX = ftd3xx.create(0, _ft.FT_OPEN_BY_INDEX)
    if D3XX is None:
        logging.debug("ERROR: Please check if another D3XX application is open!")
        return False
		
    # get and display current chip configuration
    cfg = D3XX.getChipConfiguration()
    #DisplayChipConfiguration(cfg)

    # enable or disable battery charging detection
    # BatteryChargingGPIOConfig Default setting : 11100100b  (0xE4 - FT_CONFIGURATION_DEFAULT_BATTERYCHARGING) 
    # 7 - 6 : DCP = 11b         (GPIO1 = 1 GPIO0 = 1)
    # 5 - 4 : CDP = 10b         (GPIO1 = 1 GPIO0 = 0)
    # 3 - 2 : SDP = 01b         (GPIO1 = 0 GPIO0 = 1)
    # 1 - 0 : Unknown/Off = 00b (GPIO1 = 0 GPIO0 = 0)
    if bEnable:
        cfg.OptionalFeatureSupport |= _ft.FT_CONFIGURATION_OPTIONAL_FEATURE_ENABLEBATTERYCHARGING
        cfg.BatteryChargingGPIOConfig |= _ft.FT_CONFIGURATION_DEFAULT_BATTERYCHARGING
    else:
        cfg.OptionalFeatureSupport &= ~_ft.FT_CONFIGURATION_OPTIONAL_FEATURE_ENABLEBATTERYCHARGING
		
    #DisplayChipConfiguration(cfg)
    D3XX.setChipConfiguration(cfg)
    D3XX.close()
    D3XX = 0
	
    # wait until device has reenumerated
    DemoWaitForDeviceReenumeration()

    # verify the chip configuration
    D3XX = ftd3xx.create(0, _ft.FT_OPEN_BY_INDEX)
    if D3XX is None:
        logging.debug("ERROR: Please check if another D3XX application is open!")
        return False	
    cfg = D3XX.getChipConfiguration()
    DisplayChipConfiguration(cfg)
    D3XX.close()
    D3XX = 0
    if bEnable and not (cfg.OptionalFeatureSupport & _ft.FT_CONFIGURATION_OPTIONAL_FEATURE_ENABLEBATTERYCHARGING):
        return False
	
    return True


def DemoGpioBatteryCharging():

    logging.debug("enable battery charging detection feature")
    EnableBatteryChargingDetectionFeature(True)
	
    D3XX = ftd3xx.create(0, _ft.FT_OPEN_BY_INDEX)
    if D3XX is None:
        logging.debug("ERROR: Please check if another D3XX application is open!")
        return False
		
    mask = _ft.FT_GPIO_MASK_GPIO_0 | _ft.FT_GPIO_MASK_GPIO_1
	
    # enable gpio by setting gpio direction
    direction = (_ft.FT_GPIO_DIRECTION_OUT << _ft.FT_GPIO_0) | (_ft.FT_GPIO_DIRECTION_OUT << _ft.FT_GPIO_1)
    D3XX.enableGPIO(mask, direction)
	
    # read gpio
    # BatteryChargingGPIOConfig Default setting : 11100100b  (0xE4)
    # 7 - 6 : DCP = 11b         (GPIO1 = 1 GPIO0 = 1)
    # 5 - 4 : CDP = 10b         (GPIO1 = 1 GPIO0 = 0)
    # 3 - 2 : SDP = 01b         (GPIO1 = 0 GPIO0 = 1)
    # 1 - 0 : Unknown/Off = 00b (GPIO1 = 0 GPIO0 = 0)
    # Since device is connected to a host machine, then we should get SDP (GPIO1 = 0 GPIO0 = 1)
    bcdtype = ['UNKNOWN', 'SDP - Standard Downstream Port', 'CDP - Charging Downstream Port', 'DCP - Dedicated Charging Port']
    data = D3XX.readGPIO()
    logging.debug("detected battery charging type: [%s]" % bcdtype[data])
    logging.debug("")

    D3XX.close()
    D3XX = 0

    logging.debug("disable battery charging detection feature")
    EnableBatteryChargingDetectionFeature(False)
	
    return True


def DemoGpioSetGet():

    if sys.platform == 'linux':
        DemoTurnOffPipeThreads()

    D3XX = ftd3xx.create(0, _ft.FT_OPEN_BY_INDEX)
    if D3XX is None:
        logging.debug("ERROR: Please check if another D3XX application is open!")
        return False
		
    mask = _ft.FT_GPIO_MASK_GPIO_0 | _ft.FT_GPIO_MASK_GPIO_1

    # enable gpio by setting gpio direction
    direction = (_ft.FT_GPIO_DIRECTION_OUT << _ft.FT_GPIO_0) | (_ft.FT_GPIO_DIRECTION_OUT << _ft.FT_GPIO_1)
    D3XX.enableGPIO(mask, direction)
    logging.debug("enable gpio[gpio0: %d, gpio1: %d]" % 
        (direction & _ft.FT_GPIO_MASK_GPIO_0, (direction & _ft.FT_GPIO_MASK_GPIO_1) >> _ft.FT_GPIO_1))	
	
    # set gpio pull both high
    pull = (_ft.FT_GPIO_PULL_HIGH << _ft.FT_GPIO_0) | (_ft.FT_GPIO_PULL_HIGH << _ft.FT_GPIO_1)
    D3XX.setGPIOPull(mask, pull)
    logging.debug("pull  gpio [gpio0: %d, gpio1: %d]" % 
        (pull & _ft.FT_GPIO_MASK_GPIO_0, (pull & _ft.FT_GPIO_MASK_GPIO_1) >> _ft.FT_GPIO_1))

    # read gpio
    data = D3XX.readGPIO()
    logging.debug("read  gpio [gpio0: %d, gpio1: %d]" % 
        (data & _ft.FT_GPIO_MASK_GPIO_0, (data & _ft.FT_GPIO_MASK_GPIO_1) >> _ft.FT_GPIO_1))
	
    # write gpio both low
    data = (_ft.FT_GPIO_VALUE_LOW << _ft.FT_GPIO_0) | (_ft.FT_GPIO_VALUE_LOW << _ft.FT_GPIO_1)
    D3XX.writeGPIO(mask, data)
    logging.debug("write gpio [gpio0: %d, gpio1: %d]" % 
        (data & _ft.FT_GPIO_MASK_GPIO_0, (data & _ft.FT_GPIO_MASK_GPIO_1) >> _ft.FT_GPIO_1))

    # read gpio
    data = D3XX.readGPIO()
    logging.debug("read  gpio [gpio0: %d, gpio1: %d]" % 
        (data & _ft.FT_GPIO_MASK_GPIO_0, (data & _ft.FT_GPIO_MASK_GPIO_1) >> _ft.FT_GPIO_1))

    # write gpio both high
    data = (_ft.FT_GPIO_VALUE_HIGH << _ft.FT_GPIO_0) | (_ft.FT_GPIO_VALUE_HIGH << _ft.FT_GPIO_1)
    D3XX.writeGPIO(mask, data)
    logging.debug("write gpio [gpio0: %d, gpio1: %d]" % 
        (data & _ft.FT_GPIO_MASK_GPIO_0, (data & _ft.FT_GPIO_MASK_GPIO_1) >> _ft.FT_GPIO_1))

    # read gpio
    data = D3XX.readGPIO()
    logging.debug("read  gpio [gpio0: %d, gpio1: %d]" % 
        (data & _ft.FT_GPIO_MASK_GPIO_0, (data & _ft.FT_GPIO_MASK_GPIO_1) >> _ft.FT_GPIO_1))

    D3XX.close()
    D3XX = 0
    logging.debug("")
	
    return True

	
def DemoGpio():

    result = DemoGpioSetGet()
    
    if sys.platform == 'win32':
        if result == True:	
            result = DemoGpioBatteryCharging()

    return result


def GetOSVersion():

    if (sys.platform == 'win32'):
        verList = [("Windows 7", 6, 1), ("Windows 8", 6, 2), ("Windows 8.1", 6, 3), ("Windows 10", 10, 0)]
        ver = sys.getwindowsversion()
        elemList = [elem for index, elem in enumerate(verList) if ver.major == elem[1] and ver.minor == elem[2]]
        return elemList[0][0] if len(elemList) == 1 else os.getenv("OS")

    return os.uname()[0]


def GetOSArchitecture():

    if (sys.platform == 'win32'):
        return os.environ["PROCESSOR_ARCHITECTURE"]

    return platform.machine()


def GetComputername():

    if (sys.platform == 'win32'):
        return os.getenv('COMPUTERNAME')

    return platform.node()


def GetUsername():

    if (sys.platform == 'win32'):
        return os.getenv('USERNAME')

    import pwd
    return pwd.getpwuid(os.getuid())[0]


def main():

    # check connected devices
    numDevices = DemoGetNumDevicesConnected()	
    if (numDevices != 1):
        logging.debug("ERROR: Please check environment setup! %d device(s) detected." % numDevices)
        return False	

    # list the test cases
    testCases = [
        # (DemoEnumerateDevices,  "DemoEnumerateDevices"),
        # (DemoOpenDeviceBy,      "DemoOpenDeviceBy"),
        # (DemoVersions,          "DemoVersions"),
        # (DemoDescriptors,       "DemoDescriptors"),
        (DemoChipConfiguration, "DemoChipConfiguration"),
        (DemoTransfer,          "DemoTransfer"),
        # (DemoPipeTimeout,       "DemoPipeTimeout"),
        # (DemoSuspendTimeout,    "DemoSuspendTimeout"),
        # (DemoCyclePort,         "DemoCyclePort"),
        # (DemoGpio,              "DemoGpio"),
    ]
		
    # execute the test cases
    fails = success = 0	
    for test in testCases:

        logging.debug("--------------------------------------------------------------")
        logging.debug("%s" % test[1])
        logging.debug("--------------------------------------------------------------")
		
        start = datetime.datetime.now()
        logging.debug("Start time,%s" % start)
        logging.debug("")
		
        result = test[0]()
		
        stop = datetime.datetime.now()
        logging.debug("")
        logging.debug("Stop time,%s" % stop)
		
        if result == True:
            logging.debug("Status,SUCCESS")
            success += 1
        else:
            logging.debug("Status,FAILED")
            fails += 1
        logging.debug("")
        logging.debug("")

    # display summary count			
    logging.debug("--------------------------------------------------------------")
    logging.debug("Summary")
    logging.debug("--------------------------------------------------------------")
    logging.debug("Summary Log Counts,[ Fails (%d); Success (%d) ]" % (fails, success))
    logging.debug("")
    logging.debug("")

    if sys.platform == 'win32':
        DemoResetChipConfiguration(False)
	
    return fails == 0


if __name__ == "__main__":

    # initialize logging to log in both console and file
    logging.basicConfig(filename='apiusage.log', filemode='w',
        level=logging.DEBUG, format='[%(asctime)s] %(message)s')	
    logging.getLogger().addHandler(logging.StreamHandler())
	
    logging.debug("")
    logging.debug("**************************************************************")
    logging.debug("FT60X D3XX PYTHON API USAGE DEMO")
    logging.debug("WORKSTATION,%s" % GetComputername())
    logging.debug("OSVERSION,%s,%s" % (GetOSVersion(), GetOSArchitecture()))
    logging.debug("OPERATOR,%s" % GetUsername())
    logging.debug("DATE,%s" % datetime.datetime.now().strftime("%Y-%m-%d"))
    logging.debug("TIME,%s" % datetime.datetime.now().strftime("%H:%M:%S"))
    logging.debug("PYTHON,%d.%d.%d" % (sys.version_info.major, sys.version_info.minor, sys.version_info.micro))
    logging.debug("**************************************************************")
    logging.debug("")
    logging.debug("")
    logging.debug("")
    logging.debug("")
	
    main()  


