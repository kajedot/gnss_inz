import time
from nmea_parser.nmea_parser import NmeaParser
from fixes_communication.fixes_communication import FixesCommunication


def main():
    parser = NmeaParser()
    while 1:
        #print("Fix mode: " + str( parser.get_fix_mode() ))
        #print(parser.get_raw())

        FixesCommunication.send_data(parser.get_raw())

        time.sleep(3)


if __name__ == '__main__':
    main()
