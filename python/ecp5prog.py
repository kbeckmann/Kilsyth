import digitalio
import time


class ECP5Prog(object):
    def __init__(self, spi, baudrate=24000000):
        self._spi = spi

        self._spi.try_lock()
        self._spi.configure(baudrate=baudrate)
        self._spi.unlock()

    def write_file(self, file_name):
        self._spi.try_lock()

        for i in range(32):
            self._spi.write(b'\xFF')

        self._spi.write(b'\xBA\xB3')

        print("writing " + file_name)
        with open(file_name, 'rb') as f:
            while True:
                data = f.read(1024 * 4)
                if not data:
                    break

                self._spi.write(data)

        self._spi.unlock()
