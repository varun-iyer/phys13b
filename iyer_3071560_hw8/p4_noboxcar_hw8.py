import sys
import time
import numpy as np
import matplotlib.pyplot as plt
from Adafruit import ADS1x15
from pwm import set_duty
import rtd
adc = ADS1x15()
a = -0.048
b = 0.0001
T0 = 23.265 + 273.15
R0 =  107682.260
temperature = []
rtd_temp = []
t = []
t0 = time.time()

def duty(target):
    return ((target - 30 - 273)/30) * (0.11-0.08) + 0.08

setpoint = 0
try:
    setpoint = float(sys.argv[1])
except:
    print("USAGE: python3 p2_hw8.py SETPOINT\n where SETPOINT is desired temp in K")
    sys.exit()

try:
    while True:
       vin = adc.readADCDifferential01(4096, 128)*0.001  # returns float
       vout = adc.readADCDifferential23(4096, 128)*0.001  # returns float
       current = vout / 100e3
       resistance = (vin - vout) / current
       power = (vin - vout) ** 2 / resistance
       temp = (-a - np.sqrt(a ** 2 + 4 * b * np.log(resistance / R0))) / (2 * b) + T0
       set_duty(duty(setpoint) if temp < setpoint else 0)
       if len(t) < 1 or time.time() > t[-1] + 1 + t0:
           t.append(time.time() - t0)
           rtd_temp.append(rtd.get())
           temperature.append(temp)
           print("Resistance: {} Ohms Power: {} J Temperature: {} K".format(resistance, power, temp))
except KeyboardInterrupt:
    set_duty(0)
    plt.plot(t, temperature)
    plt.plot(t, rtd_temp)
    plt.xlabel("Time (s)")
    plt.ylabel("Temperature (K)")
    plt.show()
    try:
        np.savetxt(sys.argv[2], np.vstack((t, rtd_temp, temperature)))
    except IndexError:
        pass
