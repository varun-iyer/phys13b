import sys
import time
from collections import deque
import numpy as np
import matplotlib.pyplot as plt
import heat
from pwm import set_duty
import rtd


TINTERVAL = 2 # time interval in seconds
EPSILON = 0.1

def duty(target):
    return ((target-30-273)/30) * (0.11 - 0.08) + 0.08


def test_temp(target):
    t0 = time.time()
    box_temp = deque()
    box_mtemp = deque()
    box_rtd = deque()
    prev = 0
    while True:
        temp = heat.get()
        box_temp.append(temp)
        mtemp = sum(list(box_temp)) / len(box_temp)
        box_mtemp.append(mtemp)
        box_rtd.append(rtd.get())
        if time.time() - TINTERVAL > t0:
            box_mtemp.popleft()
            box_rtd.popleft()
            box_temp.popleft()

        ep = np.array(list(box_mtemp))
        ep -= target
        ep = np.abs(ep)
        if np.all(ep < EPSILON) and time.time() - TINTERVAL > t0:
            # only get second half bc of the lag
            box_rtd = list(box_rtd)[len(box_rtd)//2:]
            rtdtemp = sum(list(box_rtd)) / len(box_rtd)
            print("Read {} from RTD for {}".format(rtdtemp, target))
            return rtdtemp
        set_duty(duty(target) if mtemp < target else 0)
        print(mtemp)


temp = []
res = []
try:
    for temperature in range(273+30, 273+60, 5):
        print("Testing {}".format(temperature))
        rtdtemp = test_temp(temperature)
        resistance = heat.get_resistance()
        print("Resistance {} at Temp {}, nominally {}".format(resistance, rtdtemp, temperature))
        temp.append(rtdtemp)
        res.append(resistance)
except KeyboardInterrupt:
    set_duty(0)
    sys.exit()
set_duty(0)
np.savetxt("p5_calibration_hw8.txt", np.vstack((temp, res)))
