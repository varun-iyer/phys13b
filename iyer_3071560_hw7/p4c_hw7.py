import sys
import time
import numpy as np
import matplotlib.pyplot as plt
from Adafruit import ADS1x15
from pwm import set_duty
adc = ADS1x15()
a = -0.048
b = 0.0001
T0 = 23.265 + 273.15
R0 =  107682.260

setpoint = 0
try:
    setpoint = float(sys.argv[1])
except:
    print("USAGE: python3 p4d_hw7.py SETPOINT\n where SETPOINT is desired temp in K")
    sys.exit()

try:
    while True:
       vin = adc.readADCDifferential01(4096, 128)*0.001  # returns float
       vout = adc.readADCDifferential23(4096, 128)*0.001  # returns float
       current = vout / 100e3
       resistance = (vin - vout) / current
       power = (vin - vout) ** 2 / resistance
       temp = (-a - np.sqrt(a ** 2 + 4 * b * np.log(resistance / R0))) / (2 * b) + T0
       set_duty(1 if temp < setpoint else 0)
