from manageFile.manageFile import ManageFile
from manageSocket.socketTcp import SocketTcp
from settings.settings import Settings

class PtracerLogs(SocketTcp):
    
    def __init__(self, name: str, host: str, port: int, clients: int, manageFile: ManageFile, settings: Settings):
        super().__init__(name, host, port, clients, manageFile, settings)
    
    # function to restrict the input messages
    def _restrictInputMessages(self, message):
        #
        # boolean variable to check if the input message is valid
        valid = False
        #
        # if input message contains a valid message
        if message.__contains__("------------------ SYSCALL ENTRY START ------------------"):
            # valid message
            valid = True
        elif message.__contains__("------------------ SYSCALL ENTRY STOP ------------------"):
            # valid message
            valid = True
        elif message.__contains__("------------------ SYSCALL EXIT START ------------------"):
            # valid message
            valid = True
        elif message.__contains__("------------------ SYSCALL EXIT STOP ------------------"):
            # valid message
            valid = True
        elif message.__contains__("PID to trace"):
            # valid message
            valid = True
        elif message.__contains__("PID"):
            # valid message
            valid = True
        elif message.__contains__("SPID"):
            # valid message
            valid = True
        elif message.__contains__("Timestamp"):
            # valid message
            valid = True
        elif message.__contains__("Syscall"):
            # valid message
            valid = True
        #
        # return if the message is valid
        return valid
        # if it is a valid message
        if valid:
            #
            # write the input message in the log file
            self._manageFile.writeIntoFile(message)
    
    # function used to
    def _analyzeInputData(self):
        #
        # get the list of single row of ptracer
        actualmessages = self._receivedMessageString.split("\n")
        #
        # for each single row of the received message from the client
        for x in actualmessages:
            #
            # analyze the actual message
            valid = self._restrictInputMessages(x)
            #
            # if it is valid
            if valid:
                #
                # we must analyze it
                pass
            #
            # if it is not valid
            else:
                #
                # we must skip it
                pass
