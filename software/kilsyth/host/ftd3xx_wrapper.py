import sys
import time

from ..ftd3xx import ftd3xx
from ..ftd3xx.defines import *

class FTD3xxWrapper():
    def __init__(self):
        self.ResetChipConfiguration()

        channel = 0
        if sys.platform == 'linux':
            epout = channel
            epin = channel
        else:
            epout = 0x02 + channel
            epin = 0x82 + channel

        D3XX = ftd3xx.create(0, FT_OPEN_BY_INDEX)
        if D3XX is None:
            print("ERROR: Please check if another D3XX application is open!")
            return

        self.D3XX = D3XX
        self.epin = epin
        self.epout = epout

    def close(self):
        if self.D3XX is not None:
            self.D3XX.close(True)
            self.D3XX = None

    def write(self, bytes, timeout=1000):
        return self.D3XX.writePipe(self.epout, bytes, len(bytes), timeout)

    def read(self, datalen, timeout=1000):
        output = self.D3XX.readPipeEx(self.epin, datalen=datalen, timeout=timeout, raw=True)
        return output['bytes']

    def WaitForDeviceReenumeration(self):
        origValue = ftd3xx.raiseExceptionOnError(False)
        time.sleep(1)
        while (ftd3xx.listDevices() == None):
            time.sleep(1)
        ftd3xx.raiseExceptionOnError(origValue)

        if sys.platform == 'linux':
            count = 0
            while count == 0:
                count = ftd3xx.createDeviceInfoList()

    def ResetChipConfiguration(self):
        # set default chip configuration
        # TODO: Use FT_OPEN_BY_DESCRIPTION to avoid problems with LimeSDR Mini
        # TODO: Only do this in factory/recovery mode, no need to reconfigure all the time 
        D3XX = ftd3xx.create(0, FT_OPEN_BY_INDEX)
        if D3XX is None:
            raise Exception("Failed to open driver: FT60x not found or busy.")

        cfg = D3XX.getChipConfiguration()
        cfg.ProductID = 0x601e
        cfg.bInterval = 0x09
        cfg.PowerAttributes = 0xe0
        cfg.PowerConsumption = 0x60
        cfg.Reserved2 = 0x00
        cfg.FIFOClock = FT_CONFIGURATION_FIFO_CLK_100
        # cfg.FIFOClock = FT_CONFIGURATION_FIFO_CLK_66
        # cfg.FIFOClock = FT_CONFIGURATION_FIFO_CLK_50
        # cfg.FIFOClock = FT_CONFIGURATION_FIFO_CLK_40
        cfg.FIFOMode = FT_CONFIGURATION_FIFO_MODE_245
        cfg.ChannelConfig = FT_CONFIGURATION_CHANNEL_CONFIG_1
        cfg.OptionalFeatureSupport = 0x03c2
        cfg.BatteryChargingGPIOConfig = 0xe4
        cfg.MSIO_Control = 0x00010800

        D3XX.setChipConfiguration(cfg)
        D3XX.close(True)
        D3XX = 0

        # wait until device has reenumerated
        self.WaitForDeviceReenumeration()
