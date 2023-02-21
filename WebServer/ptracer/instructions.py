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
			Name: name1
			Pid: 1
			Spid: 1
			Status: Finished
			Start: 1676364852615690
			Finish: 3715285019562354
			Duration: 2038920166946664
			Return Value: 0
"""

# class to manage the structure of a single instruction
class Instruction :
    
    # constructor to initialize an instruction
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
    
    # function used to set the terminated status in the actual instruction
    def finish_instruction ( self , return_value: int , finish_timestamp: int ) -> None :
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
    
    # function used to print an instruction object
    def __str__ ( self ) -> str :
        #
        # variable to store the output
        output: str = "\tSyscall\n"
        #
        # add name of syscall
        output: str = f"{output}\t\t\tName: {self.syscall}\n"
        #
        # add pid of syscall
        output: str = f"{output}\t\t\tPid: {self.pid}\n"
        #
        # add spid of syscall
        output: str = f"{output}\t\t\tSpid: {self.spid}\n"
        #
        # if the syscall in not finished
        if not self.finished :
            #
            # add status of syscall
            output: str = f"{output}\t\t\tStatus: Executing\n"
            #
            # add start timestamp of syscall
            output: str = f"{output}\t\t\tStart: {self.start_timestamp}\n"
        #
        # else if the syscall is finished
        else :
            #
            # add status of syscall
            output: str = f"{output}\t\t\tStatus: Finished\n"
            #
            # add start timestamp of syscall
            output: str = f"{output}\t\t\tStart: {self.start_timestamp}\n"
            #
            # add finish timestamp of syscall
            output: str = f"{output}\t\t\tFinish: {self.finish_timestamp}\n"
            #
            # add duration of syscall
            output: str = f"{output}\t\t\tDuration: {self.get_duration_instruction ( )}\n"
            #
            # add return value of syscall
            output: str = f"{output}\t\t\tReturn Value: {self.return_value}\n"
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
    def addInstructionInTheList ( self , syscall: str , pid: int , spid: int , start_timestamp: int ) :
        #
        # create the instruction
        instruction: Instruction = Instruction ( syscall , pid , spid , start_timestamp )
        #
        # append the instruction in the list of all instructions
        self.listAllInstructions.append ( instruction )
        #
        # append the instruction in the list of not terminated instructions
        self.listNotTerminatedInstructions.append ( instruction )
    
    # function used to terminate instruction
    def terminateInstruction ( self , pid: int , spid: int , return_value: int , finish_timestamp: int ) :
        #
        # for each instruction in the list of not terminated instructions
        for instruction in self.listNotTerminatedInstructions :
            #
            # if it is the right instruction looking pid and spid codes
            if instruction.pid == pid and instruction.spid == spid :
                #
                # terminated the right instruction in the list of all instructions
                self.listAllInstructions [ self.listAllInstructions.index ( instruction ) ].finish_instruction ( return_value , finish_timestamp )
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

"""if __name__ == "__main__" :
    i = Instructions ( )
    i.addInstructionInTheList ( "name1" , 1 , 1 , 1676364852615690 )
    i.addInstructionInTheList ( "name2" , 2 , 2 , 2676364852615690 )
    print ( i )
    i.terminateInstruction(1, 1, 0, 3715285019562354)
    i.terminateInstruction(2, 2, 0, 4715285019562354)
    print ( i )"""
