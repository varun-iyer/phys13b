"""
Ramps the voltage up from 0 to 3.3 in incremends of one.
Takes two differential readings at each step.
Saves data in a numpy array
"""
from time import sleep
import numpy as np
from dacdemo import setV, mcp4725
from Adafruit import ADS1x15
import sys

dacv = np.arange(0, 3.4, 0.1)
pin1 = np.zeros(dacv.shape[0])
vout = np.zeros(dacv.shape[0])

dac = mcp4725(busnum=1)
adc = ADS1x15()

for i, d in enumerate(dacv):
	setV(dac, d)
	sleep(0.1)
	pin1[i] = adc.readADCDifferential01(4096, 128) * 0.001
	vout[i] = adc.readADCDifferential23(4096, 128) * 0.001

dpv = np.vstack((dacv, pin1, vout))
np.save(sys.argv[1], dpv)
