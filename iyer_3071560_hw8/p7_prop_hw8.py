import sys
from collections import deque
import time
import numpy as np
import matplotlib.pyplot as plt
from Adafruit import ADS1x15
import heat
from pwm import set_duty

TINTERVAL = 1 # time interval in seconds
temperature = []
box_temp = deque()
t = []
t0 = time.time()
Kp = 0.05
P0 = 0.02

def duty(target, current):
    if current > target:
        return 0
    return min(Kp * (target - current) + P0, 1)


setpoint = 0
try:
    setpoint = float(sys.argv[1])
except:
    print("USAGE: python3 p2_hw8.py SETPOINT\n where SETPOINT is desired temp in K")
    sys.exit()

try:
    while True:
        resistance, power, temp = heat.get_rpt()

        box_temp.append(temp)
        if time.time() - TINTERVAL > t0:
            box_temp.popleft()

        mtemp = sum(list(box_temp)) / len(box_temp)
        set_duty(duty(setpoint, mtemp))

        if len(t) < 1 or time.time() > t[-1] + 5 + t0:
            t.append(time.time() - t0)
            temperature.append(temp)
            print("Resistance: {} Ohms Power: {} J Temperature: {} K".format(resistance, power, temp))

except KeyboardInterrupt:
    set_duty(0)
    plt.plot(t, temperature)
    plt.xlabel("Time (s)")
    plt.ylabel("Temperature (K)")
    plt.show()
    np.savetxt(sys.argv[2], np.vstack((t, temperature)))
