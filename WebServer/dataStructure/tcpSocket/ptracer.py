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
    
    # function used to call the single manager of each type of input
    def callManagerActualInput ( self , message ) -> bool :
        #
        # select the right manager for actual input message
        match message :
            #
            # pid to trace
            case s if "PID to trace" in s :
                #
                # do nothing
                pass
            #
            # start a new instruction
            case s if "SYSCALL ENTRY START" in s :
                #
                # start a new instruction
                self.managerAlgorithm.startNewInstruction ( )
                pass
            #
            # end of start a new instruction
            case s if "SYSCALL ENTRY STOP" in s :
                #
                # do nothing
                pass
            #
            # finish a new instruction
            case s if "SYSCALL EXIT START" in s :
                #
                # finish actual instruction
                self.managerAlgorithm.finishActualInstruction ( )
            #
            # end of finish a new instruction
            case s if "SYSCALL EXIT STOP" in s :
                #
                # do nothing
                pass
            #
            # pid
            case s if "PID:" in s :
                #
                # set pid
                self.managerAlgorithm.setPid (s )
            #
            # spid
            case s if "SPID:" in s :
                #
                # set spid
                self.managerAlgorithm.setSpid (s )
            #
            # timestamp
            case s if "Timestamp:" in s :
                #
                # set timestamp
                self.managerAlgorithm.setTimestamp (s )
            #
            # syscall
            case s if "Syscall =" in s :
                #
                # set instruction
                self.managerAlgorithm.setName ( )
            #
            # return value
            case s if "Return value:" in s :
                #
                #
                pass
            #
            # other case
            case _ :
                #
                # return that is a not important instruction
                return False
        #
        # return that is a valid string
        return True
