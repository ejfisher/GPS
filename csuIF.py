import csuGPS
import time

gps = csuGPS.init()
type(gps)

while True:
	csuGPS.acquire(gps)
	time.sleep(1)
