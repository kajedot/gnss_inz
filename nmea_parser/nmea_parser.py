import serial
from ublox_gps import UbloxGps


class NmeaParser:

    def __init__(self):
        self.port = serial.Serial('/dev/ttyACM0', baudrate=38400, timeout=1)
        self.gps = UbloxGps(self.port)

    def listen(self):

        try:
            print("Listening for UBX Messages")
            while True:
                try:
                    print(self.gps.stream_nmea())
                except (ValueError, IOError) as err:
                    print(err)

        finally:
            self.port.close()
