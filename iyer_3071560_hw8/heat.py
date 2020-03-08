import sys
import numpy as np
import pwm
from Adafruit import ADS1x15

adc = ADS1x15()
a = -0.048
b = 0.0001
T0 = 23.265 + 273.15
R0 =  107682.260
SAFETY = 373

def safe_exit():
    pwm.set_duty(0)
    sys.exit()

def get_rpt():
    vin = adc.readADCDifferential01(4096, 128)*0.001  # returns float
    vout = adc.readADCDifferential23(4096, 128)*0.001  # returns float
    current = vout / 100e3
    resistance = (vin - vout) / current
    power = (vin - vout) ** 2 / resistance
    temp = (-a - np.sqrt(a ** 2 + 4 * b * np.log(resistance / R0))) / (2 * b) + T0
    return resistance, power, temp

def get():
    vin = adc.readADCDifferential01(4096, 128)*0.001  # returns float
    vout = adc.readADCDifferential23(4096, 128)*0.001  # returns float
    current = vout / 100e3
    resistance = (vin - vout) / current
    power = (vin - vout) ** 2 / resistance
    temp = (-a - np.sqrt(a ** 2 + 4 * b * np.log(resistance / R0))) / (2 * b) + T0
    if temp > SAFETY:
        print("READ DANGEROUS TEMP; EXITING")
        safe_exit()
    return temp

def get_resistance():
    vin = adc.readADCDifferential01(4096, 128)*0.001  # returns float
    vout = adc.readADCDifferential23(4096, 128)*0.001  # returns float
    current = vout / 100e3
    resistance = (vin - vout) / current
    return resistance
