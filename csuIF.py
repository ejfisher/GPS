import csuGPS
import csuI2C
import csuDM
import time
#gps = csuGPS.init()
#print(type(gps))

csuGPS.init()
csuI2C.init()
# Return Tuples for aquire are in the format
# time = (utc-hr, utc-min, utc-sec)
# gpsData = (Latitude, Longitude, Altitude, Speed, TAD, HD)
# gpsQuality = (fix-quality, # of Sattelites)
while True:
	dNames = ['gpsTime.txt', 'gpsData.txt', 'gpsQuality.txt', 'acc.txt', 'mag.txt', 'gyro.txt', 'pressure.txt', 'altitude.txt', 'temperature.txt']
	for f in dNames:
		csuDM.init(f)
	bigData = [gpsTime, gpsData, gpsQuality, acc, mag, gyro, pressure, altitude, temperature]
	gpsTime, gpsData,gpsQuality = csuGPS.acquire()
	acc, mag, gyro, pressure, altitude, temperature  = csuI2C.acquire()

	#Take the aquired data and output to a file
	for i in range(9):
		csuDM.write(dNames[i], bigData[i])

	#display data aquired
	print('=' * 40)  # Print a separator line.
	print('Acceleration (m/s^2): ({0:0.3f},{1:0.3f},{2:0.3f})'.format(*acc))
	print('Magnetometer (uTesla): ({0:0.3f},{1:0.3f},{2:0.3f})'.format(*mag))
	print('Gyroscope (radians/s): ({0:0.3f},{1:0.3f},{2:0.3f})'.format(*gyro))
	print('=' * 40)  # Print a separator line.
	print('Fix timestamp: {0[0]:02}:{0[1]:02}:{0[2]:02} '.format(gpsTime))
	print('Latitude: {0[0]:.6f} degrees\nLongitude: {0[1]:.6f} degrees\nAltitude: {0[2]} meters'.format(gpsData))
	print('Fix quality: {0[0]}\n# satellites: {0[1]}'.format(gpsQuality))
	print('=' * 40)  # Print a separator line.
	print('Pressure: {0:0.3f} pascals'.format(pressure))
	print('Altitude: {0:0.3f} meters'.format(altitude))
	print('Temperature: {0:0.3f} degrees Celsius'.format(temperature))
	time.sleep(1)




print('=' * 40)  # Print a separator line.