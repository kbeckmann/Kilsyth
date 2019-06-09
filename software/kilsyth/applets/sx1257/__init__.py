from migen import *
from migen.genlib.fifo import SyncFIFO, AsyncFIFO, AsyncFIFOBuffered
import os, sys

from .. import KilsythApplet
from ...gateware.ft600 import *

# Borrowed from the Migen example
# https://github.com/m-labs/migen/blob/master/examples/sim/fir.py
# This does not sythesize well, so need to optimize it.
from scipy import signal
from functools import reduce
from operator import add
class FIR(Module):
    def __init__(self, coef, wsize=16):
        self.coef = coef
        self.wsize = wsize
        self.i = Signal((self.wsize, True))
        self.o = Signal((self.wsize, True))

        muls = []
        src = self.i
        for c in self.coef:
            sreg = Signal((self.wsize, True))
            self.sync += sreg.eq(src)
            src = sreg
            c_fp = int(c*2**(self.wsize - 1))
            muls.append(c_fp*sreg)
        sum_full = Signal((2*self.wsize-1, True))
        self.sync += sum_full.eq(reduce(add, muls))
        self.comb += self.o.eq(sum_full >> self.wsize-1)


class IQSampler(Module):
    def __init__(self, i_out, q_out, fifo, debug):
        cmax = 72*2
        counter = Signal(16)
        bit_depth = 12
        i_r = Signal((bit_depth, True))
        q_r = Signal((bit_depth, True))
        overflow = Signal()

        coef = signal.firwin(8, 0.25/36, window=('kaiser', 8))

        firI = FIR(coef, bit_depth)
        self.submodules += firI
        firQ = FIR(coef, bit_depth)
        self.submodules += firQ

        self.comb += [
            debug[0].eq(overflow),
            firI.i.eq(i_r),
            firQ.i.eq(q_r),
            If(counter == 0,
                fifo.din.eq(
                    ((firI.o[bit_depth-8:])     ) |
                    ((firQ.o[bit_depth-8:]) << 8)
                ),
                fifo.we.eq(1),
            ).Else(
                fifo.we.eq(0),
            ),
        ]

        self.sync += [
            If (~fifo.writable,
                overflow.eq(1)
            ),

            If(i_out,
                i_r.eq(1),
            ).Else(
                i_r.eq(-1),
            ),

            If(q_out,
                q_r.eq(1),
            ).Else(
                q_r.eq(-1),
            ),

            counter.eq(counter + 1),
            If(counter == cmax,
                counter.eq(0)
            ),

        ]

def BuildCmd(values):
    v = [len(values)] + values
    return Array([Signal(8, reset=x) for x in v])

class I2CMaster(Module):
    # TODO: Convert to a generic module
    # clkdiv:       Constant to count to for clock division
    # slave_addr:   Slave address
    def __init__(self, clkdiv, slave_addr, scl, sda, leds):

        # debug = Signal(8)
        debug = leds

        # debug = Signal(8)
        # debug2 = Cat(leds[x] for x in range(2, 8))
        # self.comb += [debug2.eq(0b10_0000)]

        # debug2 = Cat(leds[x] for x in range(2, 8))
        # a = Signal(16)
        # self.sync += [a.eq(a + 1)]
        # self.sync += [debug2.eq(a[8:])]

        self.slow_counter = Signal(max=100_000_000)
        self.clkdiv = clkdiv
        self.stop_counter = clkdiv * 2
        self.clk_counter = Signal(max=self.stop_counter + 1)
        self.w_addr = (slave_addr << 1) | 0
        self.r_addr = (slave_addr << 1) | 1

        scl_triple = TSTriple(1)
        self.scl = scl_triple.get_tristate(scl)
        self.specials += self.scl

        sda_triple = TSTriple(1)
        self.sda = sda_triple.get_tristate(sda)
        self.specials += self.sda

        self.comb += [
            self.scl.o.eq(0),
            self.sda.o.eq(0),
        ]

        # Array of commands
        # Commands are arrays of 8 bit Signals starting with a length 
        data = Array([
            # Enable GPIO SS1
            BuildCmd([
                self.w_addr,
                0xF6,
                0x02
            ]),

            # Set GPIO SS1 = 1 (reset=1)
            BuildCmd([
                self.w_addr,
                0xF4,
                0x02
            ]),

            # Configure SPI
            # MSB is transmitted first
            # CLK is low when idle
            # data is clocked on leading edge
            # SPI CLK is 1843 kHz
            BuildCmd([
                self.w_addr,
                0xF0,
                0b000_0_0_0_00,
            ]),

            # Set GPIO SS1 = 0 (reset=0)
            BuildCmd([
                self.w_addr,
                0xF4,
                0x00,
            ]),

            ##############

            # Set TX freq=867.990 MHz
            BuildCmd([
                self.w_addr,
                0x01,
                0x80 | 0x04, # RegFrfTxMsb
                0xc0,
            ]),
            BuildCmd([
                self.w_addr,
                0x01,
                0x80 | 0x05, # RegFrfTxxMid
                0xe2,
            ]),
            BuildCmd([
                self.w_addr,
                0x01,
                0x80 | 0x06, # RegFrfTxLsb
                0xfc,
            ]),

            #########

            ##############

            # Set RX freq=867.900 MHz
            # TODO: Write helper function for this
            BuildCmd([
                self.w_addr,
                0x01,
                0x80 | 0x01, # RegFrfRxMsb
                0xc0,
            ]),
            BuildCmd([
                self.w_addr,
                0x01,
                0x80 | 0x02, # RegFrfRxMid
                0xdd,
            ]),
            BuildCmd([
                self.w_addr,
                0x01,
                0x80 | 0x03, # RegFrfRxLsb
                0xde,
            ]),

            #########


            # Set PA, TX, IDLE enabled
            BuildCmd([
                self.w_addr,
                0x01,
                0x80, # Operating mode
                # 0b0000_1_1_0_1, # PA, TX, IDLE enabled
                0b0000_0_0_1_1, # RX, IDLE enabled
            ]),

            # Set clock out enabled
            BuildCmd([
                self.w_addr,
                0x01,
                0x80 | 0x10, # RegClkSelect
                0b0000_0_0_1_0, # Clk_out=1
            ]),

            # Set 50 ohm Impedance
            BuildCmd([
                self.w_addr,
                0x01,
                0x80 | 0x0C, # RegRxAnaGain
                0b001_1111_0, # RxLnaGain=0dB, RxBasebandGain=0b1111, LnaZin=50 Ohm
            ]),

            # Set trim to 36MHz xtal
            BuildCmd([
                self.w_addr,
                0x01,
                0x80 | 0x0D, # RegRxBw
                0b111_101_01, # RxAdcBw = 400kHz, RxAdcTrim=36MHz, RxBasebandBw=500kHz
            ]),


        ])

        command = Signal(max=len(data)+1)
        byte = Signal(max=256)
        bit = Signal(max=8)
    
        self.submodules.fsm = FSM(reset_state="INIT")
        self.fsm.act(
            "INIT",
            NextValue(debug, 0b010101),
            NextValue(command, 0),
            NextValue(byte, 1),
            NextValue(bit, 7),
            NextValue(self.scl.oe, 0),
            NextValue(self.sda.oe, 0),
            NextValue(self.slow_counter, self.slow_counter + 1),
            If (self.slow_counter == 100_000_000-1,
                NextState("W_START"),
                NextValue(self.clk_counter, 0),
                NextValue(self.slow_counter, 0),
            )
        )

        self.fsm.act(
            "W_START",
            NextValue(debug, 0b000001),
            NextValue(self.sda.oe, 1),
            NextValue(self.clk_counter, self.clk_counter + 1),
            If (self.clk_counter == self.clkdiv,
                NextValue(self.clk_counter, 0),
                NextValue(bit, 7),
                NextState("W_ADDR"),
            ),
        )

        self.fsm.act(
            "W_ADDR",
            NextValue(debug, 0b000010),
            NextValue(self.scl.oe, self.clk_counter < (self.clkdiv // 2)),
            NextValue(self.sda.oe, ~((data[command][byte] >> bit) & 1)),
            NextValue(self.clk_counter, self.clk_counter + 1),
            If(self.clk_counter == self.clkdiv,
                NextValue(bit, bit - 1),
                NextValue(self.clk_counter, 0),
                If(bit == 0,
                    NextState("W_ADDR_WAIT_ACK"),
                    NextValue(self.sda.oe, 0),
                )
            ),
        )

        self.fsm.act(
            "W_ADDR_WAIT_ACK",
            NextValue(debug, 0b000100),
            NextValue(self.scl.oe, self.clk_counter < (self.clkdiv // 2)),
            NextValue(self.clk_counter, self.clk_counter + 1),
            If(self.clk_counter >= self.clkdiv,
                NextValue(self.clk_counter, 0),
                If(self.sda.i == 0,
                    # ACK
                    NextState("W_ADDR_WAIT_SCL"),
                ).Else(
                    # NACK
                    NextState("W_ADDR_HANDLE_NACK"),
                ),
            ),
        )

        self.fsm.act(
            "W_ADDR_HANDLE_NACK",
            NextValue(debug, 0b000111),
            NextValue(self.sda.oe, 1),
            # Wait for clock stretching
            If(self.scl.i == 1,
                NextValue(self.clk_counter, self.clk_counter + 1),
                If(self.clk_counter == self.clkdiv,
                    NextValue(byte, 1),
                    NextValue(bit, 7),
                    NextValue(self.sda.oe, 0),
                    NextValue(self.clk_counter, 0),
                    NextState("W_START"),
                ).Elif(self.clk_counter >= self.clkdiv // 2,
                    NextValue(self.sda.oe, 0),
                )
            )
        )

        self.fsm.act(
            "W_ADDR_WAIT_SCL",
            NextValue(debug, 0b001000),
            NextValue(self.scl.oe, 1),
            NextValue(self.sda.oe, 1), # ACK
            If(self.clk_counter == self.clkdiv,
                NextValue(self.scl.oe, 0),

                If(byte == data[command][0],
                    If(command == len(data) - 1,
                        NextState("W_ADDR_SEND_FINAL_STOP"),
                        NextValue(self.clk_counter, 0),
                    ).Else(
                        NextState("W_ADDR_SEND_STOP"),
                        NextValue(byte, 1),
                        NextValue(command, command + 1),
                        NextValue(bit, 7),
                        NextValue(self.clk_counter, 0),
                    )
                ).Else(
                    NextState("W_ADDR_WAIT_SCL1"),
                    NextValue(byte, byte + 1),
                    NextValue(bit, 7),
                    NextValue(self.clk_counter, self.clkdiv // 2),
                ),
            ).Else(
                NextValue(self.clk_counter, self.clk_counter + 1),
            ),
        )

        self.fsm.act(
            "W_ADDR_WAIT_SCL1",
            NextValue(debug, 0b010000),
            # Set sda to MSB of the next byte we're going to send
            # Wait for slave to release clock (clock stretching)
            NextValue(self.sda.oe, ~((data[command][byte] >> bit) & 1)),
            If(self.scl.i == 1,
                NextState("W_ADDR"),
            )
        )

        self.fsm.act(
            "W_ADDR_SEND_STOP",
            NextValue(debug, 0b100000),
            NextValue(self.sda.oe, 1), # Prepare stop signal
            If(self.scl.i == 1, # Wait for slave to release clock (clock stretching)
                # Wait 1 period with sda=1, scl=1
                NextValue(self.clk_counter, self.clk_counter + 1),
                If(self.clk_counter == self.stop_counter,
                    NextState("W_START"),
                    NextValue(self.sda.oe, 0),
                    NextValue(self.clk_counter, 0),
                ).Elif(self.clk_counter > self.clkdiv // 2,
                    NextValue(self.sda.oe, 0), # Prepare stop signal
                ),
            )
        )

        self.fsm.act(
            "W_ADDR_SEND_FINAL_STOP",
            NextValue(debug, 0b110000),
            NextValue(self.sda.oe, 1), # Prepare stop signal
            If(self.scl.i == 1, # Wait for slave to release clock (clock stretching)
                # Wait 1 period with sda=1, scl=1
                NextValue(self.clk_counter, self.clk_counter + 1),
                If(self.clk_counter == self.stop_counter,
                    NextState("HANG"),
                    NextValue(self.clk_counter, 0),
                    NextValue(self.sda.oe, 0), # Prepare stop signal
                ).Elif(self.clk_counter > self.clkdiv // 2,
                    NextValue(self.sda.oe, 0), # Prepare stop signal
                ),
            )
        )

        self.fsm.act(
            "HANG",
            NextValue(debug, 0b000000),
            If(self.clk_counter == 3,
                NextState("INIT"),
            )
        )

class SX1257(KilsythApplet, name="sx1257"):
    help = "SX1257 PMOD integration"
    description = """
To test this as a streaming receiver:
cd software/ft600_test/linux-x86_64
make
mkfifo dump.raw
mkfifo out.raw
LD_LIBRARY_PATH=. ./streamer 0 1 0 dump.raw
sox -t raw -e unsigned -b 8 -c 2 -r 48000 dump.raw  -t raw -e floating-point -b 32 -c 2 -r 48000 out.raw
Start gqrx with the config: file=$PWD/ft600_test/linux-x86_64/out.raw,freq=867.9e6,rate=250e3,repeat=false,throttle=true
"""

    __all_revs = ["a", "b"]

    @classmethod
    def add_build_arguments(cls, parser):
        parser.add_argument(
            "--rev", metavar="REV", type=str, default=cls.__all_revs[0],
            help="SX1257 PMOD revision (one of {})".format(" ".join(cls.__all_revs)))

    def __init__(self, device, args):
        self.device = device
        pmod0 = device.request('pmod0')

        if args.rev == "a":
            scl = pmod0.pin1
            sda = pmod0.pin2
            i_out = pmod0.pin7
            q_out = pmod0.pin8
            iq_clk = pmod0.pin4
        elif args.rev == "b":
            scl = pmod0.pin5
            sda = pmod0.pin6
            i_out = pmod0.pin3
            q_out = pmod0.pin4
            iq_clk = pmod0.pin8

        led = device.request('user_led')
        ft600_pins = device.request('ft600')

        # TODO: How to support multiple clock constraints?
        # device.add_period_constraint("ft600", 1000. / 100)
        device.add_period_constraint("iq_clk", 1000. / 36)

        self.clock_domains.cd_por = ClockDomain()
        self.clock_domains.cd_sys = ClockDomain(reset_less=False)
        self.cd_sys.clk = ft600_pins.clk

        self.clock_domains.cd_sx1257 = ClockDomain(reset_less=True)
        self.cd_sx1257.clk = iq_clk

        debug_i2c = led[0:6]
        self.submodules += I2CMaster(100_000_000 // 400_000, 0x28, scl, sda, debug_i2c)

        depth = 64
        fifo_tx = ClockDomainsRenamer({
            "write": "sx1257",
            "read":  "sys",
        })(AsyncFIFO(16, depth))
        self.submodules += fifo_tx

        fifo_rx = ClockDomainsRenamer({
            "write": "sys",
            "read":  "sx1257",
        })(AsyncFIFO(16, depth))
        self.submodules += fifo_rx

        debug_ft = Signal(8)
        self.submodules.ft600 = FT600(ft600_pins, fifo_rx, fifo_tx, debug_ft)

        debug_iq = Signal()
        rxsamples = ClockDomainsRenamer({"sys": "sx1257"})(IQSampler(i_out, q_out, fifo_tx, debug_iq))
        self.submodules += rxsamples

