import ftd3xx
import sys
if sys.platform == 'win32':
    import ftd3xx._ftd3xx_win32 as _ft
elif sys.platform == 'linux':
    import ftd3xx._ftd3xx_linux as _ft
import datetime
import time
import ctypes
import logging
import os
import platform
import argparse



def GetNumDevicesConnected():

    DEVICES = ftd3xx.listDevices()
    return len(DEVICES) if DEVICES is not None else 0


def WaitForDeviceReenumeration():

    # should be called when setChipConfiguration, cycleDevicePort or resetDevicePort is called
    # todo: get optimal sleep times
    origValue = ftd3xx.raiseExceptionOnError(False)
    time.sleep(1)
    while (ftd3xx.listDevices() == None):
        time.sleep(1)
    time.sleep(1)
    ftd3xx.raiseExceptionOnError(origValue)


def TurnOffPipeThreads():

    conf = _ft.FT_TRANSFER_CONF();
    conf.wStructSize = ctypes.sizeof(_ft.FT_TRANSFER_CONF);
    conf.pipe[_ft.FT_PIPE_DIR_IN].fPipeNotUsed = True;
    conf.pipe[_ft.FT_PIPE_DIR_OUT].fPipeNotUsed = True;
    conf.pipe.fReserved = False;
    conf.pipe.fKeepDeviceSideBufferAfterReopen = False;
    for i in range(4):
        ftd3xx.setTransferParams(conf, i);

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
    manufacturer = bytearray(manufacturer)
    productDescription = bytearray(productDescription)
    serialNumber = bytearray(serialNumber)
	
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

    fifoClock = ["100 MHz", "66 MHz"]	
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


def GetChipConfiguration(bDisplay=True):

    if sys.platform == 'linux':
        TurnOffPipeThreads()
        ftd3xx.createDeviceInfoList()
        ftd3xx.getDeviceInfoList()

    D3XX = ftd3xx.create(0, _ft.FT_OPEN_BY_INDEX)
    if D3XX is None:
        logging.debug("ERROR: Please check if another D3XX application is open!")
        return None
		
    # get and display current chip configuration
    cfg = D3XX.getChipConfiguration()
    if bDisplay == True and cfg != None:
        DisplayChipConfiguration(cfg)

    D3XX.close()
    D3XX = 0

    return cfg


def SetChipConfiguration(cfg=None, bDisplay=False):

    if sys.platform == 'linux':
        TurnOffPipeThreads()
        ftd3xx.createDeviceInfoList()
        ftd3xx.getDeviceInfoList()

    D3XX = ftd3xx.create(0, _ft.FT_OPEN_BY_INDEX)
    if D3XX is None:
        logging.debug("ERROR: Please check if another D3XX application is open!")
        return False

    if bDisplay == True and cfg != None:
        DisplayChipConfiguration(cfg)		
    D3XX.setChipConfiguration(cfg)

    D3XX.close()
    D3XX = 0
	
    WaitForDeviceReenumeration()		
    return True


def GetLogPath(fileName):

    logPath = ""
    if sys.platform == 'linux':
        logPath = os.path.dirname(__file__) + "/" + fileName
    elif sys.platform == 'win32':
        logPath = os.path.dirname(__file__) + "\\" + fileName

    return logPath


def WriteFile(logPath, strBuffer):

    fileObject = open(logPath, "w")
    fileObject.write(strBuffer)	
    fileObject.close()

    return True


def ReadFile(logPath):

    lineList = []
    fileObject = open(logPath, "r")
    for line in fileObject:
        lineList.append(line)	
    fileObject.close()

    return lineList


def SaveChipConfiguration(filename, cfg):

    # determine the log path
    logPath = GetLogPath(filename)

    # save configuration details into a string
    strBuffer = ""
    strBuffer += "VendorID=0x{0:04x}\r\n".format(cfg.VendorID)
    strBuffer += "ProductID=0x{0:04x}\r\n".format(cfg.ProductID)
    STRDESC = GetInfoFromStringDescriptor(cfg.StringDescriptors)
    strBuffer += "Manufacturer={0}\r\n".format(STRDESC['Manufacturer'])
    strBuffer += "ProductDescription={0}\r\n".format(STRDESC['ProductDescription'])
    strBuffer += "SerialNumber={0}\r\n".format(STRDESC['SerialNumber'])
    strBuffer += "InterruptInterval=0x{0:02x}\r\n".format(cfg.bInterval)
    strBuffer += "PowerAttributes=0x{0:02x}\r\n".format(cfg.PowerAttributes)
    strBuffer += "PowerConsumption=0x{0:02x}\r\n".format(cfg.PowerConsumption)
    strBuffer += "FIFOClock=0x{0:02x}\r\n".format(cfg.FIFOClock)
    strBuffer += "FIFOMode=0x{0:02x}\r\n".format(cfg.FIFOMode)
    strBuffer += "ChannelConfig=0x{0:02x}\r\n".format(cfg.ChannelConfig)
    strBuffer += "OptionalFeatureSupport=0x{0:04x}\r\n".format(cfg.OptionalFeatureSupport)
    strBuffer += "BatteryChargingGPIOConfig=0x{0:02x}\r\n".format(cfg.BatteryChargingGPIOConfig)
    strBuffer += "MSIOControl=0x{0:08x}\r\n".format(cfg.MSIO_Control)
    strBuffer += "GPIOControl=0x{0:08x}".format(cfg.GPIO_Control)
	
    # write to file
    WriteFile(logPath, strBuffer)

    #logging.debug("%s" % logPath)	
    #logging.debug("%s" % strBuffer)
	
    return logPath


def LoadChipConfiguration(filename, cfg):

    # determine the log path
    logPath = GetLogPath(filename)

    # read from file to a list of line
    lineList = ReadFile(logPath)
	
    # parse string into a cfg structure
    Manufacturer = ""
    ProductDescription = ""
    SerialNumber = ""
    newCfg = _ft.FT_60XCONFIGURATION()
    for line in lineList:
        if (line != "\r\n"):
            a,b=line.split("=")
            a=a.strip()
            b=b.strip()
            #logging.debug("[%s] [%s]" % (a, b))
            if a == "VendorID":
                newCfg.VendorID = int(b, 16)
                if (newCfg.VendorID != cfg.VendorID):
                    logging.debug("Note: Changing VID requires changing Windows Driver INF or Linux udev rules")
                    logging.debug("Note: Original VID will be used")
                    logging.debug("Note: Please update code if you really know what you are doing")
                    logging.debug("")
                    newCfg.VendorID = cfg.VendorID
            elif a == "ProductID":
                newCfg.ProductID = int(b, 16)
                if (newCfg.ProductID != cfg.ProductID):
                    logging.debug("Note: Changing PID requires changing Windows Driver INF or Linux udev rules")
                    logging.debug("Note: Original PID will be used")				
                    logging.debug("Note: Please update code if you really know what you are doing")
                    logging.debug("")
                    newCfg.ProductID = cfg.ProductID
            elif a == "Manufacturer":
                Manufacturer = b
            elif a == "ProductDescription":
                ProductDescription = b
            elif a == "SerialNumber":
                SerialNumber = b
            elif a == "InterruptInterval":
                newCfg.bInterval = int(b, 16)
            elif a == "PowerAttributes":
                newCfg.PowerAttributes = int(b, 16)
            elif a == "PowerConsumption":
                newCfg.PowerConsumption = int(b, 16)
            elif a == "FIFOClock":
                newCfg.FIFOClock = int(b, 16)
            elif a == "FIFOMode":
                newCfg.FIFOMode = int(b, 16)
            elif a == "ChannelConfig":
                newCfg.ChannelConfig = int(b, 16)
            elif a == "OptionalFeatureSupport":
                newCfg.OptionalFeatureSupport = int(b, 16)
            elif a == "BatteryChargingGPIOConfig":
                newCfg.BatteryChargingGPIOConfig = int(b, 16)
            elif a == "MSIOControl":
                newCfg.MSIO_Control = int(b, 16)
            elif a == "GPIOControl":
                newCfg.GPIO_Control = int(b, 16)
            else:
                logging.debug("Invalid parameter found in file: %s=%s" % (a, b))			
                return None
    SetInfoForStringDescriptor(newCfg, Manufacturer, ProductDescription, SerialNumber)					
	
    return newCfg


def main(output, input, reset):

    logging.debug("INPUT: outputFileName=[%s], inputFileName=[%s], resetChipConfiguration=%s" % (output, input, reset))
    logging.debug("")
    logging.debug("")
	
    # check connected devices
    numDevices = GetNumDevicesConnected()	
    if (numDevices != 1):
        logging.debug("ERROR: Please check environment setup! %d device(s) detected." % numDevices)
        return False	

    if reset == True:
        # display current configuration
        cfg = GetChipConfiguration()
        if (cfg == None):
            return False
		
        # prompt user to continue setting the chip configuration to the device
        while True:
            proceed = raw_input("Do you want to proceed reseting configuration? [Y/N] ")
            if (proceed != 'Y' and proceed != 'N'):
                continue
            if (proceed == 'Y'):
                result = SetChipConfiguration()
                if (result == False):
                    logging.debug("Resetting chip configuration failed!")
            break
		
    elif output == "" and input == "":
        # display current configuration	
        cfg = GetChipConfiguration()
        if (cfg == None):
            return False

    elif output != "":	
        # display current configuration	
        cfg = GetChipConfiguration()
        if (cfg == None):
            return False

        # save current configuration into the specified file
        logPath = SaveChipConfiguration(output, cfg)
        if (logPath != ""):
            logging.debug("Current chip configuration has been saved to %s" % output)	 		
            logging.debug("%s" % logPath)	 		

    elif input != "":
        # display current configuration	
        cfg = GetChipConfiguration(False)
        if (cfg == None):
            return False
			
        # read file and parse to get chip configuration structure	
        cfg = LoadChipConfiguration(input, cfg)		
        if (cfg != None):
            DisplayChipConfiguration(cfg)
            
            # prompt user to continue setting the chip configuration to the device
            while True:
                proceed = raw_input("Do you want to proceed updating configuration? [Y/N] ")
                if (proceed != 'Y' and proceed != 'N'):
                    continue
                if (proceed == 'Y'):
                    result = SetChipConfiguration(cfg)
                    if (result == False):
                        logging.debug("Setting chip configuration failed!")
                break

    logging.debug("")		
    logging.debug("")		
    return True


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


if __name__ == "__main__":

    # initialize logging to log in both console and file
    logging.basicConfig(filename='chipconfiguration.log', filemode='a',
        level=logging.DEBUG, format='[%(asctime)s] %(message)s')	
    logging.getLogger().addHandler(logging.StreamHandler())
	
    logging.debug("")
    logging.debug("**************************************************************")
    logging.debug("FT60X D3XX CHIP CONFIGURATION UTIL")
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
	
    logging.debug("USAGE: chipconfiguration.py [-h] [-o OUTPUTFILE] [-i INPUTFILE] [--reset]")
    logging.debug("")

    # sample usage: 
    # chipconfiguration.py				- display device chip configuration
    # chipconfiguration.py -o save.txt	- save device chip configuration into save.txt
    # chipconfiguration.py -i load.txt	- load device chip configuration from load.txt
    # chipconfiguration.py --reset	    - reset device chip configuration
	
    # parse commandline arguments		
    parser = argparse.ArgumentParser(description="chip configuration demo application")
    parser.add_argument('-o', '--output', default="", help="save device chip configuration to specified file")
    parser.add_argument('-i', '--input', default="", help="set device chip configuration from specified file")
    parser.add_argument('--reset', action="store_true", help="reset device to default chip configuration")
    args = parser.parse_args()

    main(args.output, args.input, args.reset)


