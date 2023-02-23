from dataStructure.other.file import File
from settings.settings import Settings
from dataStructure.tcpSocket.generalSocket import GeneralSocket

# class for the android socket
class Android ( GeneralSocket ) :
    
    # constructor for the android socket class
    def __init__ ( self , name: str , host: str , port: int , clients: int , manageFile: File , settings: Settings ) :
        #
        # initialize the general socket
        super ( ).__init__ ( name , host , port , clients , manageFile , settings )
    
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
            valid = True
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
