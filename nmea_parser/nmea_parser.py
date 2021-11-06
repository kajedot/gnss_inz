import serial


class NmeaParser:

    def listen(self):

        with serial.Serial('/dev/ttyACM0', baudrate=38400, timeout=1) as port:
            port.flushInput()
            try:
                line_bytes = port.readline()  # reciving via serial port
                print(line_bytes)

            except (ValueError, IOError) as err:
                print(err)

            finally:
                port.close()

        return line_bytes

    def peel_gngga_message(self):
        heard = self.listen()
        splited = [0]

        print(heard)

        if heard[0] == "$":
            splited = heard.split(",")

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

