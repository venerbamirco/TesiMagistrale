import socket

from dataStructure.file import File
from settings.settings import Settings

# class to manage the general tcp socket
class GeneralSocket :
    
    # constructor to initialize the whole manageSocket object
    def __init__ ( self , name: str , host: str , port: int , clients: int , manageFile: File , settings: Settings ) :
        #
        # save the name for the tcpSocket
        self.name = name
        #
        # initialize the host field
        self.host = host
        #
        # initialize the port field
        self.port = port
        #
        # initialize the maximum number of client
        self.clients = clients
        #
        # save the reference for the file
        self.manageFile = manageFile
        #
        # save the reference for the settings
        self.settings = settings
        #
        # save the server socket reference
        self.serversocket = None
        #
        # save the reference of the ip address of the client
        self.address = None
        #
        # save the reference for the connection
        self.conn = None
    
    # function used to create configure and start the tcpSocket
    def createConfigureStartSocket ( self ) :
        #
        # create and configure the tcpSocket
        self.createAndConfigureSocketTcp ( )
        #
        # wait a connection request
        self.waitNewRequests ( )
        #
        # start to listen in the tcpSocket channel
        self.listenMessageIntoSocket ( )
        #
        # close the tcpSocket
        self.closeAll ( )
    
    # function used to create the tcp manageSocket
    def createAndConfigureSocketTcp ( self ) :
        #
        # create the manageSocket object
        self.serversocket = socket.socket ( )
        #
        # bing parameter to the manageSocket object
        self.serversocket.bind ( (self.host , self.port) )
        #
        # one client maximum for the connection
        self.serversocket.listen ( self.clients )
    
    # function used to listen new requests
    def waitNewRequests ( self ) :
        #
        # wait new incoming request
        self.conn , self.address = self.serversocket.accept ( )
        #
        # debug row for a connection
        print ( self.name + " - Connection from: " + str ( self.address ) )
    
    # function to receive data from the manageSocket
    def listenMessageIntoSocket ( self ) :
        #
        # while all messages are not received
        while True :
            #
            # receive data stream, it won't accept data packet greater than 10240 bytes
            receivedMessageBytes = self.conn.recv ( self.settings.dimensionSocketData )
            #
            # if there aren't received data
            if not receivedMessageBytes :
                #
                # exit from listening mode
                break
            #
            # transform the bytes array into a string
            receivedMessageString = receivedMessageBytes.decode ( )
            #
            # delete from the incoming message the final new line
            receivedMessageString = receivedMessageString.rstrip ( )
            #
            # if the received string is not an empty string
            if receivedMessageString != "" :
                #
                # analyze the input data
                self.analyzeInputData ( receivedMessageString )
        #
        # debug row that actual tcpSocket is terminated
        print ( self.name + " - Terminated" )
    
    # function used to analyze the received data
    def analyzeInputData ( self , receivedMessageString: str ) :
        pass
    
    # function used to restrict the received data
    def restrictInputMessages ( self ) :
        pass
    
    # function used to close the tcp tcpSocket and the file
    def closeAll ( self ) :
        #
        # close the file
        self.manageFile.closeFile ( )
        # close the connection
        self.conn.close ( )
        # close the management of tcpSocket
        self.serversocket.close ( )
