import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

time, temp = np.loadtxt("p1_data_hw7.txt")
fn = lambda t, t0, c, tc, x0: t0 * np.exp(-(t-x0) / tc) + c
cf = curve_fit(fn, time, temp, p0=[200, 100, 120, 0])

# mixing python formatting characters and inline latex: VERY HARD
# typing in numbers after you run your program once: VERY EASY
# https://xkcd.com/1495/
plt.plot(time, fn(time, *cf[0]),
         label="Temp = $119.97 e^{-(t + 199.13)/186.42} + 300.16$")
plt.scatter(time, temp, color="orange", label="Measured temp")
plt.xlabel("Time (s)")
plt.ylabel("Temperature (K)")
plt.legend()
plt.show()
