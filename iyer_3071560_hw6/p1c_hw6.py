import numpy as np
import matplotlib.pyplot as plt

f = np.array([260, 360, 410, 440, 450, 460, 470, 480, 510, 560, 660])
a = np.array([0.431, 0.350, 0.325, 0.307, 0.300, 0.293, 0.285, 0.280, 0.261, 0.226, 0.156])

plt.scatter(f, a)
plt.xlabel("Input Frequency (Hz)")
plt.ylabel("Output Amplitude (V)")
plt.show()
