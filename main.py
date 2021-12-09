from nmea_parser.nmea_parser import NmeaParser
from fixes_communication.fixes_communication import FixesCommunication


def main():
    parser = NmeaParser()
    communication = FixesCommunication()
    while 1:

        raw = parser.get_raw()
        if raw:
            print(raw)
            communication.send_fix(raw)


if __name__ == '__main__':
    main()
