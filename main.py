import argparse

from fixes_transmission.fixes_transmission import FixesTransmissionServer
from ublox_communication.ublox_communication import UbloxCommunication


def main():
    args = get_arguments()  # firstly manage command−line arguments

    ublox_comm = UbloxCommunication(args['device'], args['baudrate'])

    if not args['nofixes']:
        fixes_trans = FixesTransmissionServer(ublox_comm, args['server'], args['port'], args['verbose'])

    while True:
        if args['verbose']:
            print(ublox_comm.get_nmea_message(b'GNGGA'))

        if args['csv']:
            latitude, latitude_dir, longitude, longitude_dir = ublox_comm.get_position()
            print(f"{ublox_comm.get_fix_mode()},{latitude},{latitude_dir},{longitude},{longitude_dir},{ublox_comm.get_nmea_message(b'GNGGA')}")
        else:
            print("Fix mode: " + str(ublox_comm.get_fix_mode()))
            print(ublox_comm.get_position())


def get_arguments():
    arg_parser = argparse.ArgumentParser()
    #  definitions of command-line arguments
    arg_parser.add_argument("-d", "--device", required=False, default='/dev/ttyACM0', help="path to the u-blox rover device (default: '/dev/ttyACM0')")
    arg_parser.add_argument("-b", "--baudrate", required=False, default=38400, help="baud rate of transmission with the u-blox rover device (default: 38400)")
    arg_parser.add_argument("-s", "--server", required=False, default='0.0.0.0', help="ip address on which the server should run (default: 0.0.0.0)")
    arg_parser.add_argument("-p", "--port", required=False, default=5002, help="server's port (default: 5002)")
    arg_parser.add_argument("-n", "--nofixes", required=False, action='store_true', help="turn off fixes handling and WebSocket server") # store_true for arg. without value
    arg_parser.add_argument("-c", "--csv", required=False, action='store_true', help="print data in csv format: fix, latitude, latitude_dir, longitude, longitude_dir, GNGGA message")
    arg_parser.add_argument("-v", "--verbose", required=False, action='store_true', help="print received raw fixes data for the diagnostic purposes")
    return vars(arg_parser.parse_args())


if __name__ == '__main__':
    main()
