# class used to represent an instruction object
class Instruction :
    
    # constructor to initialize the instruction object
    def __init__ ( self ) -> None :
        #
        # set pid
        self.pid: int = None
        #
        # set spid
        self.spid: int = None
        #
        # set name
        self.name: str = None
        #
        # set start timestamp
        self.startTimestamp: int = None
        #
        # set finish timestamp
        self.finishTimestamp: int = None
        #
        # set duration
        self.duration: int = None
        #
        # set return value
        self.returnValue: int = None
    
    # function used to get the duration of actual instruction
    def getDuration ( self ) -> int :
        #
        # if it is possible to calculate the duration
        if self.finishTimestamp :
            #
            # if negative duration
            if self.finishTimestamp - self.startTimestamp < 0 :
                #
                # return positive duration
                return self.startTimestamp - self.finishTimestamp
            #
            # return the duration in milliseconds
            return self.finishTimestamp - self.startTimestamp
        #
        # else if the range is not finished
        else :
            #
            # return a zero duration
            return 0
    
    def __repr__ ( self ) :
        return "pid " + str ( self.pid ) + " spid " + str ( self.spid ) + " name " + self.name + " start " + str ( self.startTimestamp ) + " finish " + str ( self.finishTimestamp ) + " duration " + str ( self.duration )
