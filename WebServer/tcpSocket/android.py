from file.file import File
from settings.settings import Settings
from tcpSocket.generalSocket import GeneralSocket

# class for the android socket
class Android ( GeneralSocket ) :
    
    # constructor for the android socket class
    def __init__ ( self , name: str , host: str , port: int , clients: int , manageFile: File , settings: Settings ) :
        #
        # initialize the general socket
        super ( ).__init__ ( name , host , port , clients , manageFile , settings )
