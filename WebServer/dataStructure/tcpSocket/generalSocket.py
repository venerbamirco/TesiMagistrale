import socket

from algorithm.manager.manager import Manager
from dataStructure.other.file import File
from settings.settings import Settings

# class to manage the general tcp socket
class GeneralSocket :
    
    # constructor to initialize the whole manageSocket object
    def __init__ ( self , name: str , host: str , port: int , clients: int , manageFile: File , settings: Settings , managerAlgorithm: Manager ) :
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
        # save the reference for the other
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
        #
        # save the reference for the manager algorithm
        self.managerAlgorithm = managerAlgorithm
        #
        # variable to manage the last part of the previous message
        self.finalPartLastMessage = ""
    
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
        # set timeout for connection
        self.conn.settimeout ( self.settings.timeout )
        #
        # debug row for a connection
        print ( self.name + " - Connection from: " + str ( self.address ) )
    
    # function to receive data from the manageSocket
    def listenMessageIntoSocket ( self ) :
        #
        # while all messages are not received
        while True :
            #
            # manage the exception in conn.recv
            try :
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
            # in case of exception
            except socket.timeout :
                #
                # if the actual socket is android
                if self.name == "android" :
                    #
                    # do nothing because the device is stationary
                    pass
                #
                # if the actual socket is ptracer
                else :
                    #
                    # if the android socket is closed
                    if self.managerAlgorithm.flagAndroidSocket :
                        #
                        # exit from listen mode
                        break
                    #
                    # if android is not terminated
                    else :
                        #
                        # do nothing
                        pass
        #
        # debug row that actual tcpSocket is terminated
        print ( self.name + " - Terminated" )
        #
        # if the actual socket is android
        if self.name == "android" :
            #
            # set the android socket closed
            self.managerAlgorithm.setAndroidSocketTerminated ( )
        #
        # if the actual socket is ptracer
        else :
            #
            # set the ptracer socket closed
            self.managerAlgorithm.setPtracerSocketTerminated ( )
    
    # function used to analyze the received data
    def analyzeInputData ( self , receivedMessageString: str ) :
        #
        # only on ptracer socket
        if self.name == "ptracer" :
            #
            # get the list of single row of ptracer
            actualMessages = receivedMessageString.split ( "\n" )
            #
            # for each single row of the received message from the client
            for i in range ( 0 , len ( actualMessages ) ) :
                #
                # if first element
                if i == 0 :
                    #
                    # if it is a valid string for ptracer
                    if self.checkStringForPtracer ( actualMessages [ i ] ) :
                        #
                        # if also the previous final part is a valid string for ptracer
                        if self.checkStringForPtracer ( self.finalPartLastMessage ) :
                            #
                            # print actual message
                            self.printActualMessage ( self.finalPartLastMessage )
                            #
                            # print actual message
                            self.printActualMessage ( actualMessages [ i ] )
                        #
                        # else if the previous final part is not valid for ptracer
                        else :
                            #
                            # print actual message
                            self.printActualMessage ( self.finalPartLastMessage + actualMessages [ i ] )
                        #
                        # empty the final part of last message
                        self.finalPartLastMessage = ""
                    #
                    # else if it is not a valid string
                    else :
                        #
                        # print actual message
                        self.printActualMessage ( self.finalPartLastMessage + actualMessages [ i ] )
                        #
                        # empty the final part of last message
                        self.finalPartLastMessage = ""
                #
                # if it is the last message
                elif i == len ( actualMessages ) - 1 :
                    #
                    # save in the final part of last message
                    self.finalPartLastMessage = actualMessages [ i ]
                #
                # other elements
                else :
                    #
                    # if it is a valid string for ptracer
                    if self.checkStringForPtracer ( actualMessages [ i ] ) :
                        #
                        # print actual message
                        self.printActualMessage ( actualMessages [ i ] )
                        #
                        # empty the final part of last message
                        self.finalPartLastMessage = ""
        #
        # only on android socket
        else :
            #
            # get the list of single row of ptracer
            actualMessages = receivedMessageString.split ( "\n" )
            #
            # for each single row of the received message from the client
            for i in range ( 0 , len ( actualMessages ) ) :
                #
                # if first element
                if i == 0 :
                    #
                    # if it is a valid string
                    if self.checkStringForAndroid ( actualMessages [ i ] ) :
                        #
                        # if also the previous final part is a valid message for android
                        if self.checkStringForAndroid ( self.finalPartLastMessage ) :
                            #
                            # print actual message
                            self.printActualMessage ( self.finalPartLastMessage )
                            #
                            # print actual message
                            self.printActualMessage ( actualMessages [ i ] )
                        #
                        # else if the previous final part is not valid for android
                        else :
                            #
                            # print actual message
                            self.printActualMessage ( self.finalPartLastMessage + actualMessages [ i ] )
                        #
                        # empty the final part of last message
                        self.finalPartLastMessage = ""
                    #
                    # else if it is not a valid string
                    else :
                        #
                        # print actual message
                        self.printActualMessage ( self.finalPartLastMessage + actualMessages [ i ] )
                        #
                        # empty the final part of last message
                        self.finalPartLastMessage = ""
                #
                # if it is the last message
                elif i == len ( actualMessages ) - 1 :
                    #
                    # save in the final part of last message
                    self.finalPartLastMessage = actualMessages [ i ]
                #
                # other elements
                else :
                    #
                    # if it is a valid string for android
                    if self.checkStringForAndroid ( actualMessages [ i ] ) :
                        #
                        # print actual message
                        self.printActualMessage ( actualMessages [ i ] )
                        #
                        # empty the final part of last message
                        self.finalPartLastMessage = ""
    
    # function used to check if it is a valid string for android
    def checkStringForAndroid ( self , string: str ) -> bool :
        #
        # if it is a valid string
        if string != "" and string [ 0 ].isdigit ( ) and \
                (
                        "DebuggableApplications" in string or
                        "GnuDebugger_GDB" in string or
                        "JavaDebugWireProtocol_JDWP" in string or
                        "DeveloperOptions" in string or
                        "UsbChecker" in string or
                        "SensorListener" in string or
                        "Ptracer" in string or
                        "AppManagement" in string
                ) :
            #
            # return that it is a valid string
            return True
        #
        # if it is not a valid string
        else :
            #
            # return that it is not a valid string
            return False
    
    # function used to check if it is a valid string for ptracer
    def checkStringForPtracer ( self , string: str ) -> None :
        #
        # if it is a valid string
        if string != "" and \
                (
                        (string.startswith ( "------------------ SYSCALL" ) and string.endswith ( "------------------" )) or
                        string.startswith ( "PID:" ) or
                        string.startswith ( "SPID:" ) or
                        string.startswith ( "Timestamp:" ) or
                        string.startswith ( "Syscall =" ) or
                        string.startswith ( "Return value:" )
                ) :
            #
            # return that it is a valid string
            return True
        #
        # if it is not a valid string
        else :
            #
            # return that it is not a valid string
            return False
    
    # function used to print actual message
    def printActualMessage ( self , message: str ) :
        #
        # only on android socket
        if self.name == "ptracer" :
            #
            # print actual message
            # print ( message )
            pass
        #
        """# call the relative manager if it is a valid message
        valid = self.callManagerActualInput ( message )
        #
        # if it is valid
        if valid :
            #
            # write the actual message in the log
            self.manageFile.writeIntoFile ( message )"""
    
    # function used to call the single manager of each type of input
    def callManagerActualInput ( self , message ) -> bool :
        pass
    
    # function used to close the tcp tcpSocket and the other
    def closeAll ( self ) :
        #
        # close the other
        self.manageFile.closeFile ( )
        # close the connection
        self.conn.close ( )
        # close the management of tcpSocket
        self.serversocket.close ( )
