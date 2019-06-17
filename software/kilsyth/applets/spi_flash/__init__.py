from migen import *
from migen.genlib.fifo import AsyncFIFO
import os, sys, time

from .. import KilsythApplet
from ...gateware import *

from ...host import *

def BuildReg(values):
    return Array([Signal(8, reset=x) for x in values])

class FlashController(Module):
    def __init__(self, clk, clk_period, fifo, ce_n, sck, mosi, miso, wp_n, hold_n):
        io0 = mosi
        io1 = miso
        io2 = wp_n
        io3 = hold_n

        data = BuildReg([

            # 0x0B, # Fast Read Sequence (1-SPI)
            0x03, # Normal Read Sequence (1-SPI)
            # 0xAB, # RDID
            # 0xC7, # Chip erase
            # 0x06, # WREN (Write Enable)

            0x00, # Addr[0]
            0x00, # Addr[1]
            0x00, # Addr[2]
            0x00, # Addr[3]
        ])
        byte = Signal(max=len(data)+1)

        bit = Signal(max=16)

        word_rd = Signal(16)

        delay_s = 2
        counter = Signal(32, reset=int(delay_s * clk_period))

        clk_en = Signal()
        self.comb += [
            # fifo.din.eq(word_rd),
            If(clk_en,
                sck.eq(clk),
            ).Else(
                # Clock line should be pulled low when idling
                sck.eq(0),
            )
        ]

        self.submodules.fsm = FSM(reset_state="INIT")
        self.fsm.act(
            "INIT",
            NextValue(clk_en, 0),
            NextValue(ce_n, 1),
            NextValue(wp_n, 1),
            NextValue(hold_n, 1),
            NextValue(mosi, 0),

            NextValue(byte, 0),
            NextValue(bit, 0),

            NextValue(counter, counter - 1),
            If(counter == 0,
                NextValue(ce_n, 0),
                NextState("READ1"),
            ),
        )

        self.fsm.act(
            "READ1",
            NextValue(ce_n, 0),
            NextValue(clk_en, 1),

            If((data[byte] << bit) & 0x80,
                NextValue(mosi, 1),
            ).Else(
                NextValue(mosi, 0),
            ),
            NextValue(bit, bit + 1),
            If(bit == 7,
                NextValue(byte, byte + 1),
                NextValue(bit, 0),
            ),
            If(byte == len(data) - 1,
                NextValue(bit, 0),
                NextValue(byte, 0),
                NextValue(word_rd, 0),
                NextState("READ2"),
            ),
        ),

        self.fsm.act(
            "READ2",
            NextValue(ce_n, 0),
            NextValue(clk_en, 1),
            NextValue(fifo.we, 0),

            NextValue(word_rd, (word_rd << 1) | miso), # todo: msb first, big endian
            NextValue(bit, bit + 1),

            If (bit == 15,
                NextValue(fifo.we, 1),
                NextValue(fifo.din, (word_rd << 1) | miso),
                NextValue(word_rd, 0),
                NextValue(bit, 0),
            ),

            # infinite loop
            If(byte == 1,
                NextState("INIT"),
            ),
        )




class SpiFlash(KilsythApplet, name="spi_flash"):
    description = "SPI flash dumper / writer"
    help = "TODO"

    @classmethod
    def add_build_arguments(cls, parser):
        parser.add_argument(
            "--flash-clock", type=float, default=100,
            help="Clock frequency to use for the flash (MHz)")

        parser.add_argument(
            "--bytes", type=int, default=16*1024*1024,
            help="Number of bytes to dump")


    def __init__(self, device, args):
        self.args = args
        self.device = device

        ft600_pins = device.request('ft600')
        flash_pins = device.request('spiflash')
        wide = device.request('wide')

        self.clock_domains.cd_por = ClockDomain()
        self.clock_domains.cd_sys = ClockDomain(reset_less=False)
        self.cd_sys.clk = ft600_pins.clk
        device.add_period_constraint(ft600_pins.clk.backtrace[-1][0], 1000. / 100)

        flash_clk_f = int(float(args.flash_clock) * 1e6)
        cyc, _, _ = ClockGen.calculate(input_hz=100e6, output_hz=flash_clk_f)
        flash_clk = ClockGen(cyc)
        self.submodules.flash_clk = flash_clk

        self.clock_domains.cd_flash = ClockDomain(reset_less=True)
        self.cd_flash.clk = flash_clk.clk
        device.add_period_constraint("flash_clk_clk", 1000. / args.flash_clock)

        depth = 1024 * 2

        fifo_rx = ClockDomainsRenamer({
            "write": "sys",
            "read":  "flash",
        })(AsyncFIFO(16, depth))
        self.submodules += fifo_rx

        fifo_tx = ClockDomainsRenamer({
            "write": "flash",
            "read":  "sys",
        })(AsyncFIFO(16, depth))
        self.submodules += fifo_tx

        debug = Signal(3)
        self.submodules.ft600 = FT600(ft600_pins, fifo_rx, fifo_tx, debug)

        self.submodules.flash = ClockDomainsRenamer({
            "sys": "flash",
        })(FlashController(
            flash_clk.clk,
            flash_clk_f,
            fifo_tx,
            flash_pins.cs_n,
            wide[0],           # flash_pins.sck,
            flash_pins.mosi,   # 0
            flash_pins.miso,   # 1
            flash_pins.wp_n,   # 2
            flash_pins.hold_n, # 3
        ))

    async def run(self):
        print("Init driver")
        self.ftd3xx = FTD3xxWrapper()

        print("Reading...")
        bytesRead = 0
        bytesReadTotal = 0

        # TODO: Need to figure out how to detect HiSpeed vs SuperSpeed
        size = 1024

        t0 = time.time()
        f = open("flash.raw", "wb")
        while True:
            output = self.ftd3xx.read(size)
            if len(output) == 0:
                break

            bytesRead += len(output)
            bytesReadTotal += len(output)
            f.write(output)
            if bytesReadTotal >= self.args.bytes:
                break
            if bytesRead % (1000000 * self.args.flash_clock / 8) < size:
                diff = time.time() - t0
                t0 = time.time()
                print("read %d bytes (%.2f MB/s)" % (bytesRead, bytesRead/1024./1024./diff))
                bytesRead = 0
        print("Read %d bytes in total" % bytesReadTotal)
