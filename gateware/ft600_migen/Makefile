PROJ=ft600
OPENOCD_INTERFACE:=interface/ftdi/dp_busblaster.cfg
TARGET:=lfe5u12

TAP:=$(TARGET).tap

all: build/top.svf

build/top.svf: ft600.py kilsyth.py
	python ${PROJ}.py --build

prog: build/top.svf
	openocd -f $(OPENOCD_INTERFACE) -f ../../openocd/kilsyth_$(TARGET).cfg -c "transport select jtag; adapter_khz 10000; init; svf -tap $(TAP) -quiet -progress $<; exit"

clean:
	rm -rf build

.PHONY: prog clean
