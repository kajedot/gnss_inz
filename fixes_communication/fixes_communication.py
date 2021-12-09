import socket


class FixesCommunication:

    def __init__(self, server_ip, server_port):

        server_ip = "192.168.1.103"
        server_port = 5002

        # initialization of the TCP socket
        self.tcp_socket = socket.socket()
        print(f"Connecting to rover @ {server_ip}:{server_port}...")
        # connect to the server
        self.tcp_socket.connect((server_ip, server_port))
        print("Connected successfully")

    def send_fix(self, to_send):
        self.tcp_socket.send(to_send)

    def __del__(self):
        self.tcp_socket.close()

