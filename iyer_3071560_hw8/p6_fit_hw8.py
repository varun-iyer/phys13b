import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

tmpr, res = np.loadtxt("p5_data_hw8.txt")
 
# from p1
R0 = 109529.86
T0 = 23.67119 + 273.15
 
fn = lambda t, a, b: R0 * np.exp(a * (t - T0) + b * (t-T0)**2)
 
par, cov = curve_fit(fn, tmpr, res, p0=[-0.048, 0.0001])
print("alpha: {}, beta {}".format(*par))

plt.scatter(tmpr, res)
x = np.arange(min(tmpr) - 5, max(tmpr) + 5, 0.1)
plt.plot(x, fn(x, *par), color="orange")
plt.xlabel("Resistance (Ohms)")
plt.ylabel("Temperature (Kelvin)")
plt.show()
