import serial
from ublox_gps import UbloxGps


class NmeaParser:

    def __init__(self):
        self.port = serial.Serial('/dev/ttyACM0', baudrate=38400, timeout=1)

    def listen(self):

        port = serial.Serial('/dev/ttyACM0', baudrate=38400, timeout=1)
        gps = UbloxGps(port)

        response = ""

        try:
            #print(gps.stream_nmea())
            response = gps.stream_nmea()

        except (ValueError, IOError) as err:
            print(err)

        finally:
            port.close()

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
        gps = UbloxGps(port)

        position = (0, 0)

        try:
            geo = gps.geo_coords()
            position = (geo.lon, geo.lat)
        except (ValueError, IOError) as err:
            print(err)

        finally:
            port.close()

        return position

    def get_raw(self):
        line_bytes = None

        try:
            line_bytes = self.port.readline()
        except (ValueError, IOError) as err:
            print(err)

        return line_bytes

    def __del__(self):
        self.port.close()
