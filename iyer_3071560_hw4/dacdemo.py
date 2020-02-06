#!/usr/bin/env python3
#
# dacdemo.py - Digital to analog converter demo with MCP4725
#
# 07Feb19  Fixed off-by-one error in MAXN
# 30Jan18  Increased resolution of print command
# 26Jul16  Adapted from Adafruit code by Everett Lipman
#

import time

VDD = 3.3
MAXN = 4095
NSTEPS = 4
DELAY = 3  # seconds

#
# Adafruit library
#
from Adafruit.MCP4725 import MCP4725 as mcp4725
##############################################################################

def setV(thedac, V):
   """Set output voltage of specified DAC to V

      thedac is the mcp4725 class instance
      V is the voltage.  V will be clipped if out of range.
   """
   if V > VDD:
      V = VDD
   if V < 0:
      V = 0

   vnum = int(MAXN*V/VDD)

   thedac.set_voltage(vnum)
##############################################################################

if __name__ == '__main__':

   print()

   #
   # Default address is 0x62, on I2C bus #1.
   #
   # Alternative: mcp4725(address=0x49, busnum=N).
   #
   dac0 = mcp4725(busnum=1)

   nsmo = NSTEPS - 1.0
   while True:
      for i in range(NSTEPS):
         vout = (i/nsmo)*VDD
         print('Setting voltage to %.4f.' % vout)
         setV(dac0, vout)
         time.sleep(DELAY)
