import serial
from ublox_gps import UbloxGps


class NmeaParser:

    def __init__(self, dev_path="/dev/ttyACM0", bauds=38400):
        # initialize communication with u-blox ZED-F9P module
        self.port = serial.Serial(dev_path, baudrate=bauds, timeout=1)

    def get_raw(self):
        line_bytes = None
        # get data from module line by line
        try:
            line_bytes = self.port.readline()
        except (ValueError, IOError) as err:
            print(err)

        return line_bytes

    def __del__(self):
        self.port.close()

    """not used anymore:"""

    def get_fix_mode(self):

        heard = self.listen()
        fix = 0
        splited = []

        if(heard):
            # assign each field of NEMA message to each field of list
            splited = heard.split(",")  # fields of NMEA messages are splitted by commas

            if splited[0] == "$GNGGA":
                fix = splited[6]  # fix info is on the 6th position of the GNGGA message

        return fix

    """Methods using UbloxGps Qwiic library - left for test purposes:"""
    
    def listen(self):

        port = serial.Serial('/dev/ttyACM1', baudrate=38400, timeout=1)
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

    def get_position(self):

        port = serial.Serial('/dev/ttyACM1', baudrate=38400, timeout=1)
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


