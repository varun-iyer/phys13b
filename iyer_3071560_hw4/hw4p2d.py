from time import perf_counter
import numpy as np
from Adafruit.MCP4725 import MCP4725
from dacdemo import setV, VDD, MAXN

dac = MCP4725(busnum=1)

frequency = 25

lut = np.sin(np.arange(0, 2 * np.pi, 0.01))

w = 2 * np.pi * frequency

t0 = perf_counter()

while True:
    t = perf_counter() - t0
    dac.set_voltage(int(MAXN * (lut[int(100 * (w * t)) % len(lut)] + 1)/VDD))
