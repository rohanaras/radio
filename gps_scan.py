from __future__ import print_function
import serial
import pynmea2
import time
import os

import gps

from dotenv import load_dotenv
load_dotenv(verbose=True)

def gps_scan():
	found = helper()
	if found:
		return {
			"lat": found["lat"],
			"lon": found["lon"],
			"alt": found["alt"]
		}
 
def get_time():
    found = helper()
    if found:
        return found["time"]

def helper():
	# Setting initial terms so we can run scans
	counter = 0
	initial_terms = 0
	returning = {}
	print('Initiating GPS scan...')
	while counter < int(os.getenv("GPS_SCANS", 3)):
		counter += 1
		gps_data = gps.gather()
		if gps_data:
			ts = bool(gps_data["time"])
			lat = bool(gps_data["lat"])
			lon = bool(gps_data["lon"])
			alt = bool(gps_data["alt"])
		else:
			ts = lat = lon = alt = False

		count = ts + lat + lon + alt
		if count > initial_terms:
			returning = gps_data
			initial_terms = count
	
	return returning

if __name__ == "__main__":
    gps_scan()