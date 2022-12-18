import asyncio
import datetime
from decimal import *

from machine import UART
from phew import logging

BAUD_RATE = 9600
READ_TIMEOUT_MS = 5000
FT_PER_METER = 3.2808

class Gps(object):
    def __init__(self):
        self.uart = None
        self.task = None

        self.last_latitude = None
        self.last_longitude = None
        self.last_altitude_m = None
        self.last_ground_speed_knots = None
        self.last_timestamp = None
        self.last_quality = None

    def start(self):
        uart = UART(1, BAUD_RATE, timeout=READ_TIMEOUT_MS)

        self.task = asyncio.create_task(self._read())

        self.uart = uart

    def stop(self):
        self.task.cancel("GPS read task canceled")
        self.task = None
        self.uart.deinit()

    def _parse_time(self, part):
        # 181908.00 is the timestamp (UTC in hours, minutes, and seconds)
        hours = int(part[0:2])
        minutes = int(part[2:4])
        seconds = int(part[4:6])
        microsecond = int(part[7:9])
        return datetime.time(hours, minutes, seconds, microsecond)

    def _parse_latitude(self, part, direction):
        # 3404.7041778 is the latitude in DDMM.MMMMM format, N denotes north latitude
        # Positive latitude is above the equator (N), and negative latitude is below the equator (S)
        return Decimal(part) * (-1 if direction == 'S' else 1)

    def _parse_longitude(self, part, direction):
        # 07044.3966270 is the longitude in DDDMM.MMMMM format, W denotes west longitude
        # Positive longitude is east of the prime meridian, while negative longitude is west of the prime meridian (a north-south line that runs through a point in England).
        return Decimal(part) * (-1 if direction == 'W' else 1)

    def _parse_altitude(self, part, unit):
        # 495.144 is the altitude of the GPS antenna, M is the unit of altitude (meters or feet)
        altitude_value = Decimal(part)
        return altitude_value if unit == "M" else unit * FT_PER_METER

    def _parse_speed(self, part):
        return Decimal(part)

    def _parse_course(self, part):
        return Decimal(part)

    def _parse_nmea_line(self, line):
        # parse line
        if not line or not str.startswith(line, "$"):
            logging.debug(f"Not a valid NMEA message {line}")
            return
        msg_parts = line.split(",")
        if msg_parts[0] == "$GPRMC":
            # RMC – Recommended minimum specific GNSS data
            self.last_timestamp = self._parse_time(msg_parts[1])
            self.last_latitude = self._parse_latitude(msg_parts[2], msg_parts[3])
            self.last_longitude = self._parse_longitude(msg_parts[4], msg_parts[5])
            self.last_quality = int(msg_parts[6])
            self.last_altitude_m = self._parse_altitude(msg_parts[9])

        elif msg_parts[0] == "$GPGGA":
            # GGA – Global positioning system (GPS) fix data
            self.last_timestamp = self._parse_time(msg_parts[1])
            self.last_latitude = self._parse_latitude(msg_parts[3], msg_parts[4])
            self.last_longitude = self._parse_longitude(msg_parts[5], msg_parts[6])
            self.last_ground_speed_knots = self._parse_speed(msg_parts[7])
            self.last_course = self._parse_course(msg_parts[8])

        # elif msg_parts[0] == "$GPGLL":

    def _read(self):
        while True:
            nmea_line = self.uart.readline()

            print("Read")
            asyncio.sleep(10)