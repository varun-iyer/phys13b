import sys
import time
import heat
import numpy as np
import matplotlib.pyplot as plt
from pwm import set_duty
import rtd

def duty(target):
    return ((target - 30 - 273)/30) * (0.11-0.08) + 0.08

setpoint = 0
try:
    setpoint = float(sys.argv[1])
except:
    print("USAGE: python3 p2_hw8.py SETPOINT\n where SETPOINT is desired temp in K")
    sys.exit()

try:
    temperature = []
    rtd_temp = []
    t = []
    t0 = time.time()
    while True:
        tee0 = time.time()
        set_duty(0.5)
        while time.time() - 1 < tee0:
           resistance, power, temp = heat.get_rpt()
           if len(t) < 1 or time.time() > t[-1] + .1 + t0:
               rtd_temp.append(rtd.get())
               temperature.append(temp)
               t.append(time.time() - t0)
               print("temp: {}K".format(temp))
        set_duty(0)
        while heat.get() > setpoint:
           if len(t) < 1 or time.time() > t[-1] + .1 + t0:
               temp = rtd.get()
               rtd_temp.append(rtd.get())
               temperature.append(heat.get())
               t.append(time.time() - t0)
               print("temp: {}K".format(temp))
except KeyboardInterrupt:
    set_duty(0)
    temperature = temperature[:len(t)]
    rtd_temp = rtd_temp[:len(t)]
    plt.plot(t, temperature)
    plt.plot(t, rtd_temp)
    plt.xlabel("Time (s)")
    plt.ylabel("Temperature (K)")
    plt.show()
    try:
        np.savetxt(sys.argv[2], np.vstack((t, rtd_temp, temperature)))
    except IndexError:
        pass
