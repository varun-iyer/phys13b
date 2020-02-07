import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
 
xy = np.load("rcdata.npy")
xycut=(xy.T[xy[1] > 0.04]).T
 
rctime = lambda t, rc, t0: 2 * (1 - np.exp(-(t-t0)/rc))
par, cov = curve_fit(rctime, *xycut)
print(par)
plt.scatter(*xycut)
plt.plot(xycut[0], rctime(xycut[0], *par), color="orange")
plt.show()
 
rctime = lambda t, rc, t0, vf: vf * (1 - np.exp(-(t-t0)/rc))
par, cov = curve_fit(rctime, *xycut)
print(par)
plt.scatter(*xycut)
plt.plot(xycut[0], rctime(xycut[0], *par), color="orange")
plt.show()
