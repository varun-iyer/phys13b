import time
from threading import Lock
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from collections import deque

PLOT_TIME = 120 # number of time negative to plot in seconds

fig, ax = plt.subplots(1, 1)
plt.show(False)
plt.draw()

tque = deque()
kque = deque()
qmtx = Lock()

def add(time, temperature):
    qmtx.acquire(blocking=False)
    tque.append(time)
    kque.append(temperature)
    while tque[0] + PLOT_TIME < tque[-1]:
        qmtx.acquire(blocking=False)
        tque.popleft()
        kque.popleft()
    qmtx.release()

def draw(i, t, k):
    ax.clear()
    qmtx.acquire(blocking=False)
    plt.xlabel("Time (s)")
    plt.ylabel("Temperature (K)")
    ax.set_xlim([-PLOT_TIME, 0])
    a = None
    if t and k:
        a = ax.plot(np.array(list(t)) - t[-1], list(k))
    qmtx.release()
    return a

def run():
    ani = animation.FuncAnimation(fig, draw, fargs=(tque, kque), interval=100)
    plt.show()
