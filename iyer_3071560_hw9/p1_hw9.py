from threading import Thread
import sys
import atexit
from collections import deque
import time
import numpy as np
import heat
from pwm import set_duty
import cplt

atexit.register(set_duty, 0)

# really good:0.07
Kpc = -0.1
Tc = 32
Kp = Kpc * 0.6
Ti = Tc/2
Td = Tc/8
P0 = 0.02

def pid(p, i, d):
    dut = P0 + Kp * (p + (1/Ti) * i + Td * d)
    return min(1, max(dut, 0))

def pi(p, i, d):
    dut = P0 + Kp * (p + (1/Ti) * i)
    return min(1, max(dut, 0))

def pi_tune(p, i, d):
    dut = P0 + (0.45 * Kpc) * (p + (1.2/Tc) * i)
    return min(1, max(dut, 0))

def bang(p, i, d):
    return 1 if p < 0 else 0

def prop(p, i, d):
    dut = P0 + 0.5 * Kpc * p
    return min(1, max(dut, 0))


BOXT = 1 # boxcar time interval in seconds
tque = deque()
kque = deque()
dque = deque()

plot_t = []
plot_k = []


def control(alg, name, acqtime=0, target=318):
    last = 0

    integral = 0
    t0 = time.time()
    tque.append(time.time())
    kque.append(heat.get())

    while acqtime==0 or t0 > tque[-1] - acqtime:
        tque.append(time.time())
        kque.append(heat.get())
        plot_t.append(tque[-1])
        plot_k.append(kque[-1])

        if tque[-1] > last + 1:
            cplt.add(tque[-1], kque[-1])
            last = tque[-1]

        mtemp = kque[-1] # sum(list(kque)) / len(kque)
        dt = tque[-1] - tque[-2]
        dque.append((kque[-1] - kque[-2]) / dt)
        derivative = sum(list(dque)) / len(dque)
        integral += (kque[-1] - target)  * dt
        integral = max(min(integral, 60), -60)
        set_duty(alg(mtemp - target, integral, derivative))

        while tque[0] + BOXT < tque[-1]:
            tque.popleft()
            kque.popleft()
    np.savetxt(name, np.vstack((plot_t, plot_k))) 

thd = Thread(target=control, args=(pid, "p2a_pid_hw9.txt"))
thd.start()
cplt.run()
