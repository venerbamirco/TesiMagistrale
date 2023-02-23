import datetime
import socket

# class used to set all usefully constants
class Settings :
    
    # constructor for the settings class
    def __init__ ( self ) :
        #
        # ----------------------------------------------------------------------- LOG FILES
        #
        # name for the extension of log other
        self.extensionLogFile = ".log"
        #
        # name for the other to store all logs from ptracer
        self.filenameLogsPtracer = "logs/receive/ptracer/ptracer"
        #
        # name for the other to store all logs from android application
        self.filenameLogsAndroid = "logs/receive/android/android"
        #
        # variable to define how to open the other to save the logs
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
        # variable to define the port to receive data from ptracer in training mode
        self.portSocketPtracerTraining = 1502
        #
        # variable to define the port to receive data from android application in training mode
        self.portSocketAndroidTraining = 1503
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
    
    # function used to get the folder and other for ptracer logs
    def getPtracerLogs ( self ) :
        # return the folder and the filename for ptracer logs
        return self.filenameLogsPtracer + "--" + datetime.datetime.now ( ).strftime ( "%Y-%m-%d--%H-%M-%S" ) + self.extensionLogFile
    
    # function used to get the folder and other for android logs
    def getAndroidLogs ( self ) :
        # return the folder and the filename for android logs
        return self.filenameLogsAndroid + "--" + datetime.datetime.now ( ).strftime ( "%Y-%m-%d--%H-%M-%S" ) + self.extensionLogFile
