import socket
from threading import Thread


class FixesCommunication(Thread):

    def __init__(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(('0.0.0.0', 65432))
        client_socket, address = server_socket.accept()

        Thread.__init__(self)
        self.socket = client_socket
        self.addr = address
        self.start()

    def run(self):
        self.socket.send(b'eoo')
