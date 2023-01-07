import socket

from manageFile.manageFile import ManageFile
from settings.settings import Settings

# class to manage the tcp socker
class SocketTcp:
    
    # constructor to initialize the whole manageSocket object
    def __init__(self, name: str, host: str, port: int, clients: int, manageFile: ManageFile, settings: Settings):
        # save the name for the socket
        self.__name = name
        # initialize the host field
        self.__host = host
        # initialize the port field
        self.__port = port
        # initialize the maximum number of client
        self.__clients = clients
        # save the reference for the file
        self.__manageFile = manageFile
        # save the reference for the settings
        self.__settings = settings
    
    # function used to create configure and start the socket
    def createConfigureStartSocket(self):
        # create and configure the socket
        self.__createAndConfigureSocketTcp()
        # wait a connection request
        self.__waitNewRequests()
        # start to listen in the socket channel
        self.__listenMessageIntoSocket()
        # close the socket
        self.__closeTcpSocket()
    
    # function used to update the name field
    def setName(self, name):
        # update name field
        self.__name = name
    
    # function used to update host field
    def setHost(self, host: str):
        # update host field
        self.__host = host
    
    # function used to update port field
    def setPort(self, port: int):
        # update port field
        self.__port = port
    
    # function used to update clients number
    def setClients(self, clients: int):
        # update clients field
        self.__clients = clients
    
    # function used to update the manage file field
    def setManageFile(self, manageFile: ManageFile):
        # update manage file field
        self.__manageFile = manageFile
    
    # function used to update the settings field
    def setSettings(self, settings: Settings):
        # update settings field
        self.__settings = settings
    
    # function used to get the name field
    def getName(self):
        # get the name field
        return self.__name
    
    # function used to get the host field
    def getHost(self):
        # get the host field
        return self.__host
    
    # function used to get the port field
    def getPort(self):
        # get the port field
        return self.__port
    
    # function used to get the clients field
    def getClients(self):
        # get the clients field
        return self.__clients
    
    # function used to get the manage file
    def getManageFile(self):
        # return the manage file field
        return self.__manageFile
    
    # function used to get settings field
    def getSettings(self):
        # return the settings field
        return self.__settings
    
    # function used to create the tcp manageSocket
    def __createAndConfigureSocketTcp(self):
        # create the manageSocket object
        self.__server_socket = socket.socket()
        # bing parameter to the manageSocket object
        self.__server_socket.bind((self.__host, self.__port))
        # one client maximum for the connection
        self.__server_socket.listen(self.__clients)
    
    # function used to listen new requests
    def __waitNewRequests(self):
        # wait new incoming request
        self.__conn, self.__address = self.__server_socket.accept()
        print(self.__name + " - Connection from: " + str(self.__address))
    
    # function to receive data from the manageSocket
    def __listenMessageIntoSocket(self):
        # while all messages are not received
        while True:
            # receive data stream, it won't accept data packet greater than 10240 bytes
            self.__receivedMessageBytes = self.__conn.recv(self.__settings.getDimensionSocketData())
            # if there aren't received data
            if not self.__receivedMessageBytes:
                # exit from listening mode
                break
            # transform the bytes array into a string
            self.__receivedMessageString = self.__receivedMessageBytes.decode()
            # delete from the incoming message the final new line
            self.__receivedMessageString = self.__receivedMessageString.rstrip()
            # if the received string is the terminal string
            if self.__receivedMessageString == "exit":
                # exit from listening mode
                break
            # if the received string is not an empty string
            if self.__receivedMessageString != "":
                # write the incoming message into the file
                self.__manageFile.writeIntoFile(self.__receivedMessageString)
                # analyze the input data
                self._analyzeInputData()
        print("exit from function")
    
    # function used to analyze the received data
    def _analyzeInputData(self):
        pass
    
    # function used to close the tcp manageSocket
    def __closeTcpSocket(self):
        # close the file
        self.__manageFile.closeFile()
        # close the connection
        self.__conn.close()
        # close the manageSocket
        self.__server_socket.close()
