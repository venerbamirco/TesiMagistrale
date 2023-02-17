"""
Syscall
		Name: name
		Pid: pid
		Spid: spid
		Status: Executing
		Start: 1676364852615690

Syscall
		Name: name
		Pid: pid
		Spid: spid
		Status: Finished
		Start: 1676364852615690
		Finish: 1676640753169389
		Duration: 275900553699
		Return Value: 0
"""

# class to create the structure for the single instruction
class Instruction :
    
    # constructor to initialize the object for the instruction
    def __init__ ( self , syscall: str , pid: int , spid: int , start_timestamp: int ) -> None :
        #
        # save the name of the syscall
        self.syscall: str = syscall
        #
        # save the pid
        self.pid: int = pid
        #
        # save the spid
        self.spid: int = spid
        #
        # save the start_timestamp
        self.start_timestamp: int = start_timestamp
        #
        # finish timestamp not defined at this moment
        self.finish_timestamp: int = None
        #
        # save the return value not defined at this moment
        self.return_value: int = None
        #
        # variable used to see if the actual instruction is finished
        self.finished: bool = False
    
    # function used to print an instruction object
    def __str__ ( self ) :
        #
        # variable to store the output
        output: str = "Syscall\n"
        #
        # add name of syscall
        output: str = f"{output}\t\tName: {self.syscall}\n"
        #
        # add pid of syscall
        output: str = f"{output}\t\tPid: {self.pid}\n"
        #
        # add spid of syscall
        output: str = f"{output}\t\tSpid: {self.spid}\n"
        #
        # if the syscall in not finished
        if not self.finished :
            #
            # add status of syscall
            output: str = f"{output}\t\tStatus: Executing\n"
            #
            # add start timestamp of syscall
            output: str = f"{output}\t\tStart: {self.start_timestamp}\n"
        #
        # else if the syscall is finished
        else :
            #
            # add status of syscall
            output: str = f"{output}\t\tStatus: Finished\n"
            #
            # add start timestamp of syscall
            output: str = f"{output}\t\tStart: {self.start_timestamp}\n"
            #
            # add finish timestamp of syscall
            output: str = f"{output}\t\tFinish: {self.finish_timestamp}\n"
            #
            # add duration of syscall
            output: str = f"{output}\t\tDuration: {self.get_duration_instruction ( )}\n"
            #
            # add return value of syscall
            output: str = f"{output}\t\tReturn Value: {self.return_value}\n"
        #
        # return the output
        return output
    
    def set_finish_instruction ( self , return_value: int , finish_timestamp: int ) -> None :
        #
        # the instruction is finished
        self.finished: bool = True
        #
        # save the return value
        self.return_value: int = return_value
        #
        # save the finish timestamp
        self.finish_timestamp: int = finish_timestamp
    
    # function used to get the duration of actual instruction
    def get_duration_instruction ( self ) -> int :
        #
        # if the instruction is finished
        if self.finished :
            #
            # return the duration in milliseconds
            return self.finish_timestamp - self.start_timestamp
        #
        # else if the instruction is not finished
        else :
            #
            # return a zero duration
            return 0

"""if __name__ == "__main__" :
    i = Instruction ( "name" , "pid" , "spid" , 1676364852615690 )
    print ( i )
    i.set_finish_instruction ( 0 , 1676640753169389 )
    print ( i )"""
