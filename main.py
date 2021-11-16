import time
from nmea_parser.nmea_parser import NmeaParser
from fixes_communication.fixes_communication import FixesCommunication


def main():
    parser = NmeaParser()
    communication = FixesCommunication()
    while 1:
        #print("Fix mode: " + str( parser.get_fix_mode() ))
        #print(parser.get_raw())

        communication.client_loop(parser.get_raw())


if __name__ == '__main__':
    main()
