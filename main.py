
from ublox_communication.ublox_communication import UbloxCommunication
from fixes_transmission.fixes_transmission import FixesTransmissionServer


def main():

    #ublox_comm = UbloxCommunication()
    fixes_comm = FixesTransmissionServer()

    while 1:
        #print("Fix mode: " + str( parser.get_fix_mode() ))
        #print(parser.get_position())

        fixes_comm.server_loop()
        #ublox_comm.write(data)


if __name__ == '__main__':
    main()
