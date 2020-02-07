import sys
import numpy as np
import matplotlib.pyplot as plt

try:
    dacv, pin1, vout = np.loadtxt(sys.argv[1])
except IndexError:
    print("usage: python3 hw4p1b_plot.py /path/to/data.txt /path/to/save.eps")

i_res = (pin1 - vout) / 98.0
plt.plot(vout, i_res)
plt.xlabel("Voltage Across LED (V)")
plt.ylabel("Current Through LED (A)")
 
try:
    plt.savefig(sys.argv[2], format="eps")
    print("Plot saved to {}.".format(sys.argv[2]))
except IndexError:
    print("usage: python3 hw4p1b_plot.py /path/to/data.txt /path/to/save.eps")
