import sys
from collections import deque
import numpy as np
import pwm
from pwm import set_led
from accel import Lis3dh

STACKSIZE = 100
MAX_ACCEL = 50 # m/s^2

acc = Lis3dh()
# Easier to do two stacks than recompute
# could have used like a ring buffer but *shrug*
vstack = deque(iterable=[0]*STACKSIZE, maxlen=STACKSIZE) # stack of vectors
mstack = deque(iterable=[0]*STACKSIZE, maxlen=STACKSIZE) # stack of magnitudes

try:
    print("Calibrating...")
    for i in range(STACKSIZE):
        data = acc.read_accel()
        print(data)
        # deque doesn't like numpy arrays
        vstack.append(list(data))
        norm = np.sqrt(data.dot(data))
        mstack.append(norm)

    g = np.average(vstack, axis=0)
    std = np.std(mstack)
    print("Ready.")
    print("Measured g: {} Measured std: {}".format(g, std))

    i = 0
    while True:
        data = acc.read_accel()
        vstack.append(list(data))
        data = data - g
        norm = np.sqrt(data.dot(data))
        mstack.append(norm)
        set_led(norm/MAX_ACCEL)
        if i % 20 == 0: # only do a relatively expensive test once in a while
            print("Read {}".format(norm))
            if np.std(mstack) <= 2 * std: # if its stationary, then reset g
                print("Reset g")
                g = np.average(vstack, axis=0)
        i += 1
except KeyboardInterrupt:
    set_led(0)
    sys.exit(0)
