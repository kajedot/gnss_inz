import socket


class FixesCommunicationClient:

    def __init__(self, address, port):

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as self.client_socket:
            self.client_socket.connect((address, port))
            self.conn, addr = self.client_socket.accept()

    def send_data(self, data):
        try:
            self.conn.send(data)  # sending via lan socket

        except (ValueError, IOError) as err:
            print(err)

    def receive_data(self):
        try:
            data = self.client_socket.recv(1024)
            return data
        except (ValueError, IOError) as err:
            print(err)
