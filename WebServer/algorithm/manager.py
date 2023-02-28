import os
from datetime import datetime

from dataStructure.android.charging import Charging
from dataStructure.android.debuggableApplications import DebuggableApplications
from dataStructure.android.debuggers import Debuggers
from dataStructure.android.developerOptions import DeveloperOptions
from dataStructure.other.file import File
from settings.settings import Settings
from utils.functions import strToBool

# class used to manage all the parts of the algorithm
class Manager :
    
    # constructor to initialize the manager
    def __init__ ( self , settings: Settings ) -> None :
        #
        # save the reference for settings
        self.settings = settings
        #
        # flag to check if android socket is terminated
        self.flagAndroidSocket = False
        #
        # flag to check if ptracer socket is terminated
        self.flagPtracerSocket = False
        #
        # initialize the charging manager
        self.chargingManager = Charging ( )
        #
        # initialize the developer options manager
        self.developerOptionsManager = DeveloperOptions ( )
        #
        # initialize the debuggable applications manager
        self.debuggableApplicationsManager = DebuggableApplications ( )
        #
        # initialize the debuggers manager
        self.debuggersManager = Debuggers ( )
    
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
    
    # function used to add a record in charging
    def addChargingRecord ( self , record: str ) -> None :
        #
        # input: 1677155940999 UsbChecker: ischarg: false usbcharg: false accharg: false
        #
        # split the input string using the space character
        listInputWords: list [ str ] = record.split ( )
        #
        # get timestamp
        timestamp: int = int ( listInputWords [ 0 ] )
        #
        # get if it is charging
        isCharging: bool = strToBool ( listInputWords [ 3 ] )
        #
        # get if it is charging using usb
        usbCharging: bool = strToBool ( listInputWords [ 5 ] )
        #
        # get if it is charging using ac
        acCharging: bool = strToBool ( listInputWords [ 7 ] )
        #
        # add the charging record in the relative manager
        self.chargingManager.addChargingRecord ( isCharging , usbCharging , acCharging , timestamp )
    
    # function used to add a record in developer options
    def addDeveloperOptionsRecord ( self , record: str ) -> None :
        #
        # input: 1677574950586 DeveloperOptions: adb: true devops: true
        #
        # split the input string using the space character
        listInputWords: list [ str ] = record.split ( )
        #
        # get timestamp
        timestamp: int = int ( listInputWords [ 0 ] )
        #
        # get if adb is enabled
        adbEnabled: bool = strToBool ( listInputWords [ 3 ] )
        #
        # get if developer options are enabled
        devOpsEnabled: bool = strToBool ( listInputWords [ 5 ] )
        #
        # add the developer options record in the relative manager
        self.developerOptionsManager.addDeveloperOptionRecord ( devOpsEnabled , adbEnabled , timestamp )
    
    # function used to add a record in debuggable applications
    def addDebuggableApplicationsRecord ( self , record: str ) -> None :
        #
        # input: 1677576249603 DebuggableApplications: Progetto Android
        #
        # split the input string using the : character
        listInputWords: list [ str ] = record.split ( ":" )
        #
        # get name of the debuggable application
        debuggableApplication: str = listInputWords [ 1 ].strip ( )
        #
        # split the input string using the space character
        listInputWords: list [ str ] = record.split ( )
        #
        # get timestamp
        timestamp: int = int ( listInputWords [ 0 ] )
        #
        # add the debuggable application record in the relative manager
        self.debuggableApplicationsManager.addDebuggableApplication ( debuggableApplication , timestamp )
    
    # function used to add a record in debuggers
    def addDebuggerRecord ( self , record: str ) -> None :
        #
        # input: 1677577421696 GnuDebugger_GDB: Debugger found
        # input: 1677577421696 JavaDebugWireProtocol_JDWP: Debugger found
        #
        # split the input string using the space character
        listInputWords: list [ str ] = record.split ( )
        #
        # get timestamp
        timestamp: int = int ( listInputWords [ 0 ] )
        #
        # if it is a gdb debugger
        if "GnuDebugger_GDB" in record :
            #
            # set the gdb debugger in the relative manager
            self.debuggersManager.setFoundGdbDebugger ( timestamp )
        #
        # if it is a jdwp debugger
        elif "JavaDebugWireProtocol_JDWP" in record :
            #
            # set the jdwp debugger in the relative manager
            self.debuggersManager.setFoundJdwpDebugger ( timestamp )
    
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
        # create the directory
        os.mkdir ( mainDirOutputStructureLogs )
        #
        # create the file for charging manager
        fileChargingManager = File ( mainDirOutputStructureLogs + "\\Charging" + self.settings.extensionLogFile , "w" )
        fileChargingManager.writeIntoFile ( self.chargingManager )
        #
        # create the file for developer options manager
        fileDeveloperOptionsManager = File ( mainDirOutputStructureLogs + "\\DeveloperOptions" + self.settings.extensionLogFile , "w" )
        fileDeveloperOptionsManager.writeIntoFile ( self.developerOptionsManager )
        #
        # create the file for debuggable applications manager
        fileDebuggableApplicationsManager = File ( mainDirOutputStructureLogs + "\\DebuggableApplications" + self.settings.extensionLogFile , "w" )
        fileDebuggableApplicationsManager.writeIntoFile ( self.debuggableApplicationsManager )
        #
        # create the file for debuggers manager
        fileDebuggersManager = File ( mainDirOutputStructureLogs + "\\Debuggers" + self.settings.extensionLogFile , "w" )
        fileDebuggersManager.writeIntoFile ( self.debuggersManager )
