import serial
from ublox_gps import UbloxGps


class NmeaParser:

    def __init__(self):
        self.port = serial.Serial('/dev/ttyACM0', baudrate=38400, timeout=1)
        self.gps = UbloxGps(self.port)

    def listen(self):

        response = ""

        try:
            #print(self.gps.stream_nmea())
            response = self.gps.stream_nmea()

        except (ValueError, IOError) as err:
            print(err)

        finally:
            self.port.close()

        return response


    def get_fix_mode(self):

        heard = self.listen()
        fix = 0

        if(heard):
            splited = heard.split(",")

        if splited[0] == "$GNGGA":
            fix = splited[6]

        return fix



