from fixes_transmission.fixes_transmission import FixesTransmissionServer
from ublox_communication.ublox_communication import UbloxCommunication
import serial


def lines_from_serial():
    lines = set()
    with serial.Serial('/dev/ttyACM0', baudrate=9600, timeout=1) as port_in:
        for x in range(20):
            try:
                lines.add(port_in.readline())
            except (ValueError, IOError) as err:
                print(err)
    print(lines)

def main():
    ublox_comm = UbloxCommunication()

    while 1:
        #ublox_comm.check_fix_mode()
        #print("\nFix mode: " + str(ublox_comm.fix))
        #print(ublox_comm.get_position())
        ublox_comm.lines_from_serial()


if __name__ == '__main__':
    main()
