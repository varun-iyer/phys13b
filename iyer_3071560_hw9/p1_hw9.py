import _thread as thread
import sys
import atexit
from collections import deque
import time
import numpy as np
import heat
from pwm import set_duty
import cplt

atexit.register(set_duty, 0)

setpoint = 0
try:
    setpoint = float(sys.argv[1])
except:
    print("USAGE: python3 p2_hw8.py SETPOINT\n where SETPOINT is desired temp in K")
    sys.exit()

Kp = 0.05
P0 = 0.02
Ti = 100
Td = 0
def duty(p, i, d):
    d = P0 + Kp * (p + (1/Ti) * i + Td * d)
    d = min(d, 1)
    d = max(d, 0)
    return min(1, max(d, 0))


BOXT = 1 # boxcar time interval in seconds
tque = deque()
kque = deque()


def control():

    last = 0

    integral = 0
    tque.append(time.time())
    kque.append(heat.get())

    while True:
        tque.append(time.time())
        kque.append(heat.get())

        if tque[-1] > last + 1:
            cplt.add(tque[-1], kque[-1])
            last = tque[-1]

        mtemp = tque[-1] # sum(list(kque)) / len(kque)
        dt = tque[-1] - tque[-2]
        derivative = (kque[-1] - kque[-2]) / dt
        integral += (setpoint - tque[-1])  * dt
        set_duty(duty(setpoint - mtemp, integral, derivative))

        while tque[0] + BOXT < tque[-1]:
            tque.popleft()
            kque.popleft()


thread.start_new_thread(control, ())
cplt.run()
