from algorithm.manager import Manager
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
    
    # temp function
    def f1 ( self ) :
        pass
    
    def f2 ( message: str ) :
        pass
    
    # function to restrict the input messages
    def restrictInputMessages ( self , message ) :
        #
        # select the right operations for actual input message
        match message :
            #
            # ptracer start initial part
            case "------------------ SYSCALL ENTRY START ------------------" :
                #
                # start operations
                self.f1 ( )
            #
            # ptracer start final part
            case "------------------ SYSCALL ENTRY STOP ------------------" :
                #
                # start operations
                self.f1 ( )
            #
            # ptracer finish initial part
            case "------------------ SYSCALL EXIT START ------------------" :
                #
                # start operations
                self.f1 ( )
            #
            # ptracer finish final part
            case "------------------ SYSCALL EXIT STOP ------------------" :
                #
                # start operations
                self.f1 ( )
            #
            # initial pid to trace
            case s if "PID to trace" in s :
                #
                # start operations
                self.f1 ( )
            #
            # pid of actual ptracer
            case s if "PID" in s :
                #
                # start operations
                self.f1 ( )
            #
            # spid of actual ptracer
            case s if "SPID" in s :
                #
                # start operations
                self.f1 ( )
            #
            # timestamp of actual start or finish ptracer
            case s if "Timestamp" in s :
                #
                # start operations
                self.f1 ( )
            #
            # name of ptracer
            case s if "Syscall" in s :
                #
                # start operations
                self.f1 ( )
            #
            # return value of ptracer
            case s if "Return value" in s :
                #
                # start operations
                self.f1 ( )
            #
            # other case
            case _ :
                #
                # start operations
                self.f1 ( )
                #
                # return that is a not important instruction
                return False
        #
        # return that is an important instruction
        return True
    
    # function used to
    def analyzeInputData ( self , receivedMessageString ) :
        #
        # get the list of single row of ptracer
        actualmessages = receivedMessageString.split ( "\n" )
        #
        # for each single row of the received message from the client
        for x in actualmessages :
            #
            # analyze the actual message
            valid = self.restrictInputMessages ( x )
            #
            # if it is valid
            if valid :
                #
                # write the actual message in the log other
                self.manageFile.writeIntoFile ( x )
            #
            # if it is not valid
            else :
                #
                # we must skip it
                self.manageFile.writeIntoFile ( x )
