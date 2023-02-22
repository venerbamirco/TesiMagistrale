# class used to manage the single record of development options
class DeveloperOptionsRecord :
    
    # constructor to initialize the single record of development options
    def __init__ ( self , developerOptionsEnabled: bool , androidDebugBridgeEnabled: bool ) -> None :
        #
        # save if developer options are enabled
        self.developerOptionsEnabled: bool = developerOptionsEnabled
        #
        # save if the android debug bridge is enabled
        self.androidDebugBridgeEnabled: bool = androidDebugBridgeEnabled
        #
        # save the start timestamp
        self.startTimestamp: int = None
        #
        # finish timestamp not defined at this moment
        self.finishTimestamp: int = None
    
    # function used to get the duration of actual instruction
    def get_duration_instruction ( self ) -> int :
        #
        # if it is possible to calculate the duration
        if self.finishTimestamp :
            #
            # return the duration in milliseconds
            return self.finishTimestamp - self.startTimestamp
        #
        # else if the instruction is not finished
        else :
            #
            # return a zero duration
            return 0

# class used to manage developer options and adb
class DeveloperOptions :
    
    # constructor to initialize the object for the development options object
    def __init__ ( self ) :
        pass
