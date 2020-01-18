import csuGPS
import csuI2C
#gps = csuGPS.init()
#print(type(gps))

csuGPS.init()
csuI2C.init()
# Return Tuples for aquire are in the format
# time = (utc-hr, utc-min, utc-sec)
# gpsData = (Latitude, Longitude, Altitude, Speed, TAD, HD)
# gpsQuality = (fix-quality, # of Sattelites)
time, gpsData,gpsQuality = csuGPS.acquire()
print('=' * 40)  # Print a separator line.
print('Fix timestamp: {0[0]:02}:{0[1]:02}:{0[2]:02} '.format(time))
print('Latitude: {0[0]:.6f} degrees\nLongitude: {0[1]:.6f} degrees\nAltitude: {0[2]} meters'.format(gpsData))
print('Fix quality: {0[0]}\n# satellites: {0[1]}'.format(gpsQuality))