import socket


class FixesCommunication:

    def __init__(self, port):

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind(('', port))
            server_socket.listen()
            self.conn, addr = server_socket.accept()
            with self.conn:
                print('Connected by', addr)

                while 1:
                    try:
                        self.conn.send(b'eo')  # sending via lan socket

                    except (ValueError, IOError) as err:
                        print(err)

    def send_data(self, data):
        try:
            self.conn.send(data)  # sending via lan socket

        except (ValueError, IOError) as err:
            print(err)
