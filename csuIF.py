import csuGPS
import time

#gps = csuGPS.init()
#print(type(gps))

while True:
	csuGPS.acquire()
	time.sleep(1)
