import socket
from threading import Thread


class FixesTransmissionServer:

    def __init__(self):
        # server'tcp_socket IP address
        SERVER_HOST = "0.0.0.0"
        SERVER_PORT = 5002  # port we want to use
        self.separator_token = "<SEP>"  # we will use this to separate the client name & message

        # initialize list/set of all connected client's sockets
        self.client_sockets = set()
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
                msg = cs.recv(1024).decode()
            except Exception as e:
                # client no longer connected
                # remove it from the set
                print(f"[!] Error: {e}")
                self.client_sockets.remove(cs)
            # iterate over all connected sockets
            for client_socket in self.client_sockets:
                print(msg.encode())

    def server_loop(self):
        # we keep listening for new connections all the time
        client_socket, client_address = self.tcp_socket.accept()
        print(f"[+] {client_address} connected.")
        # add the new connected client to connected sockets
        self.client_sockets.add(client_socket)
        # start a new thread that listens for each client's messages
        t = Thread(target=self.listen_for_client, args=(client_socket,))
        # make the thread daemon so it ends whenever the main thread ends
        t.daemon = True
        # start the thread
        t.start()

    def __del__(self):
        # close client sockets
        for cs in self.client_sockets:
            cs.close()
        # close server socket
        self.tcp_socket.close()
