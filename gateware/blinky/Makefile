PROJ=blinky
OPENOCD_INTERFACE:=interface/ftdi/dp_busblaster.cfg
OPENOCD_CONFIG:=../../openocd/kilsyth_lfe5u12.cfg
ECP5_VARIANT:=25k
TAP:=lfe5u12.tap
IDCODE:=--idcode 0x21111043

ifndef TRELLIS
$(error Set TRELLIS to Trellis git root)
endif

all: ${PROJ}.bit

%.json: %.v
	yosys -p "synth_ecp5 -noccu2 -nobram -nomux -json $@" $<

%_out.config: %.json
	nextpnr-ecp5 --json $< --textcfg $@ --$(ECP5_VARIANT) --package CABGA381 --lpf kilsyth.lpf

%.bit: %_out.config
	# lfe5u12f: 0x21111043 = 554766403
	ecppack $(IDCODE) --svf ${PROJ}.svf $< $@

${PROJ}.svf : ${PROJ}.bit

prog: ${PROJ}.svf
	openocd -f $(OPENOCD_INTERFACE) -f $(OPENOCD_CONFIG) -c "transport select jtag; adapter_khz 10000; init; svf  -tap $(TAP) -quiet -progress $<; exit"

clean:
	rm -f *.svf *.bit *.config *.json

.PHONY: prog clean
