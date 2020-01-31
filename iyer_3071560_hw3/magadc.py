from Adafruit import ADS1x15
from sys import stdout

SPS = 250 # samples per sec, 128, 250, 490, 920, 1600, 2400, 3300
VRANGE = 4096 # range; 256, 512, 1024, 2048, 6144
adc = ADS1x15()
adc.startContinuousDifferentialConversion(2, 3, pga=VRANGE, sps=SPS)

a = np.zeros(250 * 10)

while True:
	stdout.write("{} V\r".format(0.001 * adc.getLastConversionResults()))

np.save("magdata.npy", a)
