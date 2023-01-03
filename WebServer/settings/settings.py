# class used to set all usefully constants
import socket

class Settings:
    
    # constructor for the setting class
    def __init__(self):
        # set the values for all constants
        self.__setConstants()
    
    # function used to set all constants
    def __setConstants(self):
        # name for the file to store all logs from ptracer
        self.__filenameLogsPtracer = "savedlogs/ptracer.log"
        
        # name for the file to store all logs from android application
        self.__filenameLogsAndroid = "savedlogs/androidapp.log"
        
        # variable to define how to open the file to save the logs
        self.__howToOpenFiles = "w"
        
        # variable to define the port to receive data from ptracer
        self.__portSocketPtracer = 1500
        
        # variable to define the port to receive data from android application
        self.__portSocketAndroid = 1501
        
        # variable to define the port to send data using a terminal
        self.__portSocketTerminal = 1502
        
        # variable used to set the maximum number of connected clients
        self.__maximumNumberConnectedClients = 1
        
        # hostname for the tcp manageSocket
        self.__hostname = socket.gethostname()
        
        # variable to define the max dimension of socket data
        self.__dimensionSocketData = 10240
    
    # function used to change the ptracer folder and name for logs
    def setPtracerFolderLogs(self, filenameLogsPtracer):
        # update the folder and name of logs for ptracer
        self.__filenameLogsPtracer = filenameLogsPtracer
    
    # function used to change the android folder and name for logs
    def setAndroidFolderLogs(self, filenameLogsAndroid):
        # update the folder and name of logs for android
        self.__filenameLogsAndroid = filenameLogsAndroid
    
    # function used to change how to open the logs files
    def setHowToOpenFile(self, howToOpenFiles):
        # update how to open the logs files
        self.__howToOpenFiles = howToOpenFiles
    
    # function used to change the port for the ptracer socket
    def setPortPtracerSocket(self, portSocketPtracer):
        # update the port for the ptracer socket
        self.__portSocketPtracer = portSocketPtracer
    
    # function used to change the port for the android socket
    def setPortAndroidSocket(self, portAndroidSocket):
        # update the port for the android socket
        self.__portSocketAndroid = portAndroidSocket
    
    # function used to change the port for the terminal socket
    def setPortTerminalSocket(self, portTerminalSocket):
        # update the port for the terminal socket
        self.__portSocketTerminal = portTerminalSocket
    
    # function used to change the maximum number of connected clients
    def setNumberConnectedClients(self, numberConnectedClients):
        # update the max number of connected clients
        self.__maximumNumberConnectedClients = numberConnectedClients
    
    # function used to change the dimension of socket data
    def setDimensionSocketData(self, dimensionSocketData):
        # update the dimension of socket data
        self.__dimensionSocketData = dimensionSocketData
    
    # function used to get the port for ptracer
    def getPtracerPort(self):
        # return the port for ptracer
        return self.__portSocketPtracer
    
    # function used to get the port for android
    def getAndroidPort(self):
        # return the port for android
        return self.__portSocketAndroid
    
    # function used to get the port for the terminal
    def getTerminalPort(self):
        # return the port for terminal
        return self.__portSocketTerminal
    
    # function used to get the folder and file for ptracer logs
    def getPtracerLogs(self):
        # return the folder and the filename for ptracer logs
        return self.__filenameLogsPtracer
    
    # function used to get the folder and file for android logs
    def getAndroidLogs(self):
        # return the folder and the filename for android logs
        return self.__filenameLogsAndroid
    
    # function used to get how open the files
    def getHowToOpenFiles(self):
        # return how to open the files
        return self.__howToOpenFiles
    
    # function used to get the hostname for the socket
    def getHostname(self):
        # return the hostname
        return self.__hostname
    
    # function used to get the max number of connected clients
    def getMaxNumberConnectedClients(self):
        # return the max number of connected clients
        return self.__maximumNumberConnectedClients
    
    # function used to get the dimension of socket data
    def getDimensionSocketData(self):
        # return the dimension of socket data
        return self.__dimensionSocketData
