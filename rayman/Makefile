PROJ=ft600
OPENOCD_INTERFACE:=interface/ftdi/dp_busblaster.cfg
TARGET:=lfe5u12

TAP:=$(TARGET).tap

prog_blinky0: blinky0.svf
	openocd -f $(OPENOCD_INTERFACE) -f ../openocd/kilsyth_$(TARGET).cfg -c "transport select jtag; adapter_khz 10000; init; svf -tap $(TAP) -quiet -progress $<; exit"

prog_blinky1: blinky1.svf
	openocd -f $(OPENOCD_INTERFACE) -f ../openocd/kilsyth_$(TARGET).cfg -c "transport select jtag; adapter_khz 10000; init; svf -tap $(TAP) -quiet -progress $<; exit"

clean:
	rm -rf build

.PHONY: prog clean
