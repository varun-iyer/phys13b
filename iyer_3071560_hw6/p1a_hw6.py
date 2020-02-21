import numpy as np
import matplotlib.pyplot as plt

f = 0
while True:
    try:
        f = float(input("Enter signal frequency:"))
    except ValueError:
        print("Signal must be a floating point number!")
    break

period = 1/f
pds = 20 * period
plot_f = 64 * f
signal_t = np.arange(0, pds, 1/plot_f)
signal = np.sin(2 * np.pi * f * signal_t) + 1

sample_f = 920
sample_t = np.arange(0, pds, 1/sample_f)
sample = np.sin(2 * np.pi * f * sample_t) + 1

plt.plot(signal_t, signal, label="{} Hz Signal".format(f))
plt.scatter(sample_t, sample, c='orange', marker='o', s=60, label="{} Hz Sampling".format(sample_f))
plt.xlabel("Time (s)")
plt.ylabel("Voltage (V)")
plt.legend(loc="upper right")

plt.savefig("p1a_hw6_{}hz.eps".format(int(f)), format="eps")
plt.show()
