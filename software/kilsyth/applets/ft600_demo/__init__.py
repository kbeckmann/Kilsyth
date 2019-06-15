from migen import *
from migen.genlib.fifo import SyncFIFO, AsyncFIFO, AsyncFIFOBuffered
import os, sys, time, random, string
import asyncio
from threading import Thread

from .. import KilsythApplet
from ...gateware.ft600 import *

from ...ftd3xx import ftd3xx
from ...ftd3xx.defines import *

class FT600Demo(KilsythApplet, name="ft600_demo"):
    description = "FT600 TX demo"
    help = "Sends an increasing counter to the ft600 interface"

    __all_modes = ["source", "sink", "loopback"]

    @classmethod
    def add_build_arguments(cls, parser):
        parser.add_argument(
            "-c", "--count", metavar="COUNT", type=int, default=0,
            help="Skip COUNT cycles when reading/writing (default: 0)")

        parser.add_argument(
            dest="mode", metavar="MODE", type=str, choices=cls.__all_modes,
            help="run benchmark mode MODE (one of {})".format(" ".join(cls.__all_modes)))

    def __init__(self, device, args):
        self.device = device

        led = device.request('user_led')
        ft600_pins = device.request('ft600')
        clk16 = device.request('clk16')


        self.clock_domains.cd_por = ClockDomain()
        self.clock_domains.cd_sys = ClockDomain(reset_less=False)
        self.cd_sys.clk = ft600_pins.clk
        device.add_period_constraint(ft600_pins.clk.backtrace[-1][0], 1000. / 100)

        self.clock_domains.cd_clk16 = ClockDomain(reset_less=False)
        self.cd_clk16.clk = clk16

        depth = 1024 * 2

        if False:
            fifo_rx = SyncFIFO(16, depth)
            self.submodules += fifo_rx

            fifo_tx = SyncFIFO(16, depth)
            self.submodules += fifo_tx
        else:
            # AsyncFIFO requires a depth of at least 8 to be able to run at max speed 
            fifo_rx = ClockDomainsRenamer({
                "write": "sys",
                "read":  "sys",
            })(AsyncFIFO(16, depth))
            self.submodules += fifo_rx

            fifo_tx = ClockDomainsRenamer({
                "write": "sys",
                "read":  "sys",
            })(AsyncFIFO(16, depth))
            self.submodules += fifo_tx


        debug = led[-3:]
        self.submodules.ft600 = FT600(ft600_pins, fifo_rx, fifo_tx, debug)

        if args.mode == "source":
            # Test TX only
            # Write counter every nth clock cycle
            counter = Signal(32)
            counter2 = Signal(8)
            self.comb += [
                fifo_tx.din.eq(
                    ((counter2 + 1) << 8) |
                    ((counter2    )     )
                ),
                fifo_tx.we.eq(counter == 0),
            ]

            self.sync += [
                If (counter == args.count,
                    counter.eq(0),
                    counter2.eq(counter2 + 2)
                ).Else(
                    counter.eq(counter + 1)
                )
            ]
        elif args.mode == "sink":
            # Test RX only
            counter = Signal(32)
            self.comb += [
                fifo_rx.re.eq(counter == 0),
            ]

            self.sync += [
                If (counter == args.count,
                    counter.eq(0),
                ).Else(
                    counter.eq(counter + 1)
                )
            ]
        elif args.mode == "loopback":
            # Loopback
            self.comb += [
                fifo_tx.din.eq(fifo_rx.dout),
                If(fifo_tx.writable & fifo_rx.readable,
                    fifo_tx.we.eq(1),
                    fifo_rx.re.eq(1),
                )
            ]


    def DemoLoopback(self):

        bStreamingMode=False

        result = True
        channel = 0
        if sys.platform == 'linux':
            epout = channel
            epin = channel
        else:
            epout = 0x02 + channel
            epin = 0x82 + channel
        size = 4096
        
        print("Write/read synchronous loopback of string")
        D3XX = ftd3xx.create(0, FT_OPEN_BY_INDEX)
        if D3XX is None:
            print("ERROR: Please check if another D3XX application is open!")
            return False

        # flush old crap out first
        D3XX.readPipeEx(epin, size, raw=True, timeout=0)

        for x in range(0, 1024):
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
            # print(buffwrite[:bytesWritten])
            # print(buffread[:bytesRead])
            if (buffread[:bytesRead] != buffwrite[:bytesWritten]):
                compare = False
            # print("[%d] writePipe [%d] bytes, readPipe [%d] bytes, compare = %s" % 
            #     (x, bytesWritten, bytesRead, compare))
            if compare == False:
                result = False		
                break
                
        # disable streaming mode
        if bStreamingMode and sys.platform == 'linux':
            D3XX.clearStreamPipe(epout)
            D3XX.clearStreamPipe(epin)
        
        D3XX.close()
        D3XX = 0
        print("")
        
        return result
        
    def DemoWaitForDeviceReenumeration(self):

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



    def DemoResetChipConfiguration(self):

        # set default chip configuration
        D3XX = ftd3xx.create(0, FT_OPEN_BY_INDEX)
        if D3XX is None:
            print("ERROR: Please check if another D3XX application is open!")
            return False

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
        self.DemoWaitForDeviceReenumeration()

        return True

    def setup_ft(self):
        channel = 0
        if sys.platform == 'linux':
            epout = channel
            epin = channel
        else:
            epout = 0x02 + channel
            epin = 0x82 + channel

        size = 4096
        
        D3XX = ftd3xx.create(0, FT_OPEN_BY_INDEX)
        if D3XX is None:
            print("ERROR: Please check if another D3XX application is open!")
            return False

        # flush old crap out first
        D3XX.readPipeEx(epin, size, raw=True, timeout=0)

        self.D3XX = D3XX
        self.epin = epin
        self.epout = epout


    def producer_fn(self, loop, D3XX, epout):
        asyncio.set_event_loop(loop)

        print("producer")
        size = 4096
        totalBytesWritten = 0
        buffwrite = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(size))
        buffwrite = buffwrite.encode('latin1')
        # for x in range(0, 10240):
        while True:
            bytesWritten = D3XX.writePipe(epout, buffwrite, size, timeout=1000)
            totalBytesWritten += bytesWritten
            # await asyncio.sleep(0)
        # print("wrote %d" % totalBytesWritten)


    def consumer_fn(self, loop, D3XX, epin):
        asyncio.set_event_loop(loop)
        time.sleep(0.100)

        print("consumer")
        size = 4096
        bytesRead = 0
        buffread = bytes()

        t0 = time.time()
        while (True):
            output = D3XX.readPipeEx(epin, size, raw=True, timeout=1000)
            if output['bytesTransferred'] == 0:
                break
            bytesRead += output['bytesTransferred']
            # buffread += output['bytes']
            if bytesRead % 10000000 < 4096:
                diff = time.time() - t0
                t0 = time.time()
                print("read %d bytes (%.2f MB/s)" % (bytesRead, bytesRead/1024./1024./diff))
                bytesRead = 0



    async def run(self):
        print("fun!")
        self.setup_ft()
        print("start!")

        # self.DemoResetChipConfiguration()
        # self.DemoLoopback()

        producer_loop = asyncio.new_event_loop()
        producer = Thread(target=self.producer_fn, args=(producer_loop, self.D3XX, self.epout))

        consumer_loop = asyncio.new_event_loop()
        consumer = Thread(target=self.consumer_fn, args=(consumer_loop, self.D3XX, self.epin))

        producer.start()
        consumer.start()


        # task1 = asyncio.create_task(
        #     self.producer(self.D3XX, self.epout))

        # task2 = asyncio.create_task(
        #     self.consumer(self.D3XX, self.epin))

        # await asyncio.gather(task1, task2)


        # loop = asyncio.get_event_loop()
        # task1 = asyncio.run_coroutine_threadsafe(self.producer(self.D3XX, self.epout), loop)
        # task2 = asyncio.run_coroutine_threadsafe(self.consumer(self.D3XX, self.epin), loop)
        # # await asyncio.gather(task1, task2)
        # task1.result()
        # task2.result()
