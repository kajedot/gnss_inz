import socket


class FixesCommunication:

    def __init__(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind(('', 65432))
            server_socket.listen()
            self.conn, self.addr = server_socket.accept()

    def send_data(self, data):
        with self.conn:
            print('Connected by', self.addr)
            try:
                self.conn.send(data)
            except (ValueError, IOError) as err:
                print(err)