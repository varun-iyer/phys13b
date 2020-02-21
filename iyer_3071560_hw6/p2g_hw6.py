import numpy as np
import sys
import time
from Adafruit import ADS1x15
adc = ADS1x15()
a = -0.048
b = 0.0001
T0 = 110
R0 =  11267
while True:
   vin = adc.readADCDifferential01(4096, 128)*0.001  # returns float
   vout = adc.readADCDifferential23(4096, 128)*0.001  # returns float
   current = vout / 100e3
   resistance = (vin - vout) / current
   power = (vin - vout) ** 2 / resistance
   temp = -a + np.sqrt(a ** 2 + 4 * b * np.log(resistance / R0)) / (2 * b) + T0
   print("Resistance: {} Ohms Power: {} J Temperature: {} K".format(resistance, power, temp))
   time.sleep(1)
