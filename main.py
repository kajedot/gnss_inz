import time
from nmea_parser.nmea_parser import NmeaParser
from fixes_communication.fixes_communication import FixesCommunication


def main():
    parser = NmeaParser()
    communication = FixesCommunication()
    while 1:
        #print("Fix mode: " + str( parser.get_fix_mode() ))
        #print(parser.get_raw())
        raw = parser.get_raw()
        print(raw)
        communication.client_loop(raw)


if __name__ == '__main__':
    main()
