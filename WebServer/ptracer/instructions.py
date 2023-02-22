"""
LIST OF ALL NOT TERMINATED SYSCALL
	Syscall
		Name: name1
		Pid: 1
		Spid: 1
		Status: Executing
		Start: 1676364852615690

LIST OF ALL TERMINATED SYSCALL
	Syscall
		Name: name2
		Pid: 2
		Spid: 2
		Status: Finished
		Start: 2676364852615690
		Finish: 4715285019562354
		Duration: 2038920166946664
		Return Value: 0
"""

# class to manage the structure of a single instruction
class Instruction :
    
    # constructor to initialize an instruction
    def __init__ ( self , syscall: str , pid: int , spid: int , startTimestamp: int ) -> None :
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
        # save the startTimestamp
        self.startTimestamp: int = startTimestamp
        #
        # finish timestamp not defined at this moment
        self.finishTimestamp: int = None
        #
        # save the return value not defined at this moment
        self.returnValue: int = None
        #
        # variable used to see if the actual instruction is finished
        self.finished: bool = False
    
    # function used to set the terminated status in the actual instruction
    def finishInstruction ( self , returnValue: int , finishTimestamp: int ) -> None :
        #
        # the instruction is finished
        self.finished: bool = True
        #
        # save the return value
        self.returnValue: int = returnValue
        #
        # save the finish timestamp
        self.finishTimestamp: int = finishTimestamp
    
    # function used to get the duration of actual instruction
    def getDuration ( self ) -> int :
        #
        # if the instruction is finished
        if self.finished :
            #
            # return the duration in milliseconds
            return self.finishTimestamp - self.startTimestamp
        #
        # else if the instruction is not finished
        else :
            #
            # return a zero duration
            return 0
    
    # function used to print an instruction object
    def __str__ ( self ) -> str :
        #
        # variable to store the output
        output: str = "\tSyscall\n"
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
            output: str = f"{output}\t\tStart: {self.startTimestamp}\n"
        #
        # else if the syscall is finished
        else :
            #
            # add status of syscall
            output: str = f"{output}\t\tStatus: Finished\n"
            #
            # add start timestamp of syscall
            output: str = f"{output}\t\tStart: {self.startTimestamp}\n"
            #
            # add finish timestamp of syscall
            output: str = f"{output}\t\tFinish: {self.finishTimestamp}\n"
            #
            # add duration of syscall
            output: str = f"{output}\t\tDuration: {self.getDuration ( )}\n"
            #
            # add return value of syscall
            output: str = f"{output}\t\tReturn Value: {self.returnValue}\n"
        #
        # return the output
        return output

# class to create the structure for the list of instructions
class Instructions :
    
    # constructor to initialize the list of instructions
    def __init__ ( self ) -> None :
        #
        # create the list for all instructions both terminated and also not terminated
        self.listAllInstructions: list [ Instruction ] = list ( )
        #
        # create the list for not terminated instructions
        self.listNotTerminatedInstructions: list [ Instruction ] = list ( )
    
    # function used to add a new instruction in the list
    def addInstruction ( self , syscall: str , pid: int , spid: int , startTimestamp: int ) :
        #
        # create the instruction
        instruction: Instruction = Instruction ( syscall , pid , spid , startTimestamp )
        #
        # append the instruction in the list of all instructions
        self.listAllInstructions.append ( instruction )
        #
        # append the instruction in the list of not terminated instructions
        self.listNotTerminatedInstructions.append ( instruction )
    
    # function used to terminate instruction
    def finishInstruction ( self , pid: int , spid: int , returnValue: int , finishTimestamp: int ) :
        #
        # for each instruction in the list of not terminated instructions
        for instruction in self.listNotTerminatedInstructions :
            #
            # if it is the right instruction looking pid and spid codes
            if instruction.pid == pid and instruction.spid == spid :
                #
                # terminated the right instruction in the list of all instructions
                self.listAllInstructions [ self.listAllInstructions.index ( instruction ) ].finishInstruction ( returnValue , finishTimestamp )
                #
                # exit from the loop
                break
    
    # function used to print an instruction object
    def __str__ ( self ) -> str :
        #
        # initialize as empty the output string
        output: str = ""
        #
        # print debug row of all not terminated instructions
        output: str = f"{output}\nLIST OF ALL NOT TERMINATED SYSCALL\n"
        #
        # for each not terminated instruction
        for instruction in self.listAllInstructions :
            #
            # if the actual instruction is not terminated
            if not instruction.finished :
                #
                # print the actual not terminated instruction
                output: str = f"{output}{instruction}"
        #
        # print debug row of all terminated instructions
        output: str = f"{output}\nLIST OF ALL TERMINATED SYSCALL\n"
        #
        # for each not terminated instruction
        for instruction in self.listAllInstructions :
            #
            # if the actual instruction is terminated
            if instruction.finished :
                #
                # print the actual terminated instruction
                output: str = f"{output}{instruction}"
        #
        # return the output
        return output

if __name__ == "__main__" :
    i = Instructions ( )
    i.addInstruction ( "name1" , 1 , 1 , 1676364852615690 )
    i.addInstruction ( "name2" , 2 , 2 , 2676364852615690 )
    i.finishInstruction(2, 2, 0, 4715285019562354)
    print ( i )
