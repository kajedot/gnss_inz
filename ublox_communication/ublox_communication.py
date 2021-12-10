import serial
from ublox_gps import UbloxGps


class UbloxCommunication:

    def __init__(self, device, bauds):
        self.fix = 0
        self.device = device
        self.bauds = bauds

    def lines_from_serial(self):
        lines = set()  # create set collection for recived serial lines
        with serial.Serial(self.device, baudrate=self.bauds, timeout=1) as port_in:  # open serial port
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

            # GNGGA position 2: ddmm.mm, 3: N/S, 4: ddmm.mm 5: E/W
            # (d - degree, m - minute, N/E/S/W - cardinal directions)

            if splited[2]:  # check if ublox is receiving position at all

                # conversion ddmm.mm to dd.mmmm:
                latitude = float(splited[2])/100

                # dd + 0.mmmm/0.6 for conversion minutes to degree fraction:
                latitude = round(latitude//1 + (latitude % 1)/0.6, 7)

                # conversion N/S to utf 8
                latitude_dir = splited[3].decode("utf-8")

                # analogically with longitude:
                longitude = float(splited[4])/100
                longitude = round(longitude//1 + (longitude % 1)/0.6, 7)
                longitude_dir = splited[5].decode("utf-8")

                position = (latitude, latitude_dir, longitude, longitude_dir)

        return position

    def write(self, data):
        port = serial.Serial(self.device, baudrate=self.bauds, timeout=1)

        port.write(data)

    def get_position_qwick(self):

        port = serial.Serial(self.device, baudrate=self.bauds, timeout=1)
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
