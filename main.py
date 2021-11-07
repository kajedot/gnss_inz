
from nmea_parser.nmea_parser import NmeaParser
from fixes_communication.fixes_communication import FixesCommunicationClient


def main():

    #parser = NmeaParser()
    fixes_comm = FixesCommunicationClient("192.168.1.76", 65432)

    while 1:
        #print("Fix mode: " + str( parser.get_fix_mode() ))
        #print(parser.get_position())

        data = fixes_comm.receive_data()
        print(data)


if __name__ == '__main__':
    main()
