# WIP! WIP! WIP! 
This repo is a work in progress and far from release-worthy. Please don't make your own boards and expect any kind of support. However, it might reach a stable point sometime in the future (as of 2019-01).

# Kilsyth: ECP5 FPGA + FT60x FIFO
Kilsyth is a piece of hardware that contains an FPGA (Lattice ECP5) and a SuperSpeed USB 3.0 FIFO-bridge (FT60x). The goal is to provide a platform to be able to transfer high speed data transfers between a PC and an FPGA. The FPGA in turn can do whatever - e.g. interface with SDR, video capture, act as a logic analyzer.

## Current status
It's still in the early bring-up phase. Initial verification shows that it actually seems to work.

### RevA
RevA is the first prototype and has been designed and built.

- [x] It doesn't smoke when powered up.
- [x] USB-C connector works but is messy to solder.
- [ ] Loopback test is almost in place. Using the proprietary driver, high bi-directional speeds are achieavable (> 98MB/s in both directions simultaneously). Just need to figure out some off-by-one errors...
- [ ] Bootloader to store a custom bitstream on the flash.

Errata:
- C9 is not a GPIO on ECP5 F12 and some other variants. To get the LED working put a jumper on pin 31 and 33 on the Wide connector.
- FT_CLK is not routed to a clock pin. Can be fixed with a bodge wire! Remove R50 and R36, swap their paths.
- JTAG connector has a funky footprint on the PCB because CCW vs Odd/Even pinout on the symbol vs footprint. But the PCB silk screen is accurate so don't worry - it's just a stupid pinout.
- Need to add pull-ups for the SPI flash.

### RevB
Ideas for RevB are still being collected. Feel free to suggest changes in an issue.

- Add support for reversible USB-C connector using [PI5USB30213A](https://www.diodes.com/products/connectivity-and-timing/switches-mux/protocol-switches/usb-switches/part/PI5USB30213A).


## Software usage (TODO)

Requires a patched migen and a patched ftdi library.. Nasty, I know, sorry.

```
Help:
$ python -m software.kilsyth -h

Run blinky:
$ python -m software.kilsyth run blinky

```

# Contact

Reach out to [@kbeckmann](https://twitter.com/kbeckmann) on Twitter or IRC/Freenode.
