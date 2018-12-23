from migen import *


class FT600Pipe(Module):
    def build_pin_tristate(self, pin, oe, o, i):
        self.specials += \
            Instance("TRELLIS_IO",
                p_DIR="BIDIR",
                i_T=oe,
                i_I=o,
                o_O=i,
            )

    def __init__(self, clk, leds, ft600):
        self.clock_domains.cd_por = ClockDomain(reset_less=True)
        self.clock_domains.cd_sys = ClockDomain()
        self.cd_sys.clk = clk
        wants_to_write = Signal()
 
        cd_ft600 = ClockDomain()
        cd_ft600.clk = ft600.clk

        ft_be_i = Signal(2)
        ft_be_o = Signal(2)
        ft_be_oe = Signal()
        self.build_pin_tristate(ft600.be, ft_be_oe, ft_be_o, ft_be_i)
 
        self.clock_domains += cd_ft600
 
        self.submodules.fsm = ClockDomainsRenamer("ft600")(FSM(reset_state="WAIT-INPUT"))
 
        ft_oe_n = Signal(reset=1)
        ft_wr_n = Signal(reset=1)
        ft_rd_n = Signal(reset=1)
        ft_data_oe = Signal(reset=0)
        self.counter = Signal(26)
 
        self.comb += [
            leds[0].eq(self.counter[23]),
            # Cat(leds[1], leds[2]).eq(ft600.be),
            # leds[3].eq(ft600.txe_n),
            # leds[4].eq(ft600.rxf_n),
            # leds[5].eq(ft_rd_n),
            # leds[6].eq(~leds[6]),
            # leds[7].eq(wants_to_write),
            ft_be_oe.eq(ft_data_oe),
        ]
 
        self.sync += [
            ft600.oe_n.eq(ft_oe_n),
            ft600.wr_n.eq(ft_wr_n),
            ft600.rd_n.eq(ft_rd_n),
            self.counter.eq(self.counter + 1),
        ]
 
        self.fsm.act(
            "WAIT-INPUT",
            leds[7].eq(1),
            ft_oe_n.eq(1),
            ft_wr_n.eq(1),
            ft_rd_n.eq(1),
            ft_be_oe.eq(0),
            ft_data_oe.eq(0),
            If(
                ft600.txe_n == 0 and wants_to_write,
                NextState("WRITE-WORD"),
            ).Elif(
                ft600.rxf_n == 0,
                NextState("READ-WORD"),
            )
        ),
        self.fsm.act(
            "READ-WORD",
            leds[5].eq(1),
            ft_oe_n.eq(0),
            ft_rd_n.eq(0),
            If(
                ft600.rxf_n == 1,
                wants_to_write.eq(1),
                NextState("WAIT-INPUT")
            )
        ),
        self.fsm.act(
            "WRITE-WORD",
            leds[3].eq(1),
            wants_to_write.eq(0),
            ft_be_oe.eq(1),
            ft_be_o.eq(0b11),
            ft_wr_n.eq(0),
            NextState("WAIT-INPUT"),
        )
 
 
if __name__ == '__main__':
    import kilsyth
    plat = kilsyth.Platform(toolchain='trellis')
    plat.add_period_constraint("ft600", 10.)
    clk = plat.request("clk16")
    leds = [plat.request('user_led', i) for i in range(8)]
    ft600 = plat.request('ft600')
 
    ft600pipe = FT600Pipe(clk, leds, ft600)
 
    plat.build(ft600pipe, toolchain_path='/usr/share/trellis', idcode="0x21111043")
