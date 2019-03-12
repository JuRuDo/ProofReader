#!/bin/env python

from proofreader.netspeak import Netspeak
import sys


def main():
    netspeak = Netspeak()
    print(netspeak(sys.argv[1]))
    pass
