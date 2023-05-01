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
        # name for the other to store all logs from android application
        self.filenameLogsAndroid = "logs/receive/android/android"
        #
        # name for training of analyses log
        self.filenameTrainingAnalyses = "logs/training/ptracer/Analyses"
        #
        # name for training of sequences log
        self.filenameTrainingSequences = "logs/training/ptracer/Sequences"
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
        # variable used to set the maximum number of connected clients
        self.maximumNumberConnectedClients = 1
        #
        # hostname for the tcp tcpSocket
        self.hostname = socket.gethostname ( )
        #
        # variable to define the max dimension of tcpSocket data
        self.dimensionSocketData = 100
        #
        # variable to define the timeout for connection
        self.timeout = 1
        #
        # ----------------------------------------------------------------------- OTHER
        #
        # training mode
        self.training = True
        #
        # ----------------------------------------------------------------------- SECURITY LELEL
        #
        # possible security levels
        self.possibleSecurityLevel = [
            "Debuggable applications" ,  #
            "Developer options" ,  #
            "Charging type" ,  #
            "Ptracer Started" ,  #
            "Stationary device" ,  #
            "Sensor alerts" ,  #
            "Debugger found" ,  #
            "Instructions much time" ,  #
            "Subsequences found" ,
            "Sequence not secure"  #
        ]
    
    # function used to get the folder and other for ptracer logs
    def getPtracerLogs ( self ) :
        # return the folder and the filename for ptracer logs
        return self.filenameLogsPtracer + "--" + datetime.datetime.now ( ).strftime ( "%Y-%m-%d--%H-%M-%S" ) + self.extensionLogFile
    
    # function used to get the folder and other for android logs
    def getAndroidLogs ( self ) :
        # return the folder and the filename for android logs
        return self.filenameLogsAndroid + "--" + datetime.datetime.now ( ).strftime ( "%Y-%m-%d--%H-%M-%S" ) + self.extensionLogFile
