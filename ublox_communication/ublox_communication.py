import serial
from ublox_gps import UbloxGps


class UbloxCommunication:

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

        return fix + " (" + heard + ")"

    def get_position(self):

        port = serial.Serial('/dev/ttyACM0', baudrate=38400, timeout=1)
        gps = UbloxGps(port)

        position = (0, 0)

        try:
            geo = gps.geo_coords()
            position = (geo.lat, geo.lon)
        except (ValueError, IOError) as err:
            print(err)

        finally:
            port.close()

        return position

    def write(self, data):
        port = serial.Serial('/dev/ttyACM0', baudrate=38400, timeout=1)

        port.write(data)
