import csuGPS
import time

gps = csuGPS.init()

while True:
	csuGPS.acquire(gps)
	time.sleep(1)
