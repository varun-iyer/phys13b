#!/usr/bin/env python3

#
# rtddemo.py - Platinum RTD sensor demonstration
#
# 16Feb19  Everett Lipman
#

USAGE="""
usage: rtddemo.py

   Prints out RTD readings continuously.
"""

import time

import board
import digitalio
import busio
import adafruit_max31865 as max3

spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
cs = digitalio.DigitalInOut(board.D5)
rtd_sensor = max3.MAX31865(spi, cs, wires=3, rtd_nominal=100.0, ref_resistor=430.0)
###############################################################################

while(True):
   T = rtd_sensor.temperature

   print('RTD: T = %.3f' % T)

   time.sleep(0.5)
