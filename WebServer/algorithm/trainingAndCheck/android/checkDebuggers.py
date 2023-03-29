import time

# class used to check debuggers
class CheckDebuggers :
    
    # constructor
    def __int__ ( self ) :
        #
        # do nothing
        pass
    
    # function used to say that a debugger is found
    def sayDebuggerFound ( self ) :
        #
        # print that a debugger is found
        print ( "################################################################" )
        print ( "Timestamp: " + str ( time.time_ns ( ) ) )
        print ( "A debugger is found" )
