"""
LIST OF ALL DEBUGGERS

	Debugger
		Name: GDB debugger
		Found: True
		Timestamp: 1677055652603636

	Debugger
		Name: JDWP debugger
		Found: False
"""

import time

from algorithm.settings.settings import Settings

# class used to manage the debugger
class Debugger :
    
    # constructor to initialize the debugger
    def __init__ ( self , name: str ) -> None :
        #
        # name of the debugger
        self.name: str = name
        #
        # debugger not found at the moment
        self.found: bool = False
        #
        # timestamp in which is found
        self.foundTimestamp: int = None
    
    # function used to set found a debugger
    def setDebuggerFound ( self , timestamp: int ) -> None :
        #
        # debugger is found
        self.found: bool = True
        #
        # timestamp in which is found
        self.foundTimestamp: int = timestamp
    
    # function used to print a debugger object
    def __str__ ( self ) -> str :
        #
        # variable to store the output
        output: str = "\n\tDebugger\n"
        #
        # add name of debugger
        output: str = f"{output}\t\tName: {self.name}\n"
        #
        # add status of debugger
        output: str = f"{output}\t\tFound: {self.found}\n"
        #
        # if the debugger is found
        if self.found :
            #
            # add the timestamp in which is found
            output: str = f"{output}\t\tTimestamp: {self.foundTimestamp}\n"
        #
        # return the output
        return output

# class used to manage all types of debuggers
class Debuggers :
    
    # constructor to initialize all possible debuggers
    def __init__ ( self ) -> None :
        #
        # create the gdb debugger
        self.gdbDebugger: Debugger = Debugger ( "GDB debugger" )
        #
        # create the jdwp debugger
        self.jdwpDebugger: Debugger = Debugger ( "JDWP debugger" )
    
    # function used to set found the gdb debugger
    def setFoundGdbDebugger ( self , foundTimestamp: int ) -> None :
        #
        # set found the gdb debugger
        self.gdbDebugger.setDebuggerFound ( foundTimestamp )
    
    # function used to set found the jdwp debugger
    def setFoundJdwpDebugger ( self , foundTimestamp: int ) -> None :
        #
        # set found the jdwp debugger
        self.jdwpDebugger.setDebuggerFound ( foundTimestamp )
    
    # function used to print all debuggers
    def __str__ ( self ) -> str :
        #
        # initialize as empty the output string
        output: str = ""
        #
        # print debug row of all debuggers
        output: str = f"{output}\nLIST OF ALL DEBUGGERS\n"
        #
        # print gdb debugger
        output: str = f"{output}{self.gdbDebugger}"
        #
        # print jdwp debugger
        output: str = f"{output}{self.jdwpDebugger}"
        #
        # return the output
        return output
    
    # function used to say that a debugger is found
    def sayDebuggerFound ( self ) :
        #
        # if it is enabled the flag to see if a debugger is found
        if Settings.debuggerFound :
            #
            # print that a debugger is found
            print ( "################################################################" )
            print ( "Timestamp: " + str ( time.time_ns ( ) ) )
            print ( "A jdwp debugger is found" )

if __name__ == "__main__" :
    i = Debuggers ( )
    i.setFoundGdbDebugger ( 1677055652603636 )
    print ( i )
