import socket


class FixesCommunication:

    def __init__(self):
        # server's IP address
        # if the server is not on this machine,
        # put the private (network) IP address (e.g 192.168.1.2)
        SERVER_HOST = "192.168.1.103"
        SERVER_PORT = 5002  # server's port

        # initialize TCP socket
        self.tcp_socket = socket.socket()
        print(f"[*] Connecting to {SERVER_HOST}:{SERVER_PORT}...")
        # connect to the server
        self.tcp_socket.connect((SERVER_HOST, SERVER_PORT))
        print("[+] Connected.")

    def send_fix(self, to_send):
        self.tcp_socket.send(to_send)

    def __del__(self):
        self.tcp_socket.close()

