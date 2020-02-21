import sys
import time
from Adafruit import ADS1x15
adc = ADS1x15()
while True:
   vin = adc.readADCDifferential01(4096, 128)*0.001  # returns float
   vout = adc.readADCDifferential23(4096, 128)*0.001  # returns float
   current = vout / 100e3
   resistance = (vin - vout) / current
   power = (vin - vout) ** 2 / resistance
   print("Resistance: {} Ohms Power: {} J".format(resistance, power))
   time.sleep(1)
