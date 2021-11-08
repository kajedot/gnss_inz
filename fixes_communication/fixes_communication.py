import socket


class FixesCommunication:

    def send_data(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind(('', 65432))
            server_socket.listen()
            conn, addr = server_socket.accept()
            with conn:
                print('Connected by', addr)
                while True:
                    try:
                        conn.send(b'eo')

                    except (ValueError, IOError) as err:
                        print(err)
                        break
