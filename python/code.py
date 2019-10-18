import board
import busio
import time

from ecp5prog import ECP5Prog

fpga_spi = busio.SPI(board.D1, board.D0)

prog = ECP5Prog(fpga_spi)

start = time.monotonic()
prog.write_file('gateware.bit')
end = time.monotonic()
print('programming took %fms' % ((end - start) * 1000))
