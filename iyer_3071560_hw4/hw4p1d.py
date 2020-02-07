"""
Ramps the voltage up from 0 to 3.3 in incremends of one.
Takes two differential readings at each step.
Saves data in a numpy array
"""
from time import sleep
import numpy as np
from dacdemo import setV, mcp4725, VDD
from Adafruit import ADS1x15

dac = mcp4725(busnum=1)
adc = ADS1x15()

while True:
    v = input("enter desired dac voltage>")
    try:
        v = float(v)
    except:
        print("voltage must be numerical")
        cotinue
    if v > VDD or v < 0:
        print("voltage out of range")
        continue
    setV(dac, d)
    sleep(0.1)
    print("op-amp pin1: {}".format(adc.readADCDifferential01(4096, 128) * 0.001)
    print("op-amp vout: {}".format(adc.readADCDifferential23(4096, 128) * 0.001))
