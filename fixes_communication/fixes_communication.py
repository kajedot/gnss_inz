import socket


class FixesCommunication:

    def send_via_socket(self, data, host, port):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind((host, port))
            server_socket.listen()
            conn, addr = server_socket.accept()
            with conn:
                print('Connected by', addr)
                while True:
                    try:
                        conn.send(data)  #sending via lan socket

                    except (ValueError, IOError) as err:
                        print(err)
                        break