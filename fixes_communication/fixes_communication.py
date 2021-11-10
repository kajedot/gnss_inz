import socket
from threading import Thread


class FixesCommunication(Thread):

    def __init__(self, socket, address):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(('', 65432))
        clientsocket, address = server_socket.accept()

        Thread.__init__(self)
        self.socket = socket
        self.addr = address
        self.start()

    def run(self):
        self.socket.send(b'eoo')
