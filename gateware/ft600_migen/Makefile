PROJ=ft600
OPENOCD_INTERFACE:=interface/ftdi/dp_busblaster.cfg

all: build/top.svf

build/top.svf: ft600.py kilsyth.py
	python ${PROJ}.py

prog: build/top.svf
	openocd -f $(OPENOCD_INTERFACE) -f ../../openocd/kilsyth_lfe5u12.cfg -c "transport select jtag; adapter_khz 10000; init; svf  -tap lfe5u12.tap -quiet -progress $<; exit"

clean:
	rm -rf build

.PHONY: prog clean
