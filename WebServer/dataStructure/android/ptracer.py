"""
LIST OF PTRACER INFORMATIONS
	Started: 1677055652603636
	Crashed: 1677055652999999
"""

# class used to manage all types of debuggers
class Ptracer :
    
    # constructor to initialize ptracer object
    def __init__ ( self ) -> None :
        #
        # at the beginning not started
        self.startedTimestamp: int = None
        #
        # at the beginning not crashed
        self.crashedTimestamp: int = None
    
    # function used to set started the ptracer process
    def setStartedPtracerProcess ( self , startedTimestamp: int ) -> None :
        #
        # set started the ptracer process
        self.startedTimestamp = startedTimestamp
    
    # function used to set crashed the ptracer process
    def setCrashedPtracerProcess ( self , crashedTimestamp: int ) -> None :
        #
        # set started the ptracer process
        self.crashedTimestamp = crashedTimestamp
    
    # function used to print all info of ptracer process
    def __str__ ( self ) -> str :
        #
        # initialize as empty the output string
        output: str = ""
        #
        # print debug row of all debuggers
        output: str = f"{output}\nLIST OF PTRACER INFORMATIONS\n"
        #
        # if ptracer process is started
        if self.startedTimestamp is not None :
            #
            # print gdb debugger
            output: str = f"{output}\tStarted: {self.startedTimestamp}\n"
        #
        # else if it is not started
        else :
            #
            # print gdb debugger
            output: str = f"{output}\tNot started\n"
        #
        # if ptracer process is crashed
        if self.crashedTimestamp is not None :
            #
            # print gdb debugger
            output: str = f"{output}\tCrashed: {self.crashedTimestamp}\n"
        #
        # else if it is not crashed
        else :
            #
            # print gdb debugger
            output: str = f"{output}\tNot crashed\n"
        #
        #
        # return the output
        return output

if __name__ == "__main__" :
    i = Ptracer ( )
    i.setStartedPtracerProcess ( 1677055652603636 )
    i.setCrashedPtracerProcess ( 1677055652999999 )
    print ( i )
