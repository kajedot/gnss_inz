import serial
from ublox_gps import UbloxGps


class NmeaParser:

    port = ''
    gps = ''

    def __init__(self):
        port = serial.Serial('/dev/serial0', baudrate=38400, timeout=1)
        gps = UbloxGps(port)

    def listen(self, port, gps):

        try:
            print("Listening for UBX Messages")
            while True:
                try:
                    print(gps.stream_nmea())
                except (ValueError, IOError) as err:
                    print(err)

        finally:
            port.close()
