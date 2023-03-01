import os
from datetime import datetime

from dataStructure.android.charging import Charging
from dataStructure.android.debuggableApplications import DebuggableApplications
from dataStructure.android.debuggers import Debuggers
from dataStructure.android.developerOptions import DeveloperOptions
from dataStructure.android.lifecycle import Lifecycle
from dataStructure.android.sensorAlert import SensorAlert
from dataStructure.android.sensorCalibration import SensorCalibration
from dataStructure.android.sensorNumber import SensorNumber
from dataStructure.android.sensorText import SensorText
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
        #
        # initialize the sensor alerts manager
        self.sensorAlertsManager = SensorAlert ( )
        #
        # initialize the sensor calibration manager
        self.sensorCalibrationManager = SensorCalibration ( )
        #
        # initialize the lifecycle manager
        self.lifecycleManager = Lifecycle ( )
        #
        # initialize the sensor number manager
        self.sensorNumberManager = SensorNumber ( )
        #
        # initialize the sensor text manager
        self.sensorTextManager = SensorText ( )
    
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
    
    # function used to add a record in debuggers
    def addSensorAlertRecord ( self , record: str ) -> None :
        #
        # input: 1677589219936 SensorListener: Azimuth alert
        # input: 1677589219938 SensorListener: Pitch ok
        # input: 1677589220855 SensorListener: Device is correctly used
        #
        #
        # split the input string using the space character
        listInputWords: list [ str ] = record.split ( )
        #
        # get status of alert
        status: bool = not "ok" in record
        #
        # get timestamp
        timestamp: int = int ( listInputWords [ 0 ] )
        #
        # if azimuth alert
        if "Azimuth" in record :
            #
            # add azimuth alert record
            self.sensorAlertsManager.addAzimuthAlert ( status , timestamp )
        #
        # if pitch alert
        elif "Pitch" in record :
            #
            # add pitch alert record
            self.sensorAlertsManager.addPitchAlert ( status , timestamp )
        #
        # if roll alert
        elif "Roll" in record :
            #
            # add roll alert record
            self.sensorAlertsManager.addRollAlert ( status , timestamp )
        #
        # if device correctly used
        elif "Device" in record :
            #
            # add device correctly used
            self.sensorAlertsManager.addCorrectlyUsed ( True , timestamp )
    
    # function used to add a record in calibration
    def addCalibrationRecord ( self , record: str ) -> None :
        #
        # input: 1677592653070 SensorListener: First calibration done
        # input: 1677592653150 SensorListener: Calibration done
        #
        # split the input string using the space character
        listInputWords: list [ str ] = record.split ( )
        #
        # get timestamp
        timestamp: int = int ( listInputWords [ 0 ] )
        #
        # add the calibration record in the relative manager
        self.sensorCalibrationManager.addCalibrationRecord ( True , timestamp )
    
    # function used to add a record in lifecycle
    def addLifecycleRecord ( self , record: str ) -> None :
        #
        # input: 1677660027357 AppManagement: onPause
        # input: 1677660057538 AppManagement: onResume
        #
        # split the input string using the space character
        listInputWords: list [ str ] = record.split ( )
        #
        # get timestamp
        timestamp: int = int ( listInputWords [ 0 ] )
        #
        # get if on pause
        onPause: bool = "onPause" in record
        #
        # get if on pause
        onResume: bool = "onResume" in record
        #
        # add the lifecycle record in the relative manager
        self.lifecycleManager.addLifecycleRecord ( onResume , onPause , timestamp )
    
    # function used to add a record in sensor numbers
    def addSensorNumberRecord ( self , record: str ) -> None :
        #
        # input: 1677662216435 SensorListener: Numbers: Azimuth 89 Pitch 0 Roll 0
        #
        # split the input string using the space character
        listInputWords: list [ str ] = record.split ( )
        #
        # get timestamp
        timestamp: int = int ( listInputWords [ 0 ] )
        #
        # get azimuth
        azimuth: int = int ( listInputWords [ 4 ] )
        #
        # get pitch
        pitch: int = int ( listInputWords [ 6 ] )
        #
        # get roll
        roll: int = int ( listInputWords [ 8 ] )
        #
        # add the lifecycle record in the relative manager
        self.sensorNumberManager.addSensorRecord ( azimuth , pitch , roll , timestamp )
    
    # function used to add a record in sensor texts
    def addSensorTextRecord ( self , record: str ) -> None :
        #
        # input: 1677662615922 SensorListener: Texts: Azimuth NORTH Pitch EAST Roll NORTH
        #
        # split the input string using the space character
        listInputWords: list [ str ] = record.split ( )
        #
        # get timestamp
        timestamp: int = int ( listInputWords [ 0 ] )
        #
        # get azimuth
        azimuth: str = listInputWords [ 4 ].lower ( )
        #
        # get pitch
        pitch: str = listInputWords [ 6 ].lower ( )
        #
        # get roll
        roll: str = listInputWords [ 8 ].lower ( )
        #
        # add the lifecycle record in the relative manager
        self.sensorTextManager.addSensorRecord ( azimuth , pitch , roll , timestamp )
    
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
        os.mkdir ( os.path.join(mainDirOutputStructureLogs, "android") )
        #
        # create the file for charging manager
        fileChargingManager = File ( mainDirOutputStructureLogs + "\\android\\Charging" + self.settings.extensionLogFile , "w" )
        fileChargingManager.writeIntoFile ( self.chargingManager )
        #
        # create the file for developer options manager
        fileDeveloperOptionsManager = File ( mainDirOutputStructureLogs + "\\android\\DeveloperOptions" + self.settings.extensionLogFile , "w" )
        fileDeveloperOptionsManager.writeIntoFile ( self.developerOptionsManager )
        #
        # create the file for debuggable applications manager
        fileDebuggableApplicationsManager = File ( mainDirOutputStructureLogs + "\\android\\DebuggableApplications" + self.settings.extensionLogFile , "w" )
        fileDebuggableApplicationsManager.writeIntoFile ( self.debuggableApplicationsManager )
        #
        # create the file for debuggers manager
        fileDebuggersManager = File ( mainDirOutputStructureLogs + "\\android\\Debuggers" + self.settings.extensionLogFile , "w" )
        fileDebuggersManager.writeIntoFile ( self.debuggersManager )
        #
        # create the file for sensor alerts manager
        fileSensorAlertsManager = File ( mainDirOutputStructureLogs + "\\android\\SensorAlerts" + self.settings.extensionLogFile , "w" )
        fileSensorAlertsManager.writeIntoFile ( self.sensorAlertsManager )
        #
        # create the file for calibration manager
        fileSensorCalibrationManager = File ( mainDirOutputStructureLogs + "\\android\\SensorCalibration" + self.settings.extensionLogFile , "w" )
        fileSensorCalibrationManager.writeIntoFile ( self.sensorCalibrationManager )
        #
        # create the file for lifecycle manager
        fileLifecycleManager = File ( mainDirOutputStructureLogs + "\\android\\Lifecycle" + self.settings.extensionLogFile , "w" )
        fileLifecycleManager.writeIntoFile ( self.lifecycleManager )
        #
        # create the file for sensor number manager
        sensorNumberManager = File ( mainDirOutputStructureLogs + "\\android\\SensorNumber" + self.settings.extensionLogFile , "w" )
        sensorNumberManager.writeIntoFile ( self.sensorNumberManager )
        #
        # create the file for sensor text manager
        sensorTextManager = File ( mainDirOutputStructureLogs + "\\android\\SensorText" + self.settings.extensionLogFile , "w" )
        sensorTextManager.writeIntoFile ( self.sensorTextManager )
