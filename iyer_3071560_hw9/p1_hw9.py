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
def duty(target, current):
    if current > target:
        return 0
    d = min(Kp * (target - current) + P0, 1)
    d = max(Kp * (target - current) + P0, 0)
    return d


BOXT = 1 # boxcar time interval in seconds
tque = deque()
kque = deque()


def control():
    last = 0
    while True:
        tque.append(time.time())
        kque.append(heat.get())

        if tque[-1] > last + 1:
            cplt.add(tque[-1], kque[-1])
            last = tque[-1]

        mtemp = sum(list(kque)) / len(kque)
        set_duty(duty(setpoint, mtemp))

        while tque[0] + BOXT < tque[-1]:
            tque.popleft()
            kque.popleft()


thread.start_new_thread(control, ())
cplt.run()
