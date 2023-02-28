from algorithm.manager import Manager
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
            # other case
            case _ :
                #
                # return that is a not important instruction
                return False
        #
        # return that is a valid string
        return True
    
    # function used to analyze each receive message
    def analyzeInputData ( self , receivedMessageString ) :
        #
        # get the list of single row of ptracer
        actualMessages = receivedMessageString.split ( "\n" )
        #
        # for each single row of the received message from the client
        for message in actualMessages :
            #
            # call the relative manager if it is a valid message
            valid = self.callManagerActualInput ( message )
            #
            # if it is valid
            if valid :
                #
                # write the actual message in the log
                self.manageFile.writeIntoFile ( message )
            #
            # if it is not valid
            else :
                #
                # we must skip it
                # pass
                self.manageFile.writeIntoFile ( message )
