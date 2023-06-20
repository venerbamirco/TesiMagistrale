import os
from datetime import datetime

from algorithm.dataStructure.other.file import File
from algorithm.manager.android import AndroidManager
from algorithm.manager.ptracer import PtracerManager
from algorithm.settings.settings import Settings
from algorithm.training.training import Training

# class used to manage all the parts of the algorithm
class Manager ( AndroidManager , PtracerManager ) :
    
    # constructor to initialize the manager
    def __init__ ( self ) -> None :
        #
        # initialize training manager
        self.training: Training = Training ( )
        #
        # initialize android manager
        AndroidManager.__init__ ( self , self.training )
        #
        # initialize ptracer manager
        PtracerManager.__init__ ( self , self.training )
        #
        # flag to check if android socket is terminated
        self.flagAndroidSocket = False
        #
        # flag to check if ptracer socket is terminated
        self.flagPtracerSocket = False
    
    # function used to set terminated the android socket
    def setAndroidSocketTerminated ( self ) :
        #
        # set the flag of android socket to true
        self.flagAndroidSocket = True
    
    # function used to set terminated the ptracer socket
    def setPtracerSocketTerminated ( self ) :
        #
        # set the flag of ptracer socket to true
        self.flagPtracerSocket = True
    
    # function used to save the log for all single managers
    def saveLogsEachManager ( self ) -> None :
        #
        # white until each socket is closed
        while not self.flagAndroidSocket or not self.flagPtracerSocket :
            pass
        #
        # create the main directory for the output structure logs
        mainDirOutputStructureLogs: str = os.path.join ( os.getcwd ( ) , "logs\\analyses\\" , datetime.now ( ).strftime ( "%Y-%m-%d--%H-%M-%S" ) )
        #
        # create the main directory for the actual logs
        os.mkdir ( mainDirOutputStructureLogs )
        #
        # create the subdirectory for android logs
        os.mkdir ( os.path.join ( mainDirOutputStructureLogs , "android" ) )
        #
        # create the subdirectory for ptracer logs
        os.mkdir ( os.path.join ( mainDirOutputStructureLogs , "ptracer" ) )
        #
        # create the subdirectory for other logs
        os.mkdir ( os.path.join ( mainDirOutputStructureLogs , "other" ) )
        #
        # save list of device
        fileDevices = File ( os.path.abspath ( "./logs/training/other/Devices.log" ) , "w" )
        fileDevices.writeIntoFile ( str ( self.training.devices ) )
        #
        # file csv flag
        fileCsv = File ( mainDirOutputStructureLogs + "\\Android\\" + "fileCsv.csv" , "w" )
        fileCsv.writeIntoFile ( "fakeclient=" + str ( Settings.fakeClient ) )
        fileCsv.writeIntoFile ( "Start,DebugApp,DeveloperOptions,ChargingType,PtracerStarted,StationaryDevice,SensorAlert,DebuggerFound,InstructionMuchTime,SubsequenceFound,SequenceNotSecure" )
        #
        # print in csv file all security level flags
        order = [ ]
        for i in range ( 0 , len ( self.training.devices.listDevices [ 0 ].securityLevel.timestampFlags ) ) :
            if self.training.devices.listDevices [ 0 ].securityLevel.timestampFlags [ i ] != "" :
                order.append ( (i , self.training.devices.listDevices [ 0 ].securityLevel.timestampFlags [ i ]) )
        s = ""
        done = [ ]
        finish = [ ]
        while len ( order ) > 0 :
            minimum = min ( order , key = lambda x : x [ 1 ] )
            x , y = minimum
            done.append ( x )
            order.remove ( minimum )
            for i in order :
                x1 , y1 = i
                if y == y1 :
                    done.append ( x1 )
                    order.remove ( i )
            s = s + y + ","
            s1 = ""
            for i in range ( 0 , 10 ) :
                if i in done :
                    if i == 9 :
                        s = s + "alert"
                        s1 = s1 + "alert"
                    else :
                        s = s + "alert,"
                        s1 = s1 + "alert,"
                else :
                    if i == 9 :
                        s = s + "no"
                        s1 = s1 + "no"
                    else :
                        s = s + "no,"
                        s1 = s1 + "no,"
            s = s + "\n"
            finish.append ( (y , s1) )
        fileCsv.writeIntoFile ( s )
        #
        # save all android logs
        self.saveAndroidLogs ( mainDirOutputStructureLogs )
        #
        # save all ptracer logs
        self.savePtracerLogs ( mainDirOutputStructureLogs,finish )
