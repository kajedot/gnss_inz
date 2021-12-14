import serial


class ModuleCommunication:

    def __init__(self, dev_path, bauds):
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

    def get_fix_mode(self):

        heard = self.get_raw()
        fix = 0
        splited = []

        if(heard):
            # assign each field of NEMA message to each field of list
            splited = heard.split(",")  # fields of NMEA messages are splitted by commas

            if splited[0] == "$GNGGA":
                fix = splited[6]  # fix info is on the 6th position of the GNGGA message

        return fix

    def __del__(self):
        self.port.close()
