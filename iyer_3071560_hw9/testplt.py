#!/usr/bin/python3
import matplotlib.pyplot as plt
import numpy as np
import sys
t, k = np.loadtxt(sys.argv[1])
plt.plot(t-t[0], k)
plt.xlabel("Time (s)")
plt.ylabel("Temperature (K)")
plt.show()
