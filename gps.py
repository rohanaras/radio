from __future__ import print_function
# Simple GPS module demonstration.
import time
import board
import busio

import adafruit_gps

# for a computer, use the pyserial library for uart access
import serial

def connection():
    uart = serial.Serial("/dev/serial0", baudrate=9600, timeout=10)
    gps = adafruit_gps.GPS(uart, debug=False)
    return ( uart, gps )

def setup():
    ( uart, gps ) = connection()  # Use UART/pyserial
    gps.send_command(b'PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0')
    # Set update rate to once a second (1hz) which is what you typically want.
    gps.send_command(b'PMTK220,1000')

# Main loop runs forever printing the location, etc. every second.
def gather():
    ( uart, gps ) = connection()
    gps.update()
    if gps.has_fix:
        return {
            "time": gps.timestamp_utc,
            "lat": gps.latitude,
            "lon": gps.longitude,
            "alt": gps.altitude_m
        }
    else:
        return None