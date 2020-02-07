from time import perf_counter
import numpy as np
from math import sin
from Adafruit.MCP4725 import MCP4725
from dacdemo import setV, VDD

dac = MCP4725(busnum=1)

frequency = 25

t0 = perf_counter()
while True:
    t = perf_counter() - t0
    setV(dac, sin(2 * pi * frequency * t) + 1)
