import serial


class NmeaParser:

    def listen(self):

        port = serial.Serial('/dev/ttyACM0', baudrate=38400, timeout=1)
        gps = UbloxGps(port)

        response = ""

        try:
            print(gps.stream_nmea())
            response = gps.stream_nmea()

        except (ValueError, IOError) as err:
            print(err)

        finally:
            port.close()

        return response

    def peel_gngga_message(self):
        heard = self.listen()
        splited = []

        if (heard):
            splited = heard.split(",")

            if splited[0] == "$GNGGA":
                return splited

    def get_fix_mode(self):

        gngga = self.peel_gngga_message()
        fix = 0

        if gngga[0] == "$GNGGA":
            fix = gngga[6]  # fix info is on the 6th position

        return fix

    def get_position(self):

        position = (0, '-', 0, '-')

        gngga = self.peel_gngga_message()

        if gngga[0] == "$GNGGA":
            position = (gngga[2], gngga[3], gngga[4], gngga[5])

        return position

