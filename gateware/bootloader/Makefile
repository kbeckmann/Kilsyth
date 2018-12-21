PROJ=bootloader
OPENOCD_INTERFACE:=interface/ftdi/dp_busblaster.cfg

ifndef TRELLIS
$(error Set TRELLIS to Trellis git root)
endif

bootloader/kilsyth_bootloader.bit:
	echo "Run diamond to build a .bit file!"

${PROJ}.svf: ./bootloader/kilsyth_bootloader.bit
	$(TRELLIS)/tools/bit_to_svf.py ./bootloader/kilsyth_bootloader.bit $@

prog: ${PROJ}.svf
	openocd -f $(OPENOCD_INTERFACE) -f ../../openocd/kilsyth_lfe5u12.cfg -c "transport select jtag; adapter_khz 10000; init; svf  -tap lfe5u12.tap -quiet -progress $<; exit"
