import argparse

from module_comm.module_comm import ModuleCommunication
from fixes_comm.fixes_comm import FixesCommunication


def main():
    args = get_arguments()  # firstly manage command-line arguments

    module_comm = ModuleCommunication(args['device'], args['baudrate'])
    communication = FixesCommunication(args['server'], args['port'])

    while 1:
        raw = module_comm.get_raw()  # constantly get lines with fixes from serial port
        if raw:
            if args['verbose']:
                print(raw)

            communication.send_fix(raw)


def get_arguments():
    arg_parser = argparse.ArgumentParser()
    #  definitions of command-line arguments
    arg_parser.add_argument("-d", "--device", required=False, default='/dev/ttyACM0',
                            help="path to the u-blox base device (default: '/dev/ttyACM0')")
    arg_parser.add_argument("-b", "--baudrate", required=False, default=38400,
                            help="baud rate of transmission with the u-blox base device (default: 38400)")
    arg_parser.add_argument("-s", "--server", required=True,
                            help="server's (rover's) ip address")
    arg_parser.add_argument("-p", "--port", required=False, default=5002,
                            help="server's port (default: 5002)")
    arg_parser.add_argument("-v", "--verbose", required=False, action='store_true',
                            help="print raw fixes data for the diagnostic purposes")
    return vars(arg_parser.parse_args())


if __name__ == '__main__':
    main()
