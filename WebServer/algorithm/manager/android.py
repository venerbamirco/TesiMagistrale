from dataStructure.android.charging import Charging
from dataStructure.android.debuggableApplications import DebuggableApplications
from dataStructure.android.debuggers import Debuggers
from dataStructure.android.developerOptions import DeveloperOptions
from dataStructure.android.lifecycle import Lifecycle
from dataStructure.android.ptracer import Ptracer
from dataStructure.android.sensorAlert import SensorAlert
from dataStructure.android.sensorCalibration import SensorCalibration
from dataStructure.android.sensorNumber import SensorNumber
from dataStructure.android.sensorText import SensorText
from dataStructure.other.file import File
from settings.settings import Settings
from utils.functions import strToBool

# class used for the android manager
class AndroidManager :
    
    # constructor to initialize the android manager
    def __init__ ( self , settings: Settings ) -> None :
        #
        # save the reference for settings
        self.settings: Settings = settings
        #
        # initialize the charging manager
        self.chargingManager: Charging = Charging ( )
        #
        # initialize the developer options manager
        self.developerOptionsManager: DeveloperOptions = DeveloperOptions ( )
        #
        # initialize the debuggable applications manager
        self.debuggableApplicationsManager: DebuggableApplications = DebuggableApplications ( )
        #
        # initialize the debuggers manager
        self.debuggersManager: Debuggers = Debuggers ( )
        #
        # initialize the sensor alerts manager
        self.sensorAlertsManager: SensorAlert = SensorAlert ( )
        #
        # initialize the sensor calibration manager
        self.sensorCalibrationManager: SensorCalibration = SensorCalibration ( )
        #
        # initialize the lifecycle manager
        self.lifecycleManager: Lifecycle = Lifecycle ( )
        #
        # initialize the sensor number manager
        self.sensorNumberManager: SensorNumber = SensorNumber ( )
        #
        # initialize the sensor text manager
        self.sensorTextManager: SensorText = SensorText ( )
        #
        # initialize the ptracer manager
        self.ptracerManager: Ptracer = Ptracer ( )
    
    # function used to add a record in charging
    def addChargingRecord ( self , record: str ) -> None :
        #
        # input: 1679045438927@UsbChecker: ischarg: #true# usbcharg: #false# accharg: #true#
        #
        # get timestamp
        timestamp: int = int ( record.split ( "@" ) [ 0 ] )
        #
        # get if it is charging
        isCharging: bool = strToBool ( record.split ( "#" ) [ 1 ].strip ( ) )
        #
        # get if it is charging using usb
        usbCharging: bool = strToBool ( record.split ( "#" ) [ 3 ].strip ( ) )
        #
        # get if it is charging using ac
        acCharging: bool = strToBool ( record.split ( "#" ) [ 5 ].strip ( ) )
        #
        # add the charging record in the relative manager
        self.chargingManager.addChargingRecord ( isCharging , usbCharging , acCharging , timestamp )
    
    # function used to add a record in developer options
    def addDeveloperOptionsRecord ( self , record: str ) -> None :
        #
        # input: 1679045438874@DeveloperOptions: adb: #true# devops: #true#
        #
        # get timestamp
        timestamp: int = int ( record.split ( "@" ) [ 0 ] )
        #
        # get if adb is enabled
        adbEnabled: bool = strToBool ( record.split ( "#" ) [ 1 ].strip ( ) )
        #
        # get if developer options are enabled
        devOpsEnabled: bool = strToBool ( record.split ( "#" ) [ 3 ].strip ( ) )
        #
        # add the developer options record in the relative manager
        self.developerOptionsManager.addDeveloperOptionRecord ( devOpsEnabled , adbEnabled , timestamp )
    
    # function used to add a record in debuggable applications
    def addDebuggableApplicationsRecord ( self , record: str ) -> None :
        #
        # input: 1677576249603@DebuggableApplications: Progetto Android
        #
        # get timestamp
        timestamp: int = int ( record.split ( "@" ) [ 0 ] )
        #
        # get name of the debuggable application
        debuggableApplication: str = record.split ( "#" ) [ 1 ].strip ( )
        #
        # add the debuggable application record in the relative manager
        self.debuggableApplicationsManager.addDebuggableApplication ( debuggableApplication , timestamp )
    
    # function used to add a record in debuggers
    def addDebuggerRecord ( self , record: str ) -> None :
        #
        # input: 1677577421696@GnuDebugger_GDB: Debugger found
        # input: 1677577421696@JavaDebugWireProtocol_JDWP: Debugger found
        #
        # get timestamp
        timestamp: int = int ( record.split ( "@" ) [ 0 ] )
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
        # input: 1679046491187@SensorListener: #azimuthok#
        # input: 1679046491189@SensorListener: #rollalert#
        # input: 1679046491769@SensorListener: #deviceiscorrectlyused#
        #
        # get timestamp
        timestamp: int = int ( record.split ( "@" ) [ 0 ] )
        #
        # get status of alert
        status: bool = not "ok" in record
        #
        # if azimuth alert
        if "azimuth" in record :
            #
            # add azimuth alert record
            self.sensorAlertsManager.addAzimuthAlert ( status , timestamp )
        #
        # if pitch alert
        elif "pitch" in record :
            #
            # add pitch alert record
            self.sensorAlertsManager.addPitchAlert ( status , timestamp )
        #
        # if roll alert
        elif "roll" in record :
            #
            # add roll alert record
            self.sensorAlertsManager.addRollAlert ( status , timestamp )
        #
        # if device correctly used
        elif "device" in record :
            #
            # add device correctly used
            self.sensorAlertsManager.addCorrectlyUsed ( True , timestamp )
    
    # function used to add a record in calibration
    def addCalibrationRecord ( self , record: str ) -> None :
        #
        # input: 1679046487172@SensorListener: #firstcalibrationdone#
        # input: 1679046487215@SensorListener: #calibrationdone#
        #
        # get timestamp
        timestamp: int = int ( record.split ( "@" ) [ 0 ] )
        #
        # add the calibration record in the relative manager
        self.sensorCalibrationManager.addCalibrationRecord ( True , timestamp )
    
    # function used to add a record in lifecycle
    def addLifecycleRecord ( self , record: str ) -> None :
        #
        # input: 1679045453213@AppManagement: #onpause#
        # input: 1679046485211@AppManagement: #onresume#
        #
        # get timestamp
        timestamp: int = int ( record.split ( "@" ) [ 0 ] )
        #
        # get if on pause
        onPause: bool = "onpause" in record
        #
        # get if on pause
        onResume: bool = "onresume" in record
        #
        # add the lifecycle record in the relative manager
        self.lifecycleManager.addLifecycleRecord ( onResume , onPause , timestamp )
    
    # function used to add a record in sensor numbers
    def addSensorNumberRecord ( self , record: str ) -> None :
        #
        # input: 1679046489462@SensorListener: Numbers: Azimuth #192# Pitch #-52# Roll #182#
        #
        # get timestamp
        timestamp: int = int ( record.split ( "@" ) [ 0 ] )
        #
        # get azimuth
        azimuth: int = int ( record.split ( "#" ) [ 1 ].strip ( ) )
        #
        # get pitch
        pitch: int = int ( record.split ( "#" ) [ 3 ].strip ( ) )
        #
        # get roll
        roll: int = int ( record.split ( "#" ) [ 5 ].strip ( ) )
        #
        # add the lifecycle record in the relative manager
        self.sensorNumberManager.addSensorRecord ( azimuth , pitch , roll , timestamp )
    
    # function used to add a record in sensor texts
    def addSensorTextRecord ( self , record: str ) -> None :
        #
        # input: 1679045442524@SensorListener: Texts: Azimuth #EAST# Pitch #NORTH# Roll #NORTH#
        #
        # get timestamp
        timestamp: int = int ( record.split ( "@" ) [ 0 ] )
        #
        # get azimuth
        azimuth: str = record.split ( "#" ) [ 1 ].strip ( ).lower ( )
        #
        # get pitch
        pitch: str = record.split ( "#" ) [ 3 ].strip ( ).lower ( )
        #
        # get roll
        roll: str = record.split ( "#" ) [ 5 ].strip ( ).lower ( )
        #
        # add the lifecycle record in the relative manager
        self.sensorTextManager.addSensorRecord ( azimuth , pitch , roll , timestamp )
    
    # function used to add a record in ptracer
    def addPtracerRecord ( self , record: str ) -> None :
        #
        # input: 1679150488434@Ptracer: #started#
        # input: 1679150437214@Ptracer: #error#
        #
        # get timestamp
        timestamp: int = int ( record.split ( "@" ) [ 0 ] )
        #
        # if ptracer process is started
        if "started" in record :
            #
            # set started status on ptracer
            self.ptracerManager.setStartedPtracerProcess ( timestamp )
        #
        # else if ptracer process is crashed
        elif "error" in record :
            #
            # set crashed status on ptracer
            self.ptracerManager.setCrashedPtracerProcess ( timestamp )
    
    # function used to save the all android logs
    def saveAndroidLogs ( self , mainDirOutputStructureLogs: str ) :
        #
        # create the file for charging manager
        fileChargingManager: File = File ( mainDirOutputStructureLogs + "\\android\\Charging" + self.settings.extensionLogFile , "w" )
        fileChargingManager.writeIntoFile ( self.chargingManager )
        #
        # create the file for developer options manager
        fileDeveloperOptionsManager: File = File ( mainDirOutputStructureLogs + "\\android\\DeveloperOptions" + self.settings.extensionLogFile , "w" )
        fileDeveloperOptionsManager.writeIntoFile ( self.developerOptionsManager )
        #
        # create the file for debuggable applications manager
        fileDebuggableApplicationsManager: File = File ( mainDirOutputStructureLogs + "\\android\\DebuggableApplications" + self.settings.extensionLogFile , "w" )
        fileDebuggableApplicationsManager.writeIntoFile ( self.debuggableApplicationsManager )
        #
        # create the file for debuggers manager
        fileDebuggersManager: File = File ( mainDirOutputStructureLogs + "\\android\\Debuggers" + self.settings.extensionLogFile , "w" )
        fileDebuggersManager.writeIntoFile ( self.debuggersManager )
        #
        # create the file for sensor alerts manager
        fileSensorAlertsManager: File = File ( mainDirOutputStructureLogs + "\\android\\SensorAlerts" + self.settings.extensionLogFile , "w" )
        fileSensorAlertsManager.writeIntoFile ( self.sensorAlertsManager )
        #
        # create the file for calibration manager
        fileSensorCalibrationManager: File = File ( mainDirOutputStructureLogs + "\\android\\SensorCalibration" + self.settings.extensionLogFile , "w" )
        fileSensorCalibrationManager.writeIntoFile ( self.sensorCalibrationManager )
        #
        # create the file for lifecycle manager
        fileLifecycleManager: File = File ( mainDirOutputStructureLogs + "\\android\\Lifecycle" + self.settings.extensionLogFile , "w" )
        fileLifecycleManager.writeIntoFile ( self.lifecycleManager )
        #
        # create the file for sensor number manager
        fileSensorNumberManager: File = File ( mainDirOutputStructureLogs + "\\android\\SensorNumber" + self.settings.extensionLogFile , "w" )
        fileSensorNumberManager.writeIntoFile ( self.sensorNumberManager )
        #
        # create the file for sensor text manager
        fileSensorTextManager: File = File ( mainDirOutputStructureLogs + "\\android\\SensorText" + self.settings.extensionLogFile , "w" )
        fileSensorTextManager.writeIntoFile ( self.sensorTextManager )
        #
        # create the file for ptracer manager
        filePtracerManager: File = File ( mainDirOutputStructureLogs + "\\android\\Ptracer" + self.settings.extensionLogFile , "w" )
        filePtracerManager.writeIntoFile ( self.ptracerManager )
