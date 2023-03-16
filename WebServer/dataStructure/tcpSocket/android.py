from algorithm.manager.manager import Manager
from dataStructure.other.file import File
from dataStructure.tcpSocket.generalSocket import GeneralSocket
from settings.settings import Settings

# class for the android socket
class Android ( GeneralSocket ) :
    
    # constructor for the android socket class
    def __init__ ( self , name: str , host: str , port: int , clients: int , manageFile: File , settings: Settings , managerAlgorithm: Manager ) :
        #
        # initialize the general socket
        super ( ).__init__ ( name , host , port , clients , manageFile , settings , managerAlgorithm )
    
    # function used to call the single manager of each type of input
    def callManagerActualInput ( self , message ) -> bool :
        #
        # select the right manager for actual input message
        match message :
            #
            # charging
            case s if "UsbChecker" in s :
                #
                # add the charging record
                self.managerAlgorithm.addChargingRecord ( s )
            #
            # developer options
            case s if "DeveloperOptions" in s :
                #
                # add the charging record
                self.managerAlgorithm.addDeveloperOptionsRecord ( s )
            #
            # debuggable application
            case s if "DebuggableApplications" in s :
                #
                # add the charging record
                self.managerAlgorithm.addDebuggableApplicationsRecord ( s )
            #
            # debuggers
            case s if "GnuDebugger_GDB" in s or "JavaDebugWireProtocol_JDWP" in s :
                #
                # add the debugger record
                self.managerAlgorithm.addDebuggerRecord ( s )
            #
            # sensor alerts
            case s if ("Azimuth" in s or "Pitch" in s or "Roll" in s or "Device" in s) and ("ok" in s or "alert" in s or "Device" in s) :
                #
                # add the debugger record
                self.managerAlgorithm.addSensorAlertRecord ( s )
            #
            # calibration
            case s if "Calibration" in s :
                #
                # add the calibration record
                self.managerAlgorithm.addCalibrationRecord ( s )
            #
            # lifecycle
            case s if "AppManagement" in s :
                #
                # add the lifecycle record
                self.managerAlgorithm.addLifecycleRecord ( s )
            #
            # sensor number values
            case s if "Numbers" in s :
                #
                # add the sensor number record
                self.managerAlgorithm.addSensorNumberRecord ( s )
            #
            # sensor text values
            case s if "Texts" in s :
                #
                # add the sensor number record
                self.managerAlgorithm.addSensorTextRecord ( s )
            #
            # other case
            case _ :
                #
                # return that is a not important instruction
                return False
        #
        # return that is a valid string
        return True
