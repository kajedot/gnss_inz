from fixes_transmission.fixes_transmission import FixesTransmissionServer
from ublox_communication.ublox_communication import UbloxCommunication


def main():
    ublox_comm = UbloxCommunication()
    #fixes_comm = FixesTransmissionServer(ublox_comm)

    #fixes_comm.connections_listener()

    while 1:
        ublox_comm.check_fix_mode()
        #print("\nFix mode: " + str(ublox_comm.fix))
        #print(ublox_comm.get_position())

        #ublox_comm.write(data)

        print(ublox_comm.get_nmea_message("GNGGA"))


if __name__ == '__main__':
    main()
