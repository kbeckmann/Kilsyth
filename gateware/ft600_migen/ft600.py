from migen import *
import sys, os
is_testing = False

class FT600Pipe(Module):
    def __init__(self, clk, leds, ft600):
        self.clock_domains.cd_por = ClockDomain()
        self.clock_domains.cd_sys = ClockDomain(reset_less=False)
        self.cd_sys.clk = ft600.clk

        self.counter = Signal(32)

        timer = Signal(32)

        ft_be_triple = TSTriple(2)
        ft_be = ft_be_triple.get_tristate(ft600.be)
        self.specials += ft_be

        ft_data_triple = TSTriple(16)
        ft_data = ft_data_triple.get_tristate(ft600.data)
        self.specials += ft_data

        words_received = Signal(16, reset=0)

        self.comb += [
            leds[0].eq(self.counter[0]),
        ]
 
        self.sync += [
            self.counter.eq(self.counter + 1),
        ]

        width = 16
        depth = 2048
        self.specials.mem = Memory(width, depth)
        wrport = self.mem.get_port(write_capable=True)
        rdport = self.mem.get_port(has_re=False)
        self.specials += wrport, rdport

        self.submodules.fsm = FSM(reset_state="WAIT-INPUT")
        self.fsm.act(
            "WAIT-INPUT",
            NextValue(leds[2], 1),
            NextValue(ft600.oe_n, 1),
            NextValue(ft600.rd_n, 1),
            NextValue(ft600.wr_n, 1),
            NextValue(ft_be.oe, 0),
            NextValue(ft_data.oe, 0),

            NextValue(wrport.we, 0),

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
                # TODO: Care about ft_be
                NextValue(words_received, words_received + 1),
                NextValue(wrport.we, 1),
                NextValue(wrport.adr, words_received),
                NextValue(wrport.dat_w, ft_data.i),
            )
        )
        self.fsm.act(
            "WRITE-WORD",
            NextValue(leds[6], 1),
            NextValue(ft600.wr_n, 0),

            NextValue(rdport.adr, words_received),
            NextValue(ft_data.o, rdport.dat_r),

            NextValue(ft_data.oe, 1),
            NextValue(ft_be.oe, 1),
            NextValue(ft_be.o, 0b11),
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
    target = os.environ["TARGET"] if "TARGET" in os.environ else "lfe5u12"
    plat = kilsyth.Platform(toolchain='trellis', target=target)
    plat.add_period_constraint("ft600", 10.)
    clk = plat.request("clk16")
    leds = [plat.request('user_led', i) for i in range(8)]
    ft600 = plat.request('ft600')
 
    ft600pipe = FT600Pipe(clk, leds, ft600)

    if is_testing:
        run_simulation(ft600pipe, ft600pipe.testbench(clk, leds, ft600), vcd_name="out.vcd")
        print("Passed")
    else:
        plat.build(ft600pipe, toolchain_path='/usr/share/trellis', idcode=plat.idcode)
