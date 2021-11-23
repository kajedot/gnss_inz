from fixes_transmission.fixes_transmission import FixesTransmissionServer
from ublox_communication.ublox_communication import UbloxCommunication


def main():
    ublox_comm = UbloxCommunication()

    while 1:
        #ublox_comm.check_fix_mode()

        #print(ublox_comm.get_position())
        print()
        print(ublox_comm.get_nmea_message(b'GNGGA'))
        print("Fix mode: " + str(ublox_comm.get_fix_mode()))
        print(ublox_comm.get_position())


if __name__ == '__main__':
    main()
