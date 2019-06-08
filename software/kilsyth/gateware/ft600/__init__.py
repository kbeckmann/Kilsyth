from migen import *

__all__ = ["FT600"]

class FT600(Module):
    """
    FT600 fifo

    ``sys`` clock domain is used in this module. It should be mapped to ft60x.clk.

    :param ft600:
        ft600 IOs
    :param fifo_rx:
        RX fifo, i.e. reading data from the ft600 interface (from the USB host)
    :type _FIFOInterface:
    :param fifo_tx:
        TX fifo, i.e. writing data to the ft600 interface (to the USB host)
    :type _FIFOInterface:
    :param debug:
        State machine debug information
    :type Signal[3]:
    """
    def __init__(self, ft600, fifo_rx, fifo_tx, debug):
        ft_be_triple = TSTriple(2)
        self.ft_be = ft_be_triple.get_tristate(ft600.be)
        self.specials += self.ft_be

        ft_data_triple = TSTriple(16)
        self.ft_data = ft_data_triple.get_tristate(ft600.data)
        self.specials += self.ft_data

        self.submodules.fsm = FSM(reset_state="INIT")
        self.fsm.act(
            "INIT",
            NextValue(debug[0], 0),
            NextValue(debug[1], 0),
            NextValue(debug[2], 0),

            ft600.oe_n.eq(1),
            ft600.rd_n.eq(1),
            ft600.wr_n.eq(1),

            NextValue(self.ft_be.oe, 0),
            NextValue(self.ft_data.oe, 0),

            fifo_tx.re.eq(0),

            NextState("WAIT")
        )

        cache = Signal(16)
        cache_valid = Signal()

        self.fsm.act(
            "WAIT",
            NextValue(debug[0], 1),
            NextValue(debug[1], 0),
            NextValue(debug[2], 0),

            # Idle states for the control pins
            ft600.oe_n.eq(1),
            ft600.rd_n.eq(1),
            ft600.wr_n.eq(1),

            NextValue(self.ft_data.oe, 0),
            NextValue(self.ft_be.oe, 0),

            fifo_tx.re.eq(0),
            NextValue(fifo_rx.we, 0),

            # If ((cache_valid | fifo_tx.readable) & (~ft600.txe_n),
            If ((fifo_tx.readable) & (~ft600.txe_n),

                # TX to ft60x works like this:
                # 1. When ft600.txe_n is 0, there is space available in the TX buffer.
                # 2. The clock cycle after ft600.wr_n is asserted,
                #    BE and DATA will be read until txe_n is released.
                #    Data will only be read up to the clock cycle just before.
                # This means that we need to assert ft600.wr_n only when we have data ready.

                NextValue(self.ft_be.oe, 1),
                NextValue(self.ft_be.o, 0b11),
                NextValue(self.ft_data.oe, 1),

                NextState("WRITE")
            )
            .Elif(fifo_rx.writable & (~ft600.rxf_n),
                NextValue(self.ft_be.oe, 1),
                NextValue(self.ft_be.o, 0b11),
                NextValue(self.ft_data.oe, 1),
    
                ft600.oe_n.eq(0),

                NextState("READ")
            )
        )


        self.fsm.act(
            "READ",
            NextValue(debug[0], 0),
            NextValue(debug[1], 1),
            NextValue(debug[2], 0),

            # Tell FT600 that data should be read in the next cycle
            ft600.oe_n.eq(0),
            ft600.rd_n.eq(0),
            ft600.wr_n.eq(0),

            # Tell FT600 that banks 1 and 2 are used
            NextValue(self.ft_be.oe, 1),
            NextValue(self.ft_be.o, 0b11),

            # Tell our fifo that we want to write in the next cycle
            NextValue(fifo_rx.we, 1),
            NextValue(fifo_rx.din, self.ft_data.i),

            fifo_tx.re.eq(0),

            # Output enable for the data pins
            NextValue(self.ft_data.oe, 0),

            If ((~fifo_rx.writable) | (ft600.rxf_n),
                # There is nothing to read
                # or we are not allowed to write to ft600.
                # Time to wait.
                NextValue(fifo_rx.we, 0),
                fifo_tx.re.eq(0),

                ft600.oe_n.eq(1),
                ft600.rd_n.eq(1),

                NextValue(self.ft_be.oe, 0),

                NextState("WAIT")
            )
        )

        self.fsm.act(
            "WRITE",
            NextValue(debug[0], 0),
            NextValue(debug[1], 0),
            NextValue(debug[2], 1),

            # Tell FT600 that data should be read in the next cycle
            ft600.oe_n.eq(1),
            ft600.rd_n.eq(1),
            ft600.wr_n.eq(0),

            # Tell FT600 that banks 1 and 2 are used
            NextValue(self.ft_be.oe, 1),
            NextValue(self.ft_be.o, 0b11),

            # Tell our fifo that we want to a value in the next cycle
            # NextValue(fifo_tx.re, 1),
            fifo_tx.re.eq(1),

            # Used the cached value from the previous transfer if available,
            # use the value from the FIFO otherwise.
            If (cache_valid,
                self.ft_data.o.eq(cache),
                NextValue(cache_valid, 0),
            ).Else(
                self.ft_data.o.eq(fifo_tx.dout),
                NextValue(cache, fifo_tx.dout),
            ),

            # Output enable for the data pins
            NextValue(self.ft_data.oe, 1),

            If ((~fifo_tx.readable) | (ft600.txe_n),
                # There is nothing to read
                # or we are not allowed to write to ft600.
                # Time to wait.
                fifo_tx.re.eq(0),

                ft600.wr_n.eq(1),
                NextValue(self.ft_be.oe, 0),
                NextValue(self.ft_data.oe, 0),

                # If ft600.txe_n == 1, that means that the ft600
                # will not read out data that we have just taken
                # from the FIFO. Cache it.
                # Before the next transfer, we must use the cache
                # and not take a value from the FIFO.
                If (fifo_tx.readable & ft600.txe_n,
                    NextValue(cache_valid, 1),
                ),

                NextState("WAIT")
            )
        )
