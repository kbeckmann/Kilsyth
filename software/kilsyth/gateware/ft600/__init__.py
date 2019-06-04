from migen import *

__all__ = ["FT600"]

class FT600(Module):
    """
    FT600 fifo 

    Use ``CEInserter`` and ``ResetInserter`` transformers to control the LFSR.

    ``sys`` clock domain is used for the state machine. Map this to the ft600 clock.

    :param ft600:
        ft600 IOs
    :param fifo_rx:
        RX fifo, i.e. reading data from the ft600 interface (from the USB host)
    :type AsyncFifo:
    :param fifo_tx:
        TX fifo, i.e. writing data to the ft600 interface (to the USB host)
    :type AsyncFifo:
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
            NextValue(ft600.oe_n, 1),
            NextValue(ft600.rd_n, 1),
            NextValue(ft600.wr_n, 1),
            NextValue(self.ft_be.oe, 0),
            NextValue(self.ft_data.oe, 0),
            NextValue(debug[0], 1),
            NextValue(debug[1], 0),
            NextValue(debug[2], 0),
            NextState("WAIT")
        )

        self.fsm.act(
            "WAIT",
            NextValue(debug[0], 0),
            NextValue(debug[1], 1),
            NextValue(debug[2], 0),
            NextValue(ft600.wr_n, 1),

            NextValue(self.ft_data.oe, 0),
            NextValue(self.ft_be.oe, 0),
            NextValue(self.ft_be.o, 0b00),

            If ((fifo_tx.readable) & (~ft600.txe_n),
                NextValue(fifo_tx.re, 1),
                NextState("WRITE")
            )
        )

        self.fsm.act(
            "WRITE",
            NextValue(debug[0], 0),
            NextValue(debug[1], 0),
            NextValue(debug[2], 1),
            NextValue(ft600.wr_n, 0),

            NextValue(self.ft_data.o, fifo_tx.dout),
            NextValue(self.ft_data.oe, 1),

            NextValue(self.ft_be.oe, 1),
            NextValue(self.ft_be.o, 0b11),

            If ((~fifo_tx.readable) | (ft600.txe_n),
                # There is nothing to read
                # or we are not allowed to write to ft600.
                # Time to wait.
                NextValue(fifo_tx.re, 0),
                NextState("WAIT")
            )
        )
