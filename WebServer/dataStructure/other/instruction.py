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
