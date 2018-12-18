#!/bin/sh

if [ "$TRELLIS" = "" ]; then
	echo "Set environment variable TRELLIS to your Trellis root"
	exit
fi

$TRELLIS/tools/bit_to_svf.py ../gateware/bootloader/bootloader/kilsyth_bootloader.bit ../gateware/bootloader/bootloader/kilsyth_bootloader.svf

openocd -f interface/ftdi/dp_busblaster.cfg -c "transport select jtag; adapter_khz 10000;" -f kilsyth.cfg

