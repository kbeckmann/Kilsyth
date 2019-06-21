from migen import *
from migen.genlib.fifo import AsyncFIFO, AsyncFIFOBuffered
import os, sys, time
import struct

from .. import KilsythApplet
from ...gateware import *

from ...host import *

def BuildReg(values):
    return Array([Signal(8, reset=x) for x in values])

class FlashController(Module):
    # fifo_rx: Data that is received from the SPI slave
    # fifo_tx: Data to be sent to the SPI slave
    def __init__(self, clk, clk_period, spi_fifo_rx, spi_fifo_tx, cs_n, sck, mosi, miso, wp_n, hold_n, debug):
        # io0 = mosi
        # io1 = miso
        # io2 = wp_n
        # io3 = hold_n

        self.clk = clk
        self.clk_period = clk_period
        self.spi_fifo_rx = spi_fifo_rx
        self.spi_fifo_tx = spi_fifo_tx
        self.cs_n = cs_n

        word_in = Signal(16)
        word_out = Signal(16)
        bit = Signal(max=16)

        clk_en = Signal()
        self.comb += [
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
            NextValue(cs_n, ~spi_fifo_tx.readable),
            NextValue(wp_n, 1),
            NextValue(hold_n, 1),
            NextValue(mosi, 0),
            NextValue(word_in, 0),

            NextValue(spi_fifo_rx.we, 0),
            spi_fifo_tx.re.eq(0),

            NextValue(bit, 0),

            NextValue(debug, 0b0001),

            If(spi_fifo_tx.readable,
                NextState("LOAD"),
            ),
        )

        self.fsm.act(
            "LOAD",
            NextValue(clk_en, 0),
            NextValue(mosi, 0),
            NextValue(word_in, 0),

            NextValue(spi_fifo_rx.we, 0),
            spi_fifo_tx.re.eq(0),

            NextValue(bit, 0),

            NextValue(debug, 0b0001),

            If(spi_fifo_tx.readable,
                spi_fifo_tx.re.eq(1),
                NextValue(word_out, 
                    ((spi_fifo_tx.dout << 8) & 0xff00) | 
                    ((spi_fifo_tx.dout >> 8) & 0x00ff)
                ),
                NextState("TRANSFER1"),
            ).Else(
                NextState("INIT"),
            ),
        )

        self.fsm.act(
            "TRANSFER1",
            NextValue(clk_en, 1),
            NextValue(spi_fifo_rx.we, 0),
            spi_fifo_tx.re.eq(0),

            NextValue(debug, 0b0010),

            If((word_out << bit) & 0x8000,
                NextValue(mosi, 1),
            ).Else(
                NextValue(mosi, 0),
            ),

            NextValue(word_in, (word_in << 1) | miso),

            NextValue(bit, bit + 1),
            If(bit == 15,
                NextState("WRITE"),
            ),
        ),

        self.fsm.act(
            "WRITE",
            NextValue(clk_en, 0),

            NextValue(spi_fifo_rx.we, 0),
            spi_fifo_tx.re.eq(0),

            NextValue(debug, 0b0100),

            If(spi_fifo_rx.writable,
                NextValue(spi_fifo_rx.we, 1),
                NextValue(spi_fifo_rx.din, 
                    ((word_in << 8) & 0xff00) | 
                    ((word_in >> 8) & 0x00ff)
                ),
                NextState("LOAD"),
            ),
        ),



class CommandParser(Module):
    def __init__(self, fifo_rx, fifo_tx, spi_fifo_rx, spi_fifo_tx, debug):

        self.submodules.fsm = FSM(reset_state="INIT")
        self.fsm.act(
            "INIT",
            fifo_rx.re.eq(1),
            NextValue(spi_fifo_tx.we, 0),
            If(fifo_rx.readable,
                If(fifo_rx.dout == 0xdead,
                    NextState("RX1"),
                )
            )
        )

        self.fsm.act(
            "RX1",
            fifo_rx.re.eq(1),
            NextValue(spi_fifo_tx.we, 0),
            If(fifo_rx.readable,
                If(fifo_rx.dout == 0xbeef,
                    NextState("RX2"),
                ).Else(
                    NextState("INIT"),
                )
            )
        )

        self.fsm.act(
            "RX2",
            fifo_rx.re.eq(1),
            NextValue(spi_fifo_tx.we, 0),
            If(fifo_rx.readable,
                Case(fifo_rx.dout, {
                    0:         NextState("CMD_DEBUG"),
                    1:         NextState("CMD_SPI_WRITE1"),
                    "default": NextState("INIT"),
                }),
            )
        )

        self.fsm.act(
            "CMD_DEBUG",
            fifo_rx.re.eq(1),
            NextValue(spi_fifo_tx.we, 0),
            If(fifo_rx.readable,
                NextValue(debug, fifo_rx.dout[:8]),
                NextState("INIT"),
            ),
        )

        packet_length = Signal(max=4096)
        self.fsm.act(
            "CMD_SPI_WRITE1",
            NextValue(debug, 0b0000_0010),
            fifo_rx.re.eq(1),
            NextValue(spi_fifo_tx.we, 0),
            If(fifo_rx.readable,
                NextValue(packet_length, fifo_rx.dout),
                NextState("CMD_SPI_WRITE2"),
            ),
        )

        # Write SPI RX data to fifo_tx
        self.comb += [
            fifo_tx.din.eq(spi_fifo_rx.dout),
            If(fifo_tx.writable & spi_fifo_rx.readable,
                fifo_tx.we.eq(1),
                spi_fifo_rx.re.eq(1),
            )
        ]

        self.fsm.act(
            "CMD_SPI_WRITE2",
            # NextValue(debug, 0b0000_0100),
            NextValue(debug, packet_length),
            # NextValue(debug, spi_fifo_tx.writable),
            # NextValue(debug, 0b1111),
            fifo_rx.re.eq(0),
            NextValue(spi_fifo_tx.we, 0),
            If(fifo_rx.readable & spi_fifo_tx.writable,
                fifo_rx.re.eq(1),
                NextValue(spi_fifo_tx.we, 1),
                NextValue(spi_fifo_tx.din, fifo_rx.dout),
                NextValue(packet_length, packet_length - 1),
                If(packet_length == 1,
                    NextState("INIT"),
                ),
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
        # device.add_period_constraint(ft600_pins.clk.backtrace[-1][0], 1000. / 100)
        device.add_period_constraint('clk', 1000. / 100)

        flash_clk_f = int(float(args.flash_clock) * 1e6)
        cyc, _, _ = ClockGen.calculate(input_hz=100e6, output_hz=flash_clk_f)
        flash_clk = ClockGen(cyc)
        self.submodules.flash_clk = flash_clk

        self.clock_domains.cd_flash = ClockDomain(reset_less=True)
        self.cd_flash.clk = flash_clk.clk
        device.add_period_constraint("flash_clk_clk", 1000. / args.flash_clock)

        depth = 128 #1024 * 2




        leds = device.request('user_led')

        fifo_rx = ClockDomainsRenamer({
            "write": "sys",
            "read":  "sys",
        })(AsyncFIFOBuffered(16, depth))
        self.submodules += fifo_rx

        fifo_tx = ClockDomainsRenamer({
            "write": "sys",
            "read":  "sys",
        })(AsyncFIFOBuffered(16, depth))
        self.submodules += fifo_tx

        debug = Signal(3)
        self.submodules.ft600 = FT600(ft600_pins, fifo_rx, fifo_tx, debug)






        spi_fifo_rx = ClockDomainsRenamer({
            "write": "flash",
            "read":  "sys",
        })(AsyncFIFO(16, depth))
        self.submodules += spi_fifo_rx

        spi_fifo_tx = ClockDomainsRenamer({
            "write": "sys",
            "read":  "flash",
        })(AsyncFIFO(16, depth))
        self.submodules += spi_fifo_tx



        debug1 = Signal(4)
        debug2 = Signal(4)

        self.submodules.flash = flash_controller = ClockDomainsRenamer({
            "sys": "flash",
        })(FlashController(
            clk=flash_clk.clk,
            clk_period=flash_clk_f,
            spi_fifo_rx=spi_fifo_rx,
            spi_fifo_tx=spi_fifo_tx,
            cs_n=flash_pins.cs_n,
            sck=wide[0],              # flash_pins.sck,
            mosi=flash_pins.mosi,     # 0
            miso=flash_pins.miso,     # 1
            wp_n=flash_pins.wp_n,     # 2
            hold_n=flash_pins.hold_n, # 3
            debug=debug1,
        ))



        self.submodules.sys = CommandParser(
            fifo_rx=fifo_rx,
            fifo_tx=fifo_tx,
            spi_fifo_rx=spi_fifo_rx,
            spi_fifo_tx=spi_fifo_tx,
            debug=debug2,
        )

        self.comb += [
            leds.eq(debug1 | (debug2 << 4)),
        ]

    async def run(self):
        print("Init driver")
        self.ftd3xx = FTD3xxWrapper()

        time.sleep(2)

        print("Go!")
        i = 0
        while True:
            # b = struct.pack("<HHHH", 0xdead, 0xbeef, 0x0000, i & 0xffff)
            # b = struct.pack("<HHHH", 0xdead, 0xbeef, 0x0001, 0x0010) + b'\x03\x00' + b'\x00\x00' * 15
            b = struct.pack("<HHHH", 0xdead, 0xbeef, 0x0001, 512-5) + b'\x03\x00' + b'\x00\x00' * (512 - 5)
            print(len(b))
            # b = struct.pack("<HHHHH", 0xdead, 0xbeef, 0x0001, 0x0001, 0b11110000_10101010)
            self.ftd3xx.write(b)
            print(self.ftd3xx.read(512-5))
            i += 1
            time.sleep(0.1)
            print("loop..")
