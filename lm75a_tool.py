# -*- coding: utf-8 -*-
"""
LM75A_tool
~~~~~~~~~~~~~
:license: MIT
"""
import sys
import argparse

def parse_args(in_args):
    """
    Parses arguments and passes them to the main function
    """
    parser = argparse.ArgumentParser(description='Set the temperature ranges for LM75A')

    parser.add_argument(
    '-a', '--addr',
    help='LM75A address',
    dest='addr',
    default=0x4f)

    parser.add_argument(
    '-b', '--bus',
    help='LM75A bus number',
    dest='bus',
    default='1')

    parser.add_argument(
    '-O', '--os',
    help='Higher temperature treshold',
    dest='os',
    default='80')

    parser.add_argument(
    '-H', '--hyst',
    help='Lower temperature treshold',
    dest='hyst',
    default='75')

    return parser.parse_args(in_args)


class LM75A_tool():
    def __init__(self, args: str):
        self._addr = int(args.addr)
        self._bus = args.bus
        self._os = args.os
        self._hyst = args.hyst
        self.i2c_bus = smbus.SMBus(int(self._bus))

    def show_config(self):
        raw = self.i2c_bus.read_word_data(self._addr, 3) & 0xFFF
        print ("{0:b} binary & {0:f} read from OS".format(raw))
        raw = self.i2c_bus.read_word_data(self._addr, 2) & 0xFFF
        print ("{0:b} binary & {0:f} read from HYST".format(raw))

    def show_temp(self):
        raw = self.i2c_bus.read_word_data(self._addr, 0) & 0xFFF
        print ("{0:b} binary & {0:f} Celsius".format(raw))

    def set_overtemp(self):
        self.i2c_bus.write_word_data(self._addr, 3, int(self._os))

    def set_hyst(self):
        self.i2c_bus.write_word_data(self._addr, 2, int(self._hyst))

if __name__ == "__main__":
    try:
        import smbus
    except ImportError:
        print("Need to install 'smbus'")
        exit()

    args = parse_args(sys.argv[1:])
    tool = LM75A_tool(args)

    print("Previous config")
    tool.show_config()
    tool.set_overtemp()
    tool.set_hyst()
    print("Current config")
    tool.show_config()
    print("The temperature is:")

    tool.show_temp()
