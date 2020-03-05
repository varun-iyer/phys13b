import sys
import time
import numpy as np
import matplotlib.pyplot as plt
from Adafruit import ADS1x15
from pwm import set_duty
adc = ADS1x15()
a = -0.048
b = 0.0001
T0 = 23.265 + 273.15
R0 =  107682.260
SAFETY = 317

setpoint = 0
try:
    setpoint = float(sys.argv[1])
except:
    print("USAGE: python3 p2_search_hw8.py SETPOINT\n where SETPOINT is desired temp in K")
    sys.exit()

 
def get_temp():
    vin = adc.readADCDifferential01(4096, 128)*0.001  # returns float
    vout = adc.readADCDifferential23(4096, 128)*0.001  # returns float
    current = vout / 100e3
    resistance = (vin - vout) / current
    power = (vin - vout) ** 2 / resistance
    temp = (-a - np.sqrt(a ** 2 + 4 * b * np.log(resistance / R0))) / (2 * b) + T0
    if temp >= SAFETY:
        set_duty(0)
        print("DANGEROUS TEMPERATURE READING; SHUTTING OFF")
        sys.exit(0)

 
def test_duty(duty, cycles=3):
    """ Finds max oscillations for a given duty cycle """
    set_duty(1)
    while get_temp() < setpoint:
        pass
    set_duty(0)
    while get_temp() > setpoint:
        pass

    oscillations = 0
    temperatures = []
    while oscillations < cycles:
        temp = get_temp()
        temperatures.append(temp)
        if temp < setpoint:
            set_duty(duty)
            oscillations += 1
        else:
            set_duty(0)
    t = np.array(temperatures)
    t -= setpoint
    max_ = np.max(np.abs(t))
    print("Tested {} with osc {}".format(duty, max_)

points = [0, 1]
while True:
    # binary search for the best duty cycle
    midpoint = np.mean([0, 1])
    lowtest = np.mean([points[0], midpoint])
    hightest = np.mean([points[1], midpoint])
    low_osc = test_duty(lowtest)
    high_osc = test_duty(hightest)
    osc = 0
    if low_osc <= high_osc:
        points = [points[0], midpoint]
        osc = low_osc
    else:
        points = [midpoint, points[1]]
        osc = high_osc
    print("Range {} with oscillation {} Celsius".format(points, osc))

except KeyboardInterrupt:
    set_duty(0)
    sys.exit()
