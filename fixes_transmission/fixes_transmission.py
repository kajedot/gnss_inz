import socket
from threading import Thread


class FixesTransmissionServer:

    def __init__(self):
        # server'tcp_socket IP address
        SERVER_HOST = "0.0.0.0"
        SERVER_PORT = 5002  # port we want to use
        self.separator_token = "<SEP>"  # we will use this to separate the client name & message

        # create a TCP socket
        self.tcp_socket = socket.socket()
        # make the port as reusable port
        self.tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # bind the socket to the address we specified
        self.tcp_socket.bind((SERVER_HOST, SERVER_PORT))
        # listen for upcoming connections
        self.tcp_socket.listen(5)
        print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")

    def listen_for_client(self, cs):
        """
        This function keep listening for a message from `cs` socket
        Whenever a message is received, broadcast it to all other connected clients
        """
        while True:
            try:
                # keep listening for a message from `cs` socket
                msg = cs.recv(1024)
                print(msg)
            except Exception as e:
                print(f"[!] Error: {e}")

    def server_loop(self):
        # we keep listening for new connections all the time
        client_socket, client_address = self.tcp_socket.accept()
        print(f"[+] {client_address} connected.")

        # start a new thread that listens for each client's messages
        t = Thread(target=self.listen_for_client, args=(client_socket,))
        # make the thread daemon so it ends whenever the main thread ends
        t.daemon = True
        # start the thread
        t.start()

    def __del__(self):
        # close server socket
        self.tcp_socket.close()
