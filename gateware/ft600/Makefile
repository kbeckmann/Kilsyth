PROJ=ft600
OPENOCD_INTERFACE:=interface/ftdi/dp_busblaster.cfg

# Max frequency
FREQ:=70

ifndef TRELLIS
$(error Set TRELLIS to Trellis git root)
endif

all: ${PROJ}.bit

%.json: %.v
	yosys -p "synth_ecp5 -noccu2 -nobram -nomux -json $@" $<

%_out.config: %.json
	nextpnr-ecp5 --json $< --basecfg $(TRELLIS)/misc/basecfgs/empty_lfe5u-25f.config \
	--textcfg $@ --25k --package CABGA381 --speed 6 --lpf kilsyth.lpf --freq $(FREQ) --no-tmdriv


%.bit: %_out.config
	# lfe5u12f: 0x21111043 = 554766403
	ecppack --idcode 554766403 --svf ${PROJ}.svf $< $@

${PROJ}.svf : ${PROJ}.bit

prog: ${PROJ}.svf
	openocd -f $(OPENOCD_INTERFACE) -f ../../openocd/kilsyth_lfe5u12.cfg -c "transport select jtag; adapter_khz 10000; init; svf  -tap lfe5u12.tap -quiet -progress $<; exit"

clean:
	rm -f *.svf *.bit *.config *.json

.PHONY: prog clean
