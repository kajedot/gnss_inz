import serial
from ublox_gps import UbloxGps


class NmeaParser:

    def listen(self):

        self.port = serial.Serial('/dev/ttyACM0', baudrate=38400, timeout=1)
        self.gps = UbloxGps(self.port)

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
        splited = []

        if(heard):
            splited = heard.split(",")

            if splited[0] == "$GNGGA":
                fix = splited[6]  # fix info is on the 6th position

        return fix

    def get_position(self):

        port = serial.Serial('/dev/ttyACM0', baudrate=38400, timeout=1)
        gps = UbloxGps(self.port)

        position = (0, 0)

        try:
            geo = gps.geo_coords()
            position = (geo.lon, geo.lat)
        except (ValueError, IOError) as err:
            print(err)

        return position

