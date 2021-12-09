import argparse

from nmea_parser.nmea_parser import NmeaParser
from fixes_communication.fixes_communication import FixesCommunication


def main():
    args = get_arguments()  # firstly manage command-line arguments

    nmea_parser = NmeaParser(args['device'], args['baudrate'])
    communication = FixesCommunication(args['server'], args['port'])

    while 1:

        raw = nmea_parser.get_raw()
        if raw:
            print(raw)
            communication.send_fix(raw)


def get_arguments():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("-d", "--device", required=False, default='/dev/ttyACM0',
                            help="path to the u-blox base device (default: '/dev/ttyACM0')")
    arg_parser.add_argument("-b", "--baudrate", required=False, default=38400,
                            help="baud rate of transmission with the u-blox base device (default: 38400)")
    arg_parser.add_argument("-s", "--server", required=True,
                            help="server's (rover's) ip address")
    arg_parser.add_argument("-p", "--port", required=False, default=5002,
                            help="server's port (default: 5002)")
    return vars(arg_parser.parse_args())


if __name__ == '__main__':
    main()
