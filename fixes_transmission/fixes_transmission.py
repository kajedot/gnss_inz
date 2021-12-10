import socket
from threading import Thread


class FixesTransmissionServer:

    def __init__(self, ublox_comm, server_ip, server_port):
        self.ublox_comm = ublox_comm
        self.client_sockets = set()

        # create a TCP socket
        self.tcp_socket = socket.socket()
        # set socket options which allow to connect again after loosing the connection
        self.tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # bind the socket to the address and port
        self.tcp_socket.bind((server_ip, server_port))
        # start listening for the upcoming connections (with queue of 1 connection)
        self.tcp_socket.listen(1)
        print(f"Listening as {server_ip}:{server_port}")
        self.accept_clients()

    def accept_clients(self):
        client_socket, client_address = self.tcp_socket.accept()
        print(f"{client_address} connected")
        # add recently connected client to the collection of clients
        self.client_sockets.add(client_socket)
        # start constantly listening for the new messages on the separate thread
        thread = Thread(target=self.messages_listener, args=(client_socket,))
        # daemonize thread so it will end when the main thread will end
        thread.daemon = True
        thread.start()

    def messages_listener(self, client_socket):
        while True:
            try:
                # keep listening for a message from the client's socket
                msg = client_socket.recv(1024)
                print(msg)
                # and send it to the rover's serial port
                self.ublox_comm.write(msg)
            except Exception as e:
                print(f"Error: {e}")
                self.client_sockets.remove(client_socket)

    def __del__(self):
        for cs in self.client_sockets:
            cs.close()
        # close server socket
        self.tcp_socket.close()
