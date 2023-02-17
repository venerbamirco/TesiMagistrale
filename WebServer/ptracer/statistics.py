"""
Syscall
		Name: name
		Min duration: 275900553699
		Max duration: 345900324742
		Avg duration: 302638601237
		Num measurements: 34
		Good termination: 31 -> return value 0
		Bad termination: 3 -> return value not 0
		List measurements: [275900553699, 345900324742, 302638601237....]
"""

# class used to manage statistics of single instruction
class Statistics :
    
    # constructor to initialize the structure for statistics
    def __init__ ( self , syscall: str ) :
        #
        # save the name of the syscall
        self.syscall: str = syscall
        #
        # minimum duration not defined at this moment
        self.minimum_duration: int = None
        #
        # maximum duration not defined at this moment
        self.maximum_duration: int = None
        #
        # average duration not defined at this moment
        self.average_duration: int = None
        #
        # number of measurements equal to 0
        self.measurements: int = 0
