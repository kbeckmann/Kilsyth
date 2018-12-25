from migen import *
import sys

is_testing = False

class FT600Pipe(Module):
    def build_pin_tristate(self, pin, oe, o, i):
        if not is_testing:
            self.specials += \
                Instance("TRELLIS_IO",
                    p_DIR="BIDIR",
                    io_B=pin,
                    i_T=oe,
                    i_I=o,
                    o_O=i,
                )

    def __init__(self, clk, leds, ft600):
        self.clock_domains.cd_por = ClockDomain()
        self.clock_domains.cd_sys = ClockDomain(reset_less=False)
        self.cd_sys.clk = ft600.clk

        self.counter = Signal(32)

        timer = Signal(32)

        # This tristate stuff seems to be sort of broken :(

        # ft_be_i = Signal(2)
        # ft_be_o = Signal(2)
        # ft_be_oe = Signal()
        # self.build_pin_tristate(ft600.be, ft_be_oe, ft_be_o, ft_be_i)

        # ft_data_i = Signal(16)
        # ft_data_o = Signal(16)
        # ft_data_oe = Signal()
        # self.build_pin_tristate(ft600.data, ft_data_oe, ft_data_o, ft_data_i)

        words_received = Signal(16, reset=0)
        buffer = [Signal(16)] * 1024

        self.comb += [
            leds[0].eq(self.counter[0]),
        ]
 
        self.sync += [
            self.counter.eq(self.counter + 1),
        ]
 
        self.submodules.fsm = FSM(reset_state="WAIT-INPUT")
        self.fsm.act(
            "WAIT-INPUT",
            NextValue(leds[2], 1),
            NextValue(ft600.oe_n, 1),
            NextValue(ft600.rd_n, 1),
            NextValue(ft600.wr_n, 1),
            # NextValue(ft_be_o, 0b11),
            # NextValue(ft_be_oe, 1),
            # NextValue(ft_data_o, 0xFEFE),
            # NextValue(ft_data_oe, 1),
            NextValue(ft600.be, 0b00),
            NextValue(ft600.data, 0xFEFE),
            If(
                (ft600.txe_n == 0) & (words_received != 0),
                NextValue(leds[2], 0),
                NextState("WRITE-WORD"),
            ).Elif(
                # (ft600.rxf_n == 0), # using this line makes it faster but uhm.. we shouldn't do that.
                (ft600.rxf_n == 0) & (words_received == 0),
                NextValue(words_received, 0),
                NextValue(leds[2], 0),
                NextState("READ-WORD"),
            )
        )
        self.fsm.act(
            "READ-WORD",
            NextValue(leds[4], 1),
            NextValue(ft600.oe_n, 0),
            NextValue(ft600.rd_n, 0),
            If(
                ft600.rxf_n == 1,
                NextValue(leds[4], 0),
                NextState("WAIT-INPUT")
            ).Else(
                NextValue(words_received, words_received + 1),
            )
        )
        self.fsm.act(
            "WRITE-WORD",
            NextValue(leds[6], 1),
            NextValue(ft600.wr_n, 0),
            # NextValue(ft_be_o, 0b11),
            # NextValue(ft_be_oe, 1),
            # NextValue(ft_data_o, 0xCCCC),
            # NextValue(ft_data_oe, 1),
            NextValue(ft600.be, 0b11),
            # NextValue(ft600.data, 0xCCDD),
            NextValue(ft600.data, words_received),
            If(
                (ft600.txe_n == 1) | (words_received == 0),
                NextValue(leds[6], 0),
                NextState("WAIT-INPUT")
            ).Else(
                NextValue(words_received, words_received - 1),
            )
        )

    def testbench(self, clk, leds, ft600):
        # yield
        # yield
        yield ft600.txe_n.eq(1)
        yield ft600.rxf_n.eq(1)
        yield ft600.be.eq(0)
        yield
        yield
        yield
        yield
        yield
        # FT writes 4 words to the bus master (fpga)
        yield ft600.rxf_n.eq(0)
        yield ft600.be.eq(0b11)
        yield
        # clk 0
        yield
        # clk 1
        yield
        # clk 2
        yield
        # clk 3
        yield ft600.rxf_n.eq(1)
        yield
        yield
        yield
        yield ft600.txe_n.eq(0)
        yield
        yield
        yield
        yield
        yield
        yield ft600.txe_n.eq(1)
        yield
        yield
        yield


if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == "test":
        is_testing = True

    import kilsyth
    plat = kilsyth.Platform(toolchain='trellis')
    plat.add_period_constraint("ft600", 10.)
    clk = plat.request("clk16")
    leds = [plat.request('user_led', i) for i in range(8)]
    ft600 = plat.request('ft600')
 
    ft600pipe = FT600Pipe(clk, leds, ft600)

    if is_testing:
        run_simulation(ft600pipe, ft600pipe.testbench(clk, leds, ft600), vcd_name="out.vcd")
        print("Passed")
    else:
        plat.build(ft600pipe, toolchain_path='/usr/share/trellis', idcode="0x21111043")
