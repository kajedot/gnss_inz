import socket
from threading import Thread
from datetime import datetime


class FixesCommunication:

    def __init__(self):
        # server's IP address
        # if the server is not on this machine,
        # put the private (network) IP address (e.g 192.168.1.2)
        SERVER_HOST = "192.168.1.103"
        SERVER_PORT = 5002  # server's port
        self.separator_token = "<SEP>"  # we will use this to separate the client name & message

        # initialize TCP socket
        self.tcp_socket = socket.socket()
        print(f"[*] Connecting to {SERVER_HOST}:{SERVER_PORT}...")
        # connect to the server
        self.tcp_socket.connect((SERVER_HOST, SERVER_PORT))
        print("[+] Connected.")
        self.name = "kdt"

        self.start_thread()

    def listen_for_messages(self):
        while True:
            message = self.tcp_socket.recv(1024).decode()
            print("\n" + message)

    def start_thread(self):
        # make a thread that listens for messages to this client & print them
        self.thread = Thread(target=self.listen_for_messages)
        # make the thread daemon so it ends whenever the main thread ends
        self.thread.daemon = True
        # start the thread
        self.thread.start()

    def client_loop(self):
        # input message we want to send to the server
        to_send = input()
        # a way to exit the program
        if to_send.lower() == 'q':
            return
        # add the datetime, name & the color of the sender
        date_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        to_send = f"[{date_now}] {self.name}{self.separator_token}{to_send}"
        # finally, send the message
        self.tcp_socket.send(to_send.encode())

