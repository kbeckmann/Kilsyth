from nmigen import *
from nmigen.build import *

def FT600Resource(*args, clk, data, be, rd_n, wr_n, gpio1, txe_n, rxf_n, oe_n,
                 conn=None, attrs=None):
    io = []
    io.append(Subsignal("clk", Pins(clk, dir="i", conn=conn, assert_width=1), Clock(100e6)))
    io.append(Subsignal("data", Pins(data, dir="io", conn=conn, assert_width=16)))
    io.append(Subsignal("be", Pins(be, dir="io", conn=conn, assert_width=2)))
    io.append(Subsignal("rd_n", Pins(rd_n, dir="o", conn=conn, assert_width=1)))
    io.append(Subsignal("wr_n", Pins(wr_n, dir="o", conn=conn, assert_width=1)))
    io.append(Subsignal("gpio1", Pins(gpio1, dir="o", conn=conn, assert_width=1)))
    io.append(Subsignal("txe_n", Pins(txe_n, dir="i", conn=conn, assert_width=1)))
    io.append(Subsignal("rxf_n", Pins(rxf_n, dir="i", conn=conn, assert_width=1)))
    io.append(Subsignal("oe_n", Pins(oe_n, dir="o", conn=conn, assert_width=1)))

    return Resource.family(*args, default_name="ft600", ios=io)


class FT600(Elaboratable):
    """
    FT600 fifo

    ``sys`` clock domain is used in this module. It should be mapped to ft60x.clk.

    :param pins:
        FT600 pins
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
    def __init__(self, pins, fifo_rx, fifo_tx, debug):
        self.pins = pins
        self.fifo_rx = fifo_rx
        self.fifo_tx = fifo_tx
        self.debug = debug

    def elaborate(self, platform):
        pins = self.pins
        fifo_rx = self.fifo_rx
        fifo_tx = self.fifo_tx
        debug = self.debug

        m = Module()

        cache = Signal(16)
        cache_valid = Signal()

        with m.FSM(reset="INIT") as fsm:
            with m.State("INIT"):
                m.d.sync += debug[0].eq(0)
                m.d.sync += debug[1].eq(0)
                m.d.sync += debug[2].eq(0)

                m.d.comb += pins.oe_n.eq(1)
                m.d.comb += pins.rd_n.eq(1)
                m.d.comb += pins.wr_n.eq(1)

                m.d.sync += pins.be.oe.eq(0)
                m.d.sync += pins.data.oe.eq(0)

                m.d.comb += fifo_tx.r_en.eq(0)

                m.next = "WAIT"

            with m.State("WAIT"):
                m.d.sync += debug[0].eq(1)
                m.d.sync += debug[1].eq(0)
                m.d.sync += debug[2].eq(0)

                # Idle states for the control pins
                m.d.comb += pins.oe_n.eq(1)
                m.d.comb += pins.rd_n.eq(1)
                m.d.comb += pins.wr_n.eq(1)

                m.d.sync += pins.data.oe.eq(0)
                m.d.sync += pins.be.oe.eq(0)

                m.d.comb += fifo_tx.r_en.eq(0)
                
                m.d.sync += fifo_rx.w_en.eq(0)

                # If ((cache_valid | fifo_tx.r_rdy) & (~pins.txe_n),
                with m.If((fifo_tx.r_rdy) & (~pins.txe_n)):
                    # TX to ft60x works like this:
                    # 1. When pins.txe_n is 0, there is space available in the TX buffer.
                    # 2. The clock cycle after pins.wr_n is asserted,
                    #    BE and DATA will be read until txe_n is released.
                    #    Data will only be read up to the clock cycle just before.
                    # This means that we need to assert pins.wr_n only when we have data ready.

                    m.d.sync += pins.be.oe.eq(1)
                    m.d.sync += pins.be.o.eq(0b11)
                    m.d.sync += pins.data.oe.eq(1)

                    m.next = "WRITE"
                with m.Elif(fifo_rx.w_rdy & (~pins.rxf_n)):
                    m.d.sync += pins.be.oe.eq(1)
                    m.d.sync += pins.be.o.eq(0b11)
                    m.d.sync += pins.data.oe.eq(1)
        
                    m.d.comb += pins.oe_n.eq(0)

                    m.next = "READ"

            with m.State("READ"):
                m.d.sync += debug[0].eq(0)
                m.d.sync += debug[1].eq(1)
                m.d.sync += debug[2].eq(0)

                # Tell FT600 that data should be read in the next cycle
                m.d.comb += pins.oe_n.eq(0)
                m.d.comb += pins.rd_n.eq(0)
                m.d.comb += pins.wr_n.eq(0)

                # Tell FT600 that banks 1 and 2 are used
                m.d.sync += pins.be.oe.eq(1),
                m.d.sync += pins.be.o.eq(0b11),

                # Tell our fifo that we want to write in the next cycle
                m.d.sync += fifo_rx.w_en.eq(1),
                m.d.sync += fifo_rx.w_data.eq(pins.data.i),

                m.d.comb += fifo_tx.r_en.eq(0)

                # Output enable for the data pins
                m.d.sync += pins.data.oe.eq(0),

                with m.If((~fifo_rx.w_rdy) | (pins.rxf_n)):
                    # There is nothing to read
                    # or we are not allowed to write to pins.
                    # Time to wait.
                    m.d.sync += fifo_rx.w_en.eq(0),
                    m.d.comb += fifo_tx.r_en.eq(0),

                    m.d.comb += pins.oe_n.eq(1),
                    m.d.comb += pins.rd_n.eq(1),

                    m.d.sync += pins.be.oe.eq(0),

                    m.next = "WAIT"

            with m.State("WRITE"):
                m.d.sync += debug[0].eq(0),
                m.d.sync += debug[1].eq(0),
                m.d.sync += debug[2].eq(1),

                # Tell FT600 that data should be read in the next cycle
                m.d.comb += pins.oe_n.eq(1)
                m.d.comb += pins.rd_n.eq(1)
                m.d.comb += pins.wr_n.eq(0)

                # Tell FT600 that banks 1 and 2 are used
                m.d.sync += pins.be.oe.eq(1),
                m.d.sync += pins.be.o.eq(0b11),

                # Tell our fifo that we want to a value in the next cycle
                # m.d.sync += fifo_tx.re, 1),
                m.d.comb += fifo_tx.r_en.eq(1),

                # Used the cached value from the previous transfer if available,
                # use the value from the FIFO otherwise.
                with m.If(cache_valid):
                    m.d.comb += pins.data.o.eq(cache),
                    m.d.sync += cache_valid.eq(0),
                with m.Else():
                    m.d.comb += pins.data.o.eq(fifo_tx.r_data),
                    m.d.sync += cache.eq(fifo_tx.r_data),

                # Output enable for the data pins
                m.d.sync += pins.data.oe.eq(1)

                with m.If((~fifo_tx.r_rdy) | (pins.txe_n)):
                    # There is nothing to read
                    # or we are not allowed to write to pins.
                    # Time to wait.
                    m.d.comb += fifo_tx.r_en.eq(0)

                    m.d.comb += pins.wr_n.eq(1)
                    m.d.sync += pins.be.oe.eq(0)
                    m.d.sync += pins.data.oe.eq(0)

                    # If pins.txe_n == 1, that means that the ft600
                    # will not read out data that we have just taken
                    # from the FIFO. Cache it.
                    # Before the next transfer, we must use the cache
                    # and not take a value from the FIFO.
                    with m.If(fifo_tx.r_rdy & pins.txe_n):
                        m.d.sync += cache_valid.eq(1)

                    m.next = "WAIT"
        return m
