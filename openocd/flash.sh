#!/bin/sh

openocd -f interface/ftdi/dp_busblaster.cfg -c "transport select jtag; adapter_khz 10000;" -f kilsyth.cfg
