import datetime
import socket

# class used to set all usefully constants
class Settings :
    
    # constructor for the settings class
    def __init__ ( self ) :
        #
        # ----------------------------------------------------------------------- LOG FILES
        #
        # name for the extension of log file
        self.extensionLogFile = ".log"
        #
        # name for the file to store all logs from ptracer
        self.filenameLogsPtracer = "savedlogs/ptracer/ptracer"
        #
        # name for the file to store all logs from android application
        self.filenameLogsAndroid = "savedlogs/android/android"
        #
        # variable to define how to open the file to save the logs
        self.howToOpenFiles = "w"
        #
        # ----------------------------------------------------------------------- SOCKET TCP
        #
        # variable to define the port to receive data from ptracer
        self.portSocketPtracer = 1500
        #
        # variable to define the port to receive data from android application
        self.portSocketAndroid = 1501
        #
        # variable to define the port to send data using a terminal
        self.portSocketTerminal = 1502
        #
        # variable used to set the maximum number of connected clients
        self.maximumNumberConnectedClients = 1
        #
        # hostname for the tcp tcpSocket
        self.hostname = socket.gethostname ( )
        #
        # variable to define the max dimension of tcpSocket data
        self.dimensionSocketData = 10240
        #
        # ----------------------------------------------------------------------- OTHER
        #
    
    # function used to get the folder and file for ptracer logs
    def getPtracerLogs ( self ) :
        # return the folder and the filename for ptracer logs
        return self.filenameLogsPtracer + "--" + datetime.datetime.now ( ).strftime ( "%Y-%m-%d--%H-%M-%S" ) + self.extensionLogFile
    
    # function used to get the folder and file for android logs
    def getAndroidLogs ( self ) :
        # return the folder and the filename for android logs
        return self.filenameLogsAndroid + "--" + datetime.datetime.now ( ).strftime ( "%Y-%m-%d--%H-%M-%S" ) + self.extensionLogFile
