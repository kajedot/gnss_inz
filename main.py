
from nmea_parser.nmea_parser import NmeaParser
from fixes_communication.fixes_communication import FixesCommunication


def main():

    #parser = NmeaParser()
    fixes_comm = FixesCommunication()

    #while 1:
        #print("Fix mode: " + str( parser.get_fix_mode() ))
        #print(parser.get_raw())

    fixes_comm.send_data(b'eoo')


if __name__ == '__main__':
    main()
