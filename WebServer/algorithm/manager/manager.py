import os
from datetime import datetime

from algorithm.manager.android import AndroidManager
from algorithm.manager.ptracer import PtracerManager
from algorithm.trainingAndCheck.training import Training
from settings.settings import Settings

# class used to manage all the parts of the algorithm
class Manager ( AndroidManager , PtracerManager ) :
    
    # constructor to initialize the manager
    def __init__ ( self , settings: Settings ) -> None :
        #
        # initialize trainingAndCheck manager
        self.training: Training = Training ( )
        #
        # initialize android manager
        AndroidManager.__init__ ( self , settings , self.training)
        #
        # initialize ptracer manager
        PtracerManager.__init__ ( self , settings , self.training )
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
        # save all android logs
        self.saveAndroidLogs ( mainDirOutputStructureLogs )
        #
        # save all ptracer logs
        self.savePtracerLogs ( mainDirOutputStructureLogs )
