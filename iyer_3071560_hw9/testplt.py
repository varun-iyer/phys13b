#!/usr/bin/python3
import matplotlib.pyplot as plt
import numpy as np
import sys
plt.plot(*np.loadtxt(sys.argv[1]))
plt.show()
