import serial
from ublox_gps import UbloxGps


class UbloxCommunication:

    def __init__(self):
        self.fix = 0

    def lines_from_serial(self):
        lines = set() # create set collection for recived serial lines
        with serial.Serial('/dev/ttyACM0', baudrate=38400, timeout=1) as port_in:  # open serial port
            for x in range(12):  # get 12 lines in one shot
                try:
                    lines.add(port_in.readline())
                except (ValueError, IOError) as err:
                    print(err)
        return lines

    def get_nmea_message(self, message_id: bytes):
        serial_lines = self.lines_from_serial()  # get lines from method above

        for line in serial_lines:
            splited = line.split(b',')  # split fields of the NMEA message by commas
            if splited[0] == (b'$' + message_id):  # do message has ID like in argument?
                return line

        return 0

    def get_fix_mode(self):
        serial_line = self.get_nmea_message(b'GNGGA')

        if serial_line != 0:
            splited = serial_line.split(b',')
            return splited[6].decode("utf-8")  # fix info is on the 6th position

        return 0

    def get_position(self):
        position = (0, '-', 0, '-')

        serial_line = self.get_nmea_message(b'GNGGA')

        if serial_line != 0:
            splited = serial_line.split(b',')

            latitude = float(splited[2])/100
            latitude = latitude + (latitude % 1)/0.6
            latitude_dir = splited[3].decode("utf-8")
            longitude = float(splited[4])/100
            longitude = longitude + (longitude % 1) / 0.6
            longitude_dir = splited[5].decode("utf-8")

            position = (latitude, latitude_dir, longitude, longitude_dir)

        return position

    def get_position_qwick(self):

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
