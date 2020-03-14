import matplotlib.pyplot as plt
import numpy as np

timemag = np.load("magdata.npy")
plt.plot(*timemag)
plt.xlabel("Time (s)")
plt.ylabel("Voltage (V)")
plt.show()
