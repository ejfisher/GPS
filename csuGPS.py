import time
import board
import busio
import serial
import adafruit_gps



def init():
	# for a computer, use the pyserial library for uart access
	uart = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=10)
	 
	# Create a GPS module instance.
	gps = adafruit_gps.GPS(uart, debug=False)     # Use UART/pyserial
	print(type(gps)) 
	# Turn on the basic GGA and RMC info (what you typically want)
	gps.send_command(b'PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0')

	# Set update rate to once a second (1hz) which is what you typically want.
	gps.send_command(b'PMTK220,1000')
	# This would be twice a second (2hz, 500ms delay):
	# gps.send_command(b'PMTK220,500')
	return gps

def acquire(gps):

	gps.update()
	if not gps.has_fix:
	# Try again if we don't have a fix yet.
		print('Waiting for fix...')
		#continue
	# We have a fix! (gps.has_fix is true)
	# Print out details about the fix like location, date, etc.
	print('=' * 40)  # Print a separator line.
	print('Fix timestamp: {}/{}/{} {:02}:{:02}:{:02}'.format(gps.timestamp_utc.tm_mon, gps.timestamp_utc.tm_mday, gps.timestamp_utc.tm_year, gps.timestamp_utc.tm_hour, gps.timestamp_utc.tm_min, gps.timestamp_utc.tm_sec))
	print('Latitude: {0:.6f} degrees'.format(gps.latitude))
	print('Longitude: {0:.6f} degrees'.format(gps.longitude))
	print('Fix quality: {}'.format(gps.fix_quality))
	# Some attributes beyond latitude, longitude and timestamp are optional
	# and might not be present.  Check if they're None before trying to use!
	if gps.satellites is not None:
		print('# satellites: {}'.format(gps.satellites))
	if gps.altitude_m is not None:
		print('Altitude: {} meters'.format(gps.altitude_m))
	if gps.speed_knots is not None:
		print('Speed: {} knots'.format(gps.speed_knots))
	if gps.track_angle_deg is not None:
		print('Track angle: {} degrees'.format(gps.track_angle_deg))
	if gps.horizontal_dilution is not None:
		print('Horizontal dilution: {}'.format(gps.horizontal_dilution))
	if gps.height_geoid is not None:
		print('Height geo ID: {} meters'.format(gps.height_geoid))