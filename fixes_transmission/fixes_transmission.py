import socket


class FixesTransmissionClient:

    def receive_data(self, address, port):

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as web_socket:
            web_socket.connect((address, port))
            while True:
                try:
                    data = web_socket.recv(1024)
                    print(data)
                except (ValueError, IOError) as err:
                    print(err)
