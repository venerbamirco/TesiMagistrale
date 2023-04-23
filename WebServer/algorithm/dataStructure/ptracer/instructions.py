"""
LIST OF ALL NOT TERMINATED INSTRUCTIONS

	Instruction
		Name: name1
		Pid: 1
		Spid: 1
		Status: Executing
		Start: 1676364852615690

LIST OF ALL TERMINATED INSTRUCTIONS

	Instruction
		Name: name2
		Pid: 2
		Spid: 2
		Status: Finished
		Start: 2676364852615690
		Finish: 4715285019562354
		Duration: 2038920166946664
		Return Value: 0
"""
from algorithm.dataStructure.ptracer.analyses import Analyses

# class to manage the structure of a single instruction
class InstructionRecord :
    
    # constructor to initialize an instruction
    def __init__ ( self , name: str , pid: int , spid: int , startTimestamp: int ) -> None :
        #
        # save the name of the instruction
        self.name: str = name
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
        output: str = "\n\tInstruction\n"
        #
        # add name
        output: str = f"{output}\t\tName: {self.name}\n"
        #
        # add pid
        output: str = f"{output}\t\tPid: {self.pid}\n"
        #
        # add spid
        output: str = f"{output}\t\tSpid: {self.spid}\n"
        #
        # if the instruction is not finished
        if not self.finished :
            #
            # add status
            output: str = f"{output}\t\tStatus: Executing\n"
            #
            # add start timestamp
            output: str = f"{output}\t\tStart: {self.startTimestamp}\n"
        #
        # else if the instruction is finished
        else :
            #
            # add status
            output: str = f"{output}\t\tStatus: Finished\n"
            #
            # add start timestamp
            output: str = f"{output}\t\tStart: {self.startTimestamp}\n"
            #
            # add finish timestamp
            output: str = f"{output}\t\tFinish: {self.finishTimestamp}\n"
            #
            # add duration
            output: str = f"{output}\t\tDuration: {self.getDuration ( )}\n"
            #
            # add return value
            output: str = f"{output}\t\tReturn Value: {self.returnValue}\n"
        #
        # return the output
        return output

# class to create the structure for the list of instructions
class Instructions :
    
    # constructor to initialize the list of instructions
    def __init__ ( self , analyses: Analyses ) -> None :
        #
        # save the reference for analyses
        self.analyses: Analyses = analyses
        #
        # create the list for all instructions both terminated and also not terminated
        self.listAllInstructions: list [ InstructionRecord ] = list ( )
    
    # function used to add a new instruction in the list
    def addInstruction ( self , name: str , pid: int , spid: int , startTimestamp: int ) -> None :
        #
        # create the instruction
        instruction: InstructionRecord = InstructionRecord ( name , pid , spid , startTimestamp )
        #
        # append the instruction in the list of all instructions
        self.listAllInstructions.append ( instruction )
    
    # function used to terminate instruction
    def finishInstruction ( self , pid: int , spid: int , returnValue: int , finishTimestamp: int ) -> (str , int) :
        #
        # obtain the list of not terminated instructions
        listInstructions: list [ InstructionRecord ] = [ obj for obj in self.listAllInstructions if obj.pid == pid and
                                                         obj.spid == spid and obj.finishTimestamp is None ]
        #
        # if there is at least one instruction in the list
        if len ( listInstructions ) > 0 :
            #
            # obtain the right instruction
            instruction: InstructionRecord = listInstructions [ -1 ]
            #
            # terminated the right instruction in the list of all instructions
            instruction.finishInstruction ( returnValue , finishTimestamp )
            #
            # add measure of actual instruction
            self.analyses.addMeasurement ( instruction.name , instruction.getDuration ( ) )
            #
            # return the name of the instruction
            return instruction.name , instruction.getDuration ( )
        #
        # else if there are not instructions
        else :
            #
            # return None
            return None , None
    
    # function used to get a specific instruction
    def getInstruction ( self , name: str , pid: int , spid: int , startTimestamp: int ) -> InstructionRecord :
        #
        # obtain the right instruction
        instruction: InstructionRecord = [ obj for obj in self.listAllInstructions
                                           if obj.name == name and
                                           obj.pid == pid and
                                           obj.spid == spid and
                                           obj.startTimestamp == startTimestamp ] [ 0 ]
        #
        # return the specific instruction
        return instruction
    
    # function used to print all instructions
    def __str__ ( self ) -> str :
        #
        # initialize as empty the output string
        output: str = ""
        #
        # print debug row of all terminated instructions
        output: str = f"{output}\nLIST OF ALL TERMINATED INSTRUCTIONS\n"
        #
        # for each terminated instruction
        for instruction in [ obj for obj in self.listAllInstructions if obj.finished ] :
            #
            # print the actual terminated instruction
            output: str = f"{output}{instruction}"
        #
        # print debug row of all not terminated instructions
        output: str = f"{output}\nLIST OF ALL NOT TERMINATED INSTRUCTIONS\n"
        #
        # for each not terminated instruction
        for instruction in [ obj for obj in self.listAllInstructions if not obj.finished ] :
            #
            # print the actual not terminated instruction
            output: str = f"{output}{instruction}"
        #
        # return the output
        return output

if __name__ == "__main__" :
    i = Instructions ( )
    i.addInstruction ( "name1" , 1 , 1 , 1676364852615690 )
    i.addInstruction ( "name2" , 2 , 2 , 2676364852615690 )
    i.finishInstruction ( 2 , 2 , 0 , 4715285019562354 )
    print ( i )
