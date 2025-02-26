from algorithm.dataStructure.other.file import File
from algorithm.manager.manager import Manager
from algorithm.tcpSocket.generalSocket import GeneralSocket

# class for the ptracer socket
class Ptracer ( GeneralSocket ) :
    
    # constructor for the android socket class
    def __init__ ( self , name: str , host: str , port: int , clients: int , manageFile: File , managerAlgorithm: Manager ) :
        #
        # initialize the general socket
        super ( ).__init__ ( name , host , port , clients , manageFile , managerAlgorithm )
        #
        # variables to manage if we have found all types of input details
        self.pid = None
        self.spid = None
        self.timestamp = None
        self.syscall = None
        self.returnValue = None
    
    # function used to call the single manager of each type of input
    def callManagerActualInput ( self , message ) -> None :
        #
        # select the right manager for actual input message
        match message :
            #
            # pid to trace
            case s if s.startswith ( "PID to trace:" ) :
                #
                # do nothing
                pass
            #
            # start a new instruction
            case s if "SYSCALL" in s and "ENTRY" in s and "START" in s :
                #
                # variables to manage if we have found all types of input details
                self.pid = False
                self.spid = False
                self.timestamp = False
                self.syscall = False
                #
                # start a new instruction
                self.managerAlgorithm.startNewInstruction ( )
                pass
            #
            # end of start a new instruction
            case s if "SYSCALL" in s and "ENTRY" in s and "STOP" in s :
                #
                # if we not found all necessary data
                if not self.pid or not self.spid or not self.timestamp or not self.syscall :
                    #
                    # delete the last instruction
                    self.managerAlgorithm.deleteNewInstruction ( )
                #
                # else if we found all necessary data
                else :
                    #
                    #
                    self.managerAlgorithm.setFirstPartInstruction ( )
            #
            # finish a new instruction
            case s if "SYSCALL" in s and "EXIT" in s and "START" in s :
                #
                # variables to manage if we have found all types of input details
                self.pid = False
                self.spid = False
                self.timestamp = False
                self.returnValue = False
                #
                # we are in the end part of the instruction
                self.managerAlgorithm.finishActualInstruction ( )
            #
            # end of finish a new instruction
            case s if "SYSCALL" in s and "EXIT" in s and "STOP" in s :
                #
                # if we found all necessary data
                if self.pid and self.spid and self.timestamp and self.returnValue :
                    #
                    # finish specific instruction
                    self.managerAlgorithm.finishSpecificInstruction ( )
            #
            # pid
            case s if s.startswith ( "PID" ) :
                #
                # pid found
                self.pid = True
                #
                # set pid
                self.managerAlgorithm.setPid ( s )
            #
            # spid
            case s if s.startswith ( "SPID" ) :
                #
                # spid found
                self.spid = True
                #
                # set spid
                self.managerAlgorithm.setSpid ( s )
            #
            # timestamp
            case s if s.startswith ( "Timestamp" ) :
                #
                # timestamp found
                self.timestamp = True
                #
                # set timestamp
                self.managerAlgorithm.setTimestamp ( s )
            #
            # syscall
            case s if s.startswith ( "Syscall" ) :
                #
                # syscall found
                self.syscall = True
                #
                # set instruction
                self.managerAlgorithm.setName ( s )
            #
            # return value
            case s if s.startswith ( "Return" ) :
                #
                # return value found
                self.returnValue = True
                #
                # set return value
                self.managerAlgorithm.setReturnValue ( s )
            #
            # other case
            # case _ :
            case s if "Notification" in s or "Authorized" in s or "Parameters" in s or "PC" in s or "unwinding" in s or "Follow" in s or "Tracee" in s or "Authorizer" in s or "Jumped" in s :
                return False
            case _ :
                #
                # do nothing for the moment
                pass
    
    # function used to check if it is a valid string for actual type of socket
    def checkStringForActualSocket ( self , string: str ) -> bool :
        #
        # if it is a valid string
        if string != "" and \
                (
                        (string.startswith ( "------------------ SYSCALL" ) and string.endswith ( "------------------" )) or
                        string.startswith ( "PID:" ) or
                        string.startswith ( "SPID:" ) or
                        string.startswith ( "Timestamp:" ) or
                        string.startswith ( "Syscall" ) or
                        string.startswith ( "Return" )
                ) :
            #
            # return that it is a valid string
            return True
        #
        # if it is not a valid string
        else :
            #
            # return that it is not a valid string
            return False
