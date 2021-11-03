
from nmea_parser.nmea_parser import NmeaParser


def main():

    parser = NmeaParser()

    while 1:
        print(parser.get_fix_mode())


if __name__ == '__main__':
    main()
