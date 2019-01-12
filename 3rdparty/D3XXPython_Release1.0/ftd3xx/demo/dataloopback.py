import ftd3xx
import sys
if sys.platform == 'win32':
    import ftd3xx._ftd3xx_win32 as _ft
elif sys.platform == 'linux':
    import ftd3xx._ftd3xx_linux as _ft
if sys.version_info.major == 3:
    import queue
elif sys.version_info.major == 2:
    import Queue as queue
import datetime
import time
import timeit
import binascii
import itertools
import ctypes
import threading
import logging
import os
import platform
import argparse
import random
import string



def CreateLogFile(logFile, logBuffer, bAppend=False):

    fileObject = open(logFile, "w" if bAppend==False else "a")
    fileObject.write(str(logBuffer))	
    fileObject.close()


def CreateLogDirectory():

    if sys.platform == 'linux':
        logDirectory = os.path.dirname(__file__) + "/dataloopback_output/"
    elif sys.platform == 'win32':
        logDirectory = os.path.dirname(__file__) + "\\dataloopback_output\\"	
    if not os.path.exists(logDirectory):
        os.makedirs(logDirectory)

    return logDirectory


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


def DisplayTroubleshootingGuide(operation, devList, devIndex, cfg):

    fifoClock = ["100MHz", "66MHz"]
    fifoMode = ["245Mode", "600Mode"]
    ft60XType = "FT" + str(devList[devIndex].Type) + (" (32bit)" if devList[devIndex].Type == 601 else " (16bit)")
    logging.debug("NOTE: FPGA device should be using the %s sample for %s %s %s." %
        (operation, "FT" + str(devList[devIndex].Type), fifoClock[cfg.FIFOClock], fifoMode[cfg.FIFOMode]) )
    logging.debug("If test fails or hangs, below is the basic troubleshooting guide:")
    logging.debug("1) Unplug/plug device.");
    logging.debug("2) No other D3XX application is open.");
    logging.debug("3) FPGA image is for %s. And chip is configured using same mode." % fifoMode[cfg.FIFOMode])
    logging.debug("4) FPGA image is for %s. And PCB module has matching architecture." % ft60XType)
    logging.debug("5) Jumpers and switches are set correctly on FPGA and PCB module.")
    logging.debug("");


def DisplayDeviceList(numDevices, devList):

    for i in range(numDevices):
        logging.debug("DEVICE[%d]" % i)
        logging.debug("\tFlags = %d" % devList[i].Flags)
        logging.debug("\tType = %d" % devList[i].Type)
        logging.debug("\tID = %#010X" % devList[i].ID)
        logging.debug("\tLocId = %d" % devList[i].LocId)
        logging.debug("\tSerialNumber = %s" % devList[i].SerialNumber.decode('utf-8'))
        logging.debug("\tDescription = %s" % devList[i].Description.decode('utf-8'))


def DisplayVersions(D3XX):

    logging.debug("Library Version: %#08X" % D3XX.getLibraryVersion())	
    logging.debug("Driver Version: %#08X" % D3XX.getDriverVersion())	
    logging.debug("Firmware Version: %#08X" % D3XX.getFirmwareVersion())	


def SelectDevice(numDevices):

    index = 0
    if numDevices == 1:
        return index

    # prompt user to select the index of the device to test
    while True:
        index = input("Select the index of the device to test (0-{0}): ".format(numDevices))
        try:
            index = int(index)
        except:
            continue		
        if (index >= numDevices):
            continue
        break

    logging.debug("Device at index %d will be used." % index)	
    logging.debug("")
    return index


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


def WritePipe(D3XX, pipe, buffer, size):

    if sys.platform == 'linux':
        pipe -= 0x02

    return D3XX.writePipe(pipe, buffer, size)


def ReadPipe(D3XX, pipe, size):

    if sys.platform == 'linux':
        pipe -= 0x82

    return D3XX.readPipeEx(pipe, size)


def CancelPipe(D3XX, pipe):

    if sys.platform == 'linux':
        return D3XX.flushPipe(pipe)

    return D3XX.abortPipe(pipe)


def WriterThreadFunc(D3XX, pipe, buffer, size, file):

    transferred = 0

    if sys.version_info.major == 3:
        buffer = buffer.encode('latin1')
		
    while (transferred != size):

        # write data to specified pipe	
        transferred += WritePipe(D3XX, pipe, buffer, size - transferred)
        logging.debug("Write[%#04X] bytesTransferred %d" % (pipe, transferred))
		
        # check status of writing data
        status = D3XX.getLastError()	
        if (status != 0):
            logging.debug("Write[%#04X] error status %d (%s)" %
                (pipe, status, ftd3xx.getStrError(status)))
            CancelPipe(D3XX, pipe)		
            break

    # write written data to log file			
    CreateLogFile(file, buffer)


def ReaderThreadFunc(D3XX, pipe, buffer, size, file, compare):

    # read data from specified pipe
    output = ReadPipe(D3XX, pipe, size)
    transferred = output['bytesTransferred']
	
    if sys.version_info.major == 3:
        buffer = buffer.encode('latin1')
        buffread = output['bytes'].decode('latin1')
    else:
        buffread = output['bytes']
			
    logging.debug("Read[%#04X] bytesTransferred %d" % (pipe, transferred))

    while (transferred != size):

        # check status of reading data	
        status = D3XX.getLastError()
        if (status != 0):
            logging.debug("Read[%#04X] error status %d (%s)" %
                (pipe, status, ftd3xx.getStrError(status)))
            CancelPipe(D3XX, pipe)
            break
            			
        # read data from specified pipe
        output = ReadPipe(D3XX, pipe, size - transferred)
        status = D3XX.getLastError()
        transferred += output['bytesTransferred']
		
        if sys.version_info.major == 3:
            buffread += output['bytes'].decode('latin1')
        else:
            buffread += output['bytes']
			
        logging.debug("Read[%#04X] bytesTransferred %d" % (pipe, output['bytesTransferred']))

    if sys.version_info.major == 3:
        buffread = bytes(buffread, 'latin1')

    compare.put(buffread == buffer)
	
    # write read data to log file			
    CreateLogFile(file, buffread)


def ChannelThreadFunc(D3XX, channel, size, output, timeout, directory, stress):
	
    # prepare data to loopback	
    dataBuffer = ''.join(random.choice(string.printable) for _ in range(size))

    # create logfile names for writer and reader threads
    currentDateTime = datetime.datetime.now().strftime('%Y%m%d_%H%M%S_')
    fileName = currentDateTime + "PayloadEP" + '{:02X}'.format(0x02 + channel) + ".txt"
    outFilepath = directory + fileName
    fileName = currentDateTime + "PayloadEP" + '{:02X}'.format(0x82 + channel) + ".txt"
    inFilepath = directory + fileName
				
    # initialize and run the writer and reader threads for the specified channel
    compare = queue.Queue()
    threadWriter = threading.Thread(target = WriterThreadFunc, 
        args = (D3XX, 0x02 + channel, dataBuffer, size, outFilepath))
    threadReader = threading.Thread(target = ReaderThreadFunc, 
        args = (D3XX, 0x82 + channel, dataBuffer, size, inFilepath, compare))
    threadWriter.start()
    threadReader.start()	
	
    # wait for the writer and reader threads to complete then check the status
    threadWriter.join(timeout)
    threadReader.join(timeout)
    result = compare.get(timeout)
    logging.debug("Channel[%d] loopback %s" %
        (channel, "successful" if result == True else "failed"))
    output.put(result)

    # remove ouput files if stress test and result is successful to prevent too many logs 
    if (stress == True and result == True):
        os.remove(outFilepath)
        os.remove(inFilepath)


def ProcessLoopback(D3XX, channelsToTest, sizeToTransfer, bStressTest, bUSB3):

    # set the transfer parameters
    if sizeToTransfer == 0:	
        transferSize = 1024 if bUSB3 else 512
        maxTransferSize = 65536
        incrementSize = 1024 if bUSB3 else 512
    else:	
        transferSize = sizeToTransfer
    sleepTime = 0.1
    timeout = 5

    # initialize 
    logDirectory = CreateLogDirectory()	
    threadChannel = []
    error = False
	
    while True:
	
        result = queue.Queue()

        # start the loopback channel threads
        # which will then spawn writer and reader threads		
        for channelToTest in channelsToTest:
            thread = threading.Thread(
                target = ChannelThreadFunc, 
                args = (D3XX, channelToTest, transferSize, result, timeout, logDirectory, bStressTest))
            thread.start()
            threadChannel.append(thread)
            # add delay to process context switching
            # because python has issues with multithreading
            time.sleep(sleepTime)			

        # wait for all the loopback channels to complete			
        while (len(threadChannel)):
            threadChannel[0].join()
            del threadChannel[0]

        # check the status of each loopback channel			
        for channelToTest in channelsToTest:
            if (result.get(timeout) == False):
                error = True
        if (error == True):
            break

        if (bStressTest == False):
            break
			
        # update transfer size
        if sizeToTransfer == 0:
            transferSize += incrementSize
            if (transferSize > maxTransferSize):
                transferSize = incrementSize

    return error


def main(channelsToTest=[0,1,2,3], transferSize=0, bStressTest=True):

    logging.debug("INPUT: SIZE=%d, STRESS=%s, CHANNELS=%s" % 
        (transferSize, bStressTest, channelsToTest))
    logging.debug("")
    logging.debug("")

    # raise exception on error
    # ftd3xx.raiseExceptionOnError(True)

    if sys.platform == 'linux':
        DemoTurnOffPipeThreads()
	
    # check connected devices
    numDevices = ftd3xx.createDeviceInfoList()
    if (numDevices == 0):
        logging.debug("ERROR: Please check environment setup! No device is detected.")
        return False
    logging.debug("Detected %d device(s) connected." % numDevices)
    devList = ftd3xx.getDeviceInfoList()	
    DisplayDeviceList(numDevices, devList)
    devIndex = SelectDevice(numDevices)
				
    # open the first device (index 0)
    D3XX = ftd3xx.create(devIndex, _ft.FT_OPEN_BY_INDEX)
    if (D3XX is None):
        logging.debug("ERROR: Please check if another D3XX application is open!")
        return False

    # get the version numbers of driver and firmware
    DisplayVersions(D3XX)
    if (sys.platform == 'win32' and D3XX.getDriverVersion() < 0x01020006):
        logging.debug("ERROR: Old kernel driver version. Please update driver from Windows Update or FTDI website!")
        D3XX.close()
        return False

    # check if USB3 or USB2		
    devDesc = D3XX.getDeviceDescriptor()
    bUSB3 = devDesc.bcdUSB >= 0x300

    # validate chip configuration
    cfg = D3XX.getChipConfiguration()
    DisplayChipConfiguration(cfg)
    numChannels = [4, 2, 1, 0, 0]
    numChannels = numChannels[cfg.ChannelConfig]
    if (numChannels == 0):
        logging.debug("invalid chip configuration for data loopback")	
        D3XX.close()
        return False
    if (cfg.OptionalFeatureSupport &
        _ft.FT_CONFIGURATION_OPTIONAL_FEATURE_ENABLENOTIFICATIONMESSAGE_INCHALL):
        logging.debug("invalid chip configuration: notification callback is set")	
        D3XX.close()
        return False

    # delete invalid channels		
    for channel in range(len(channelsToTest)-1, -1, -1):
        if (channelsToTest[channel] >= numChannels):
            del channelsToTest[channel]	
    if (len(channelsToTest) == 0):
        D3XX.close()
        return

    # process loopback for all channels
    error = ProcessLoopback(D3XX, channelsToTest, transferSize, bStressTest, bUSB3)
    if error:
        DisplayTroubleshootingGuide("LOOPBACK", devList, devIndex, cfg)

    D3XX.close()
    D3XX = 0	
	
    return True


if __name__ == "__main__":

    # initialize logging to log in both console and file
    logging.basicConfig(filename='dataloopback.log', filemode='w',
        level=logging.DEBUG, format='[%(asctime)s] %(message)s')	
    logging.getLogger().addHandler(logging.StreamHandler())
	
    logging.debug("")
    logging.debug("**************************************************************")
    logging.debug("FT60X D3XX PYTHON DATA LOOPBACK DEMO")
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
	
    logging.debug("USAGE: dataloopback.py [-h] [-s SIZE] [-t] [-c [CHANNEL [CHANNEL ...]]]")
    logging.debug("")

    # sample usage: 
    # dataloopback.py					- stress test with random size on all channels (channel 0-3)
    # dataloopback.py -s 1024			- stress test with 1024 transfer size
    # dataloopback.py -s 1024 -t		- test with 1024 transfer size 
    # dataloopback.py -t 				- test with random size
    # dataloopback.py -t -c 3			- test with random size on 4th channel (channel 3)
    # dataloopback.py -t -c 0 1 2 3		- test with random size on all channels (channel 0-3)

    # parse commandline arguments		
    parser = argparse.ArgumentParser(description="data loopback demo application")
    parser.add_argument('-c', '--channels', type=int, nargs='*', default=[0,1,2,3], help="channel/s to test (0-3)")
    parser.add_argument('-s', '--size', type=int, default=0, help="data transfer size")
    parser.add_argument('-t', '--stress', action="store_false", help="disable stress test")
    args = parser.parse_args()

    main(args.channels, args.size, args.stress)
	

