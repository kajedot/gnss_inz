
from nmea_parser.nmea_parser import NmeaParser


def main():

    parser = NmeaParser()

    while 1:
        print("Fix mode: " + parser.get_fix_mode())
        print(parser.get_position())


if __name__ == '__main__':
    main()
