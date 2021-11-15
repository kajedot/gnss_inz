
from ublox_communication.ublox_communication import UbloxCommunication
from fixes_transmission.fixes_transmission import FixesTransmissionClient


def main():

    #ublox_comm = UbloxCommunication()
    fixes_comm = FixesTransmissionClient()

    while 1:
        #print("Fix mode: " + str( parser.get_fix_mode() ))
        #print(parser.get_position())

        data = fixes_comm.receive_data("192.168.1.76", 65432)
        #print(data)
        #ublox_comm.write(data)


if __name__ == '__main__':
    main()
