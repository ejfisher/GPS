import csuGPS
import time
import adafruit_gps
#gps = csuGPS.init()
#print(type(gps))

csuGPS.init()
time, gpsData,gpsQuality = csuGPS.acquire()
print('=' * 40)  # Print a separator line.
print('Fix timestamp: {0[0]:02}:{0[1]:02}:{0[2]:02} '.format(time))
print('Latitude: {0[0]:.6f} degrees\nLongitude: {0[1]:.6f} degrees'.format(gpsData))
print('Fix quality: {0[0]}\n# satellites: {0[1]}'.format(gpsQuality))