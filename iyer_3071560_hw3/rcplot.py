>>> xycut=(xy.T[xy[1] > 0.04]).T
>>> xycut.shape
(2, 17570)
>>> plt.scatter(*xycut)
<matplotlib.collections.PathCollection object at 0xb29fdd10>
>>> plt.show()
>>> par, cov = curve_fit(rctime, *xycut)
>>> par
array([1.06839355, 1.91541932])
>>> cov
array([[1.60781885e-05, 1.12666052e-06],
       [1.12666052e-06, 5.74262092e-07]])
>>> plt.scatter(*xycut)
<matplotlib.collections.PathCollection object at 0xb29b2d90>
>>> plt.plot(xycut[0], rctime(xycut[0], *par))
[<matplotlib.lines.Line2D object at 0xb29b71b0>]
>>> plt.show()
>>> rctime = lambda t, rc, t0: 2 * (1 - np.exp(-(t-t0)/rc))
>>> par, cov = curve_fit(rctime, *xycut)
>>> par
array([0.47199902, 0.86138985])
>>> cov
array([[ 1.02889393e-05, -6.02194352e-06],
       [-6.02194352e-06,  6.09677273e-06]])
>>> plt.scatter(*xycut)
<matplotlib.collections.PathCollection object at 0xb296c3b0>
>>> plt.plot(xycut[0], rctime(xycut[0], *par), color="yellow")
[<matplotlib.lines.Line2D object at 0xb296c7b0>]
>>> plt.show()
>>> rctime = lambda t, rc, t0, v: v * (1 - np.exp(-(t-t0)/rc))
>>> par, cov = curve_fit(rctime, *xycut)
>>> plt.scatter(*xycut)
<matplotlib.collections.PathCollection object at 0xb298c390>
>>> plt.plot(xycut[0], rctime(xycut[0], *par), color="orange")
[<matplotlib.lines.Line2D object at 0xb2985e30>]
>>> plt.x
plt.xcorr(   plt.xkcd(    plt.xlabel(  plt.xlim(    plt.xscale(  plt.xticks(
>>> plt.x
plt.xcorr(   plt.xkcd(    plt.xlabel(  plt.xlim(    plt.xscale(  plt.xticks(
>>> plt.xlabel("Voltage across Capacitor (V)")
Text(0.5, 0, 'Voltage across Capacitor (V)')
>>> plt.ylabel("Time (s)")
Text(0, 0.5, 'Time (s)')
>>> plt.ti
plt.tick_params(       plt.ticklabel_format(  plt.tight_layout(      plt.time               plt.title(
>>> plt.title("RC Circuit Time Constant Determination")
Text(0.5, 1.0, 'RC Circuit Time Constant Determination')
>>> plt.show()
>>> ls
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'ls' is not defined
>>> par
array([0.37280769, 0.8935066 , 1.90373165])
>>> cov
array([[ 3.94282190e-10, -2.01642374e-10,  2.00092158e-11],
       [-2.01642374e-10,  1.98691116e-10, -5.33052812e-12],
       [ 2.00092158e-11, -5.33052812e-12,  2.49934482e-11]])
>>>

