from migen import *
from migen.genlib.fifo import _FIFOInterface, AsyncFIFO, SyncFIFOBuffered
import argparse
import sys, os

TESTING = False

class TSTripleFake():
    def __init__(self, width):
        self.oe = Signal()
        self.o = Signal(width)
        self.i = Signal(width)

# How to use:
# cd software/ft600_test/linux-x86_64
# make
# LD_LIBRARY_PATH=. ./streamer 0 1 0 dump.raw
# sox -t raw -e unsigned -b 8 -c 2 -r 48000 dump.raw  -t raw -e floating-point -b 32 -c 2 -r 48000 out.raw
# gqrx config: file=/home/konrad/dev/Kilsyth/software/ft600_test/linux-x86_64/out.raw,freq=868e6,rate=500e3,repeat=true,throttle=true
#


class IQSampler(Module):
    # pmod0.pin2 => CLK_OUT
    # pmod0.pin5 => I_OUT
    # pmod0.pin6 => Q_OUT
    # fifo = AsyncFifo()
    def __init__(self, pmod0, fifo):
        counter = Signal(3)
        sample_i = Signal(8)
        sample_q = Signal(8)

        self.comb += [
            fifo.din.eq(((sample_q) << 8) | sample_i),
            If((counter == 7) & fifo.writable,
                # if fifo.writable is false we will drop a sample
                fifo.we.eq(1),
            ).Else(
                fifo.we.eq(0),
            ),
        ]

        self.sync += [
            # LSB first
            # sample_i.eq((sample_i << 1) | pmod0.pin5),
            # sample_q.eq((sample_q << 1) | pmod0.pin6),

            # MSB first
            sample_i.eq((sample_i >> 1) | (pmod0.pin3 << 7)),
            sample_q.eq((sample_q >> 1) | (pmod0.pin4 << 7)),

            counter.eq(counter + 1),
        ]

class IQSamplerBad(Module):
    # pmod0.pin2 => CLK_OUT
    # pmod0.pin5 => I_OUT
    # pmod0.pin6 => Q_OUT
    # fifo = AsyncFifo()
    def __init__(self, pmod0, fifo):
        # Sample with 150kHz bandwidth assuming a 36MHz clock
        # 150kHz leads to a cnt_max of 240, samples are still <256
        cnt_max = 36000000 // 150000

        counter = Signal(max=cnt_max+1)
        sample_i = Signal(8)
        sample_q = Signal(8)

        self.comb += [
            fifo.din.eq(((sample_q) << 8) | sample_i),
            If((counter == cnt_max) & fifo.writable,
                # if fifo.writable is false we will drop a sample
                fifo.we.eq(1),
            ).Else(
                fifo.we.eq(0),
            ),
        ]

        self.sync += [
            If (counter == cnt_max,
                sample_i.eq(pmod0.pin5),
                sample_q.eq(pmod0.pin6),
                counter.eq(0),
            ).Else(
                sample_i.eq(sample_i + pmod0.pin5),
                sample_q.eq(sample_q + pmod0.pin6),
                counter.eq(counter + 1),
            )
        ]

class IQSamplerFake(Module):
    # Use this to test that we can count properly and not drop samples.
    def __init__(self, pmod0, fifo):
        counter = Signal(16)
        counter2 = Signal(8)

        self.comb += [
            fifo.din.eq(((counter2+1) << 8) | counter2),
            If((counter == 0) & fifo.writable,
                fifo.we.eq(1),
            ).Else(
                fifo.we.eq(0),
            ),
        ]

        self.sync += [
            # 72 = 500kHz bandwidth with a 36MHz clock
            If (counter == 72,
                counter.eq(0),
                counter2.eq(counter2 + 2)
            ).Else(
                counter.eq(counter + 1)
            )
        ]

def BuildCmd(values):
    v = [len(values)] + values
    return Array([Signal(8, reset=x) for x in v])


class I2CMaster(Module):
    # clkdiv:       Constant to count to for clock division
    # slave_addr:   Slave address
    def __init__(self, clkdiv, slave_addr, scl, sda, leds):

        debug = Cat(leds[x] for x in range(2, 8))

        # debug = Signal(8)
        # debug2 = Cat(leds[x] for x in range(2, 8))
        # self.comb += [debug2.eq(0b10_0000)]

        # debug2 = Cat(leds[x] for x in range(2, 8))
        # a = Signal(16)
        # self.sync += [a.eq(a + 1)]
        # self.sync += [debug2.eq(a[8:])]

        self.slow_counter = Signal(max=100_000_000)
        self.clkdiv = clkdiv
        self.stop_counter = clkdiv * 100
        self.clk_counter = Signal(max=self.stop_counter+1)
        self.w_addr = (slave_addr << 1) | 0
        self.r_addr = (slave_addr << 1) | 1

        if TESTING:
            self.sda = TSTripleFake(1)
            self.scl = TSTripleFake(1)
        else:
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

            # Set freq=867.990 MHz
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


            # Set PA, TX, IDLE enabled
            BuildCmd([
                self.w_addr,
                0x01,
                0x80, # Operating mode
                0b0000_1_1_0_1, # PA, TX, IDLE enabled
            ]),

            # Set clock out enabled
            BuildCmd([
                self.w_addr,
                0x01,
                0x80 | 0x10, # CLK select
                0x02, # clkout enabled
            ]),

        ])
        command = Signal(max=len(data)+1)
        byte = Signal(max=256)
        bit = Signal(max=8)
    
        self.submodules.fsm = FSM(reset_state="INIT")
        self.fsm.act(
            "INIT",
            NextValue(debug, 0b000000),
            NextValue(command, 0),
            NextValue(byte, 1),
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
            If(self.clk_counter == self.clkdiv,
                If(self.sda.i == 0,
                    # ACK
                    NextValue(self.clk_counter, 0),
                    NextState("W_ADDR_WAIT_SCL"),
                ).Else(
                    # NACK
                    NextValue(debug, 0b101010),
                )
            ).Elif(byte == data[command][0] - 1,
                # Keep the clock ticking if we're at the last byte
                NextValue(self.clk_counter, self.clk_counter + 1),
            )
            .Else(
                NextValue(self.clk_counter, self.clk_counter + 1),
            ),
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
            NextValue(debug, 0b111111),
            If(self.clk_counter == 3,
                NextState("INIT"),
            )
        )



class FT600Pipe(Module):
    def __init__(self, leds, ft600, pmod0):
        self.clock_domains.cd_por = ClockDomain()
        self.clock_domains.cd_sys = ClockDomain(reset_less=False)
        self.clock_domains.cd_sx1257 = ClockDomain(reset_less=True)
        self.cd_sys.clk = ft600.clk
        self.cd_sx1257.clk = pmod0.pin4

        self.submodules += I2CMaster(100_000_000 // 100_000, 0x28, pmod0.pin1, pmod0.pin2, leds)

        # This can probably be a lot smaller
        depth = 256
        fifo = ClockDomainsRenamer({
            "write": "sx1257",
            "read":  "sys",
        })(AsyncFIFO(16, depth))
        self.submodules += fifo

        rxsamples = ClockDomainsRenamer({"sys": "sx1257"})(IQSampler(pmod0, fifo))
        # rxsamples = ClockDomainsRenamer({"sys": "sx1257"})(IQSamplerFake(pmod0, fifo))
        self.submodules += rxsamples

        counter = Signal(32)

        if TESTING:
            self.ft_be = TSTripleFake(2)
            self.ft_data = TSTripleFake(16)
        else:
            ft_be_triple = TSTriple(2)
            self.ft_be = ft_be_triple.get_tristate(ft600.be)
            self.specials += self.ft_be

            ft_data_triple = TSTriple(16)
            self.ft_data = ft_data_triple.get_tristate(ft600.data)
            self.specials += self.ft_data

        self.comb += [
            # leds[0].eq(counter[0]),
        ]
 
        self.sync += [
            counter.eq(counter + 1),
        ]

        self.submodules.fsm = FSM(reset_state="INIT")
        self.fsm.act(
            "INIT",
            NextValue(ft600.oe_n, 1),
            NextValue(ft600.rd_n, 1),
            NextValue(ft600.wr_n, 1),
            NextValue(self.ft_be.oe, 0),
            NextValue(self.ft_data.oe, 0),
            # NextValue(leds[5], 1),
            # NextValue(leds[6], 0),
            # NextValue(leds[7], 0),
            NextState("WAIT")
        )

        self.fsm.act(
            "WAIT",
            # NextValue(leds[5], 0),
            # NextValue(leds[6], 1),
            # NextValue(leds[7], 0),
            NextValue(ft600.wr_n, 1),

            NextValue(self.ft_data.oe, 0),
            NextValue(self.ft_be.oe, 0),
            NextValue(self.ft_be.o, 0b00),

            If ((fifo.readable) & (~ft600.txe_n),
                NextValue(fifo.re, 1),
                NextState("WRITE")
            )
        )

        self.fsm.act(
            "WRITE",
            # NextValue(leds[5], 0),
            # NextValue(leds[6], 0),
            # NextValue(leds[7], 1),
            NextValue(ft600.wr_n, 0),

            NextValue(self.ft_data.o, fifo.dout),
            NextValue(self.ft_data.oe, 1),

            NextValue(self.ft_be.oe, 1),
            NextValue(self.ft_be.o, 0b11),

            If ((~fifo.readable) | (ft600.txe_n),
                # There is nothing to read
                # or we are not allowed to write to ft600.
                # Time to wait.
                NextValue(fifo.re, 0),
                NextState("WAIT")
            )
        )

def build_gateware(testing):
    # So ugly but I don't care
    global TESTING
    TESTING = testing

    import kilsyth

    target_clock_mhz = 100

    target = os.environ["TARGET"] if "TARGET" in os.environ else "lfe5u45"
    plat = kilsyth.Platform(toolchain='trellis', target=target)
    plat.add_period_constraint("ft600", 1000. / target_clock_mhz)
    leds = [plat.request('user_led', i) for i in range(8)]
    ft600 = plat.request('ft600')
    pmod0 = plat.request('pmod0')
 
    ft600pipe = FT600Pipe(leds, ft600, pmod0)

    if TESTING:
        run_simulation(ft600pipe, ft600pipe.testbench(leds, ft600), vcd_name="out.vcd")
        print("Passed")
    else:
        plat.build(ft600pipe, toolchain_path='/usr/share/trellis', idcode=plat.idcode)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Kilsyth FT600 integration')
    parser.add_argument('--test', action='store_true', help='Run gateware tests')
    parser.add_argument('--build', action='store_true', help='Builds gateware')
    parser.add_argument('--run', help='Runs applet')

    args = parser.parse_args()
    
    if args.test:
        build_gateware(True)
    elif args.build:
        build_gateware(False)
