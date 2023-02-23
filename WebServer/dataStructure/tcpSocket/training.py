from dataStructure.other.file import File
from settings.settings import Settings
from dataStructure.tcpSocket.generalSocket import GeneralSocket

# class for the ptracer socket
class Training ( GeneralSocket ) :
    
    # constructor for the android socket class
    def __init__ ( self , name: str , host: str , port: int , clients: int , manageFile: File , settings: Settings ) :
        #
        # initialize the general socket
        super ( ).__init__ ( name , host , port , clients , manageFile , settings )