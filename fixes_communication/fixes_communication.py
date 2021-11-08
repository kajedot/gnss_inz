import socket


class FixesCommunication:

    def send_data(self, data):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind(('', 65432))
            server_socket.listen()
            conn, addr = server_socket.accept()
            with conn:
                print('Connected by', addr)
                try:
                    conn.send(data)

                except (ValueError, IOError) as err:
                    print(err)