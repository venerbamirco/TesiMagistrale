import socket

from manageFile.manageFile import ManageFile
from settings.settings import Settings

# class to manage the tcp socker
class SocketTcp:
    
    # constructor to initialize the whole manageSocket object
    def _init_(self, name: str, host: str, port: int, clients: int, manageFile: ManageFile, settings: Settings):
        #
        # save the name for the socket
        self._name = name
        # initialize the host field
        self._host = host
        # initialize the port field
        self._port = port
        # initialize the maximum number of client
        self._clients = clients
        # save the reference for the file
        self._manageFile = manageFile
        # save the reference for the settings
        self._settings = settings
    
    # function used to create configure and start the socket
    def createConfigureStartSocket(self):
        #
        # create and configure the socket
        self._createAndConfigureSocketTcp()
        #
        # wait a connection request
        self._waitNewRequests()
        #
        # start to listen in the socket channel
        self._listenMessageIntoSocket()
        #
        # close the socket
        self._closeAll()
    
    # function used to create the tcp manageSocket
    def _createAndConfigureSocketTcp(self):
        #
        # create the manageSocket object
        self._server_socket = socket.socket()
        #
        # bing parameter to the manageSocket object
        self._server_socket.bind((self._host, self._port))
        #
        # one client maximum for the connection
        self._server_socket.listen(self._clients)
    
    # function used to listen new requests
    def _waitNewRequests(self):
        #
        # wait new incoming request
        self._conn, self._address = self._server_socket.accept()
        #
        # debug row for a connection
        print(self._name + " - Connection from: " + str(self._address))
    
    # function to receive data from the manageSocket
    def _listenMessageIntoSocket(self):
        #
        # while all messages are not received
        while True:
            #
            # receive data stream, it won't accept data packet greater than 10240 bytes
            self._receivedMessageBytes = self._conn.recv(self._settings.getDimensionSocketData())
            #
            # if there aren't received data
            if not self._receivedMessageBytes:
                #
                # exit from listening mode
                break
            #
            # transform the bytes array into a string
            self._receivedMessageString = self._receivedMessageBytes.decode()
            #
            # delete from the incoming message the final new line
            self._receivedMessageString = self._receivedMessageString.rstrip()
            #
            # if the received string is not an empty string
            if self._receivedMessageString != "":
                #
                # analyze the input data
                self._analyzeInputData()
        #
        # debug row that actual socket is terminated
        print(self._name + " - Terminated")
    
    # function used to analyze the received data
    def _analyzeInputData(self):
        pass
    
    # function used to restrict the received data
    def _restrictInputMessages(self):
        pass
    
    # function used to close the tcp socket and the file
    def _closeAll(self):
        #
        # close the file
        self._manageFile.closeFile()
        # close the connection
        self._conn.close()
        # close the management of socket
        self._server_socket.close()
