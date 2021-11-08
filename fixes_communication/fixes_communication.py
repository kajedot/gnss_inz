import socket


class FixesCommunication:

    def send_data(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind(('', 65432))
            server_socket.listen()
            self.conn, self.addr = server_socket.accept()

            with self.conn:
                print('Connected by', self.addr)
                try:
                    self.conn.send(b'eoo')
                except (ValueError, IOError) as err:
                    print(err)