import numpy as np
import matplotlib.pyplot as plt

dacv, pin1, vout = np.load("hw4p1b.npy")
i_res = (pin1 - vout) / 98.0

plt.plot(vout, i_res)
plt.show()
