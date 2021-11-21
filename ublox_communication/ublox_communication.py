import serial
from ublox_gps import UbloxGps


class UbloxCommunication:

    def __init__(self):
        self.fix = 0

    def lines_from_serial(self):
        lines = set()
        with serial.Serial('/dev/ttyACM0', baudrate=38400, timeout=1) as port_in:
            for x in range(12):
                try:
                    lines.add(port_in.readline())
                except (ValueError, IOError) as err:
                    print(err)
        print(lines)
        return lines

    def get_nmea_message(self, message_id: bytes):
        serial_lines = self.lines_from_serial()

        for line in serial_lines:
            splited = line.split(b',')
            print(splited[0])
            if splited[0] == (b'$' + message_id):
                return line

        return 0

    def check_fix_mode(self):

        serial_lines = self.lines_from_serial()

        print(serial_lines)
        print(type(serial_lines))

        if serial_lines:
            splited = serial_lines.split(",")

            if splited[0] == "$GNGGA":
                self.fix = splited[6]  # fix info is on the 6th position
                print(serial_lines)

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
