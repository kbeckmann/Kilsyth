# This is inspired by https://github.com/whitequark/Glasgow/blob/master/software/glasgow/__init__.py

import asyncio
import os
import sys
import logging
import argparse
from argparse import RawTextHelpFormatter

import subprocess
from .applets import *
from .device import *

def build(args):
    device_cls = KilsythDevice.all[args.device]
    applet_cls = KilsythApplet.all[args.applet]

    device = device_cls()
    applet = applet_cls(device, args=args)
    device.build(applet, toolchain_path='/usr/share/trellis')

def run(args):
    device_cls = KilsythDevice.all[args.device]
    applet_cls = KilsythApplet.all[args.applet]

    device = device_cls()
    applet = applet_cls(device, args=args)

    # Don't forget me!
    if False:
        device.build(applet, toolchain_path='/usr/share/trellis')

        # TODO fix irmask. Move to device
        script = "; ".join([
            "jtag newtap device tap -expected-id %s -irlen 8 -irmask 0xFF -ircapture 0x1" % (device.idcode),
            "transport select jtag",
            "adapter_khz 10000",
            "init",
            "svf -tap device.tap -quiet -progress %s" % ("build/top.svf"),
            "exit",
        ])

        # TODO turn into an argument
        openocd_interface = "interface/ftdi/dp_busblaster.cfg"
        subprocess.call(["openocd", "-f", openocd_interface, "-c", script])

    asyncio.run(applet.run())

def main():
    print("KILSYTH [WIP]")

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-v", "--verbose", default=0, action="count",
        help="increase logging verbosity")

    parser.add_argument('--device', 
        choices=KilsythDevice.all.keys(),
        help="which device to target",
        default="rev_a_12") # todo fix this

    subparsers = parser.add_subparsers(dest="action", metavar="COMMAND")
    subparsers.required = True

    p_run = subparsers.add_parser(
        "run",
        description="Builds and loads an applet bitstream",
        help="builds and loads an applet bitstream")
    p_run_applet = p_run.add_subparsers(dest="applet", metavar="APPLET")
    for applet in KilsythApplet.all.values():
        subparser = p_run_applet.add_parser(
            applet.name,
            description=applet.description,
            help=applet.help,
            formatter_class=RawTextHelpFormatter)
        applet.add_build_arguments(subparser)
        applet.add_run_arguments(subparser)

    p_build = subparsers.add_parser(
        "build",
        description="Builds an applet bitstream",
        help="builds an applet bitstream")
    p_build_applet = p_build.add_subparsers(dest="applet", metavar="APPLET")
    for applet in KilsythApplet.all.values():
        subparser = p_build_applet.add_parser(
            applet.name,
            description=applet.description,
            help=applet.help)
        applet.add_build_arguments(subparser)

    p_test = subparsers.add_parser(
        "test",
        description="Tests an applet",
        help="tests an applet")
    p_test_applet = p_test.add_subparsers(dest="applet", metavar="APPLET")
    for applet in KilsythApplet.all.values():
        subparser = p_build_applet.add_parser(
            applet.name,
            description=applet.description,
            help=applet.help)
        applet.add_test_arguments(subparser)

    args = parser.parse_args()
    print(args)

    if args.action == "run":
        run(args)
    elif args.action == "build":
        build(args)
    elif args.action == "test":
        print("Not implemented.")
