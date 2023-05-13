import datetime
import socket

# class used to set all usefully constants
class Settings :
    #
    # ----------------------------------------------------------------------- LOG FILES
    #
    # name for the extension of log other
    extensionLogFile = ".log"
    #
    # name for the other to store all logs from ptracer
    filenameLogsPtracer = "logs/receive/ptracer/ptracer"
    #
    # name for the other to store all logs from android application
    filenameLogsAndroid = "logs/receive/android/android"
    #
    # name for the other to store all logs from android application
    filenameLogsAndroid = "logs/receive/android/android"
    #
    # name for training of analyses log
    filenameTrainingAnalyses = "logs/training/ptracer/Analyses"
    #
    # name for training of sequences log
    filenameTrainingSequences = "logs/training/ptracer/Sequences"
    #
    # variable to define how to open the other to save the logs
    howToOpenFiles = "w"
    #
    # ----------------------------------------------------------------------- SOCKET TCP
    #
    # variable to define the port to receive data from ptracer
    portSocketPtracer = 1500
    #
    # variable to define the port to receive data from android application
    portSocketAndroid = 1501
    #
    # variable used to set the maximum number of connected clients
    maximumNumberConnectedClients = 1
    #
    # hostname for the tcp tcpSocket
    hostname = socket.gethostname ( )
    #
    # variable to define the max dimension of tcpSocket data
    dimensionSocketData = 100
    #
    # variable to define the timeout for connection
    timeout = 1
    #
    # ----------------------------------------------------------------------- PRINT ROW
    #
    # say if a debugger is found
    debuggerFound: bool = True
    #
    # say security level of device
    securityLevel: bool = True
    #
    # say found new things in security level
    foundNewThingSecurityLevel: bool = True
    #
    # say new duration instruction
    newDurationInstruction: bool = True
    #
    # say invalid sequence
    invalidSequence: bool = True
    #
    # say percentage valid and invalid sequence
    percentageValidInvalidSequence: bool = False
    #
    # ----------------------------------------------------------------------- SECURITY LELEL
    #
    # possible security levels
    possibleSecurityLevel = [
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
    #
    # ----------------------------------------------------------------------- Training mode
    #
    # training mode
    training = False
    #
    # ----------------------------------------------------------------------- NUMBER OF THINGS SECURE -> INSECURE
    #
    # number of sensors alerts
    numberSensorAlerts = 5
    #
    # number of instructions with longer durations
    numberInstructionLongerDuration = 5
    #
    # number of insecure sequence
    numberInsecureSequence = 5
    #
    # number of insecure subsequences
    numberInsecureSubsequences = 5
    #
    # number of stationary device
    numberStationaryDevice = 5
    
    #
    
    # function used to get the folder and other for ptracer logs
    def getPtracerLogs ( self ) :
        # return the folder and the filename for ptracer logs
        return Settings.filenameLogsPtracer + "--" + datetime.datetime.now ( ).strftime ( "%Y-%m-%d--%H-%M-%S" ) + Settings.extensionLogFile
    
    # function used to get the folder and other for android logs
    def getAndroidLogs ( self ) :
        # return the folder and the filename for android logs
        return Settings.filenameLogsAndroid + "--" + datetime.datetime.now ( ).strftime ( "%Y-%m-%d--%H-%M-%S" ) + Settings.extensionLogFile
