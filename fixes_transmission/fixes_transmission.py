import socket
from threading import Thread


class FixesTransmissionServer:

    def __init__(self, ublox_comm):
        self.ublox_comm = ublox_comm
        self.client_sockets = set()
        # server'tcp_socket IP address
        SERVER_HOST = "0.0.0.0"
        SERVER_PORT = 5002  # port we want to use

        # create a TCP socket
        self.tcp_socket = socket.socket()
        # make the port as reusable port
        self.tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # bind the socket to the address we specified
        self.tcp_socket.bind((SERVER_HOST, SERVER_PORT))
        # listen for upcoming connections
        self.tcp_socket.listen(1)
        print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")

    def reciver_loop(self, cs):
        while True:
            try:
                # keep listening for a message from `cs` socket
                msg = cs.recv(1024)
                assert msg
                print(msg)
                self.ublox_comm.write(msg)
            except Exception as e:
                print(f"[!] Error: {e}")
                self.client_sockets.remove(cs)
    """ while True: """
    def connections_listener(self):
        # we keep listening for new connections all the time
        client_socket, client_address = self.tcp_socket.accept()
        print(f"[+] {client_address} connected.")
        self.client_sockets.add(client_socket)
        # start a new thread that listens for each client's messages
        t = Thread(target=self.reciver_loop, args=(client_socket,))
        # make the thread daemon so it ends whenever the main thread ends
        t.daemon = True
        # start the thread
        t.start()

    def __del__(self):
        for cs in self.client_sockets:
            cs.close()
        # close server socket
        self.tcp_socket.close()
