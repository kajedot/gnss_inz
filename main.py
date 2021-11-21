from fixes_transmission.fixes_transmission import FixesTransmissionServer
from ublox_communication.ublox_communication import UbloxCommunication


def main():
    ublox_comm = UbloxCommunication()

    while 1:
        ublox_comm.check_fix_mode()
        #print("\nFix mode: " + str(ublox_comm.fix))
        #print(ublox_comm.get_position())

        print(ublox_comm.lines_from_serial())


if __name__ == '__main__':
    main()
