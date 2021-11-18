from fixes_transmission.fixes_transmission import FixesTransmissionServer
from ublox_communication.ublox_communication import UbloxCommunication


def main():
    ublox_comm = UbloxCommunication()
    fixes_comm = FixesTransmissionServer(ublox_comm)

    fixes_comm.connections_listener()

    while 1:
        print("\nFix mode: " + str( ublox_comm.get_fix_mode() ))
        print(ublox_comm.get_position())

        #ublox_comm.write(data)


if __name__ == '__main__':
    main()
