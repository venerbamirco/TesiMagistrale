import time

from algorithm.manager.manager import Manager
from dataStructure.other.file import File
from dataStructure.tcpSocket.generalSocket import GeneralSocket
from settings.settings import Settings

# class for the ptracer socket
class Ptracer ( GeneralSocket ) :
    
    # constructor for the android socket class
    def __init__ ( self , name: str , host: str , port: int , clients: int , manageFile: File , settings: Settings , managerAlgorithm: Manager ) :
        #
        # initialize the general socket
        super ( ).__init__ ( name , host , port , clients , manageFile , settings , managerAlgorithm )
        #
        # variables to manage if we have found all types of input details
        self.pid = None
        self.spid = None
        self.timestamp = None
        self.syscall = None
        self.returnValue = None
        #
        # initial timestamp to check other timestamp
        self.checkTimestamp = time.time_ns ( ) / 1000
    
    # function used to call the single manager of each type of input
    def callManagerActualInput ( self , message ) -> bool :
        #
        # select the right manager for actual input message
        match message :
            #
            # pid to trace
            case s if s.startswith ( "PID to trace:" ) and len ( s.split ( ) ) == 4 and s.split ( ) [ 3 ].isnumeric ( ) :
                #
                # do nothing
                pass
            #
            # start a new instruction
            case s if s == "------------------ SYSCALL ENTRY START ------------------" :
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
            case s if s == "------------------ SYSCALL ENTRY STOP ------------------" :
                #
                # if we not found all necessary data
                if not self.pid or not self.spid or not self.timestamp or not self.syscall :
                    #
                    # delete the last instruction
                    self.managerAlgorithm.deleteNewInstruction ( )
            #
            # finish a new instruction
            case s if s == "------------------ SYSCALL EXIT START ------------------" :
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
            case s if s == "------------------ SYSCALL EXIT STOP ------------------" :
                #
                # if we found all necessary data
                if self.pid and self.spid and self.timestamp and self.returnValue :
                    #
                    # finish specific instruction
                    self.managerAlgorithm.finishSpecificInstruction ( )
            #
            # pid
            case s if s.startswith ( "PID:" ) and len ( s.split ( ) ) == 2 and s.split ( ) [ 1 ].isnumeric ( ) :
                #
                # pid found
                self.pid = True
                #
                # set pid
                self.managerAlgorithm.setPid ( s )
            #
            # spid
            case s if s.startswith ( "SPID:" ) and len ( s.split ( ) ) == 2 and s.split ( ) [ 1 ].isnumeric ( ) :
                #
                # spid found
                self.spid = True
                #
                # set spid
                self.managerAlgorithm.setSpid ( s )
            #
            # timestamp
            case s if s.startswith ( "Timestamp:" ) and len ( s.split ( ) ) == 2 and len ( s.split ( ) [ 1 ] ) and s.split ( ) [ 1 ].isnumeric ( ) \
                      and self.checkTimestamp < int ( s.split ( ) [ 1 ] ) :
                #
                # timestamp found
                self.timestamp = True
                #
                # set timestamp
                self.managerAlgorithm.setTimestamp ( s )
            #
            # syscall
            case s if s.startswith ( "Syscall =" ) and len ( s.split ( ) ) == 4 and s.split ( ) [ 3 ].startswith ( "(" ) \
                      and s.split ( ) [ 3 ].endswith ( ")" ) and s.split ( ) [ 3 ] [ 1 :-1 ].isnumeric ( ) :
                #
                # syscall found
                self.syscall = True
                #
                # set instruction
                self.managerAlgorithm.setName ( s )
            #
            # return value
            case s if s.startswith ( "Return value:" ) and len ( s.split ( ) ) == 3 and s.split ( ) [ 2 ].isnumeric ( ) :
                #
                # return value found
                self.returnValue = True
                #
                # set return value
                self.managerAlgorithm.setReturnValue ( s )
            #
            # other case
            case _ :
                #
                # return that is a not important instruction
                return False
        #
        # return that is a valid string
        return True
