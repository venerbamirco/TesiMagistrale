from manageFile.manageFile import ManageFile
from manageSocket.socketTcp import SocketTcp
from settings.settings import Settings

class PtracerLogs(SocketTcp):
    
    def __init__(self, name: str, host: str, port: int, clients: int, manageFile: ManageFile, settings: Settings):
        super().__init__(name, host, port, clients, manageFile, settings)
    
    def _analyzeInputData(self):
        pass
