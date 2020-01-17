import csuGPS
import time

csuGPS.init()

while True:
	csuGPS.acquire()
	time.sleep(1)
