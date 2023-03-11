# class used for the ptracer manager
from dataStructure.other.file import File
from dataStructure.other.instruction import Instruction
from dataStructure.ptracer.analyses import Analyses
from settings.settings import Settings

class PtracerManager :
    
    # constructor to initialize the ptracer manager
    def __init__ ( self , settings: Settings ) -> None :
        #
        # save the reference for settings
        self.settings: Settings = settings
        #
        # create a list of instruction objects
        self.listInstruction: list [ Instruction ] = list ( )
        #
        # initialize the analyses manager
        self.analyses: Analyses = Analyses ( )
        #
        # variable used to say that we are in the start part or in the finish part of the instruction
        self.startPartInstructionLogs: bool = None
        #
        # instruction to finish it
        self.finishInstruction: Instruction = Instruction ( )
    
    # function used to start a new instruction
    def startNewInstruction ( self ) -> None :
        #
        # input: ------------------ SYSCALL ENTRY START ------------------
        #
        # we are in the start part of the instruction
        self.startPartInstructionLogs = True
        #
        # create a new instruction element
        instruction: Instruction = Instruction ( )
        #
        # append the new element in the list
        self.listInstruction.append ( instruction )
    
    # function used to delete a new instruction
    def deleteNewInstruction ( self ) -> None :
        #
        # get last instruction from the list
        instruction: Instruction = self.listInstruction [ -1 ]
        #
        # delete the new element in the list
        self.listInstruction.remove ( instruction )
    
    # function used to finish actual instruction
    def finishActualInstruction ( self ) -> None :
        #
        # input: ------------------ SYSCALL EXIT START ------------------
        #
        # we are in the end part of the instruction
        self.startPartInstructionLogs = False
    
    # function used to finish a specific instruction
    def finishSpecificInstruction ( self ) -> None :
        #
        # input: ------------------ SYSCALL EXIT STOP ------------------
        #
        # find all instructions with right pid and spid and not terminated
        listInstructions: list [ Instruction ] = [ obj for obj in self.listInstruction
                                                   if obj.pid == self.finishInstruction.pid and
                                                   obj.spid == self.finishInstruction.spid and
                                                   not obj.finishTimestamp ]
        #
        # if there is at least one instruction
        if len ( listInstructions ) > 0 :
            #
            # get the first instruction
            instruction: Instruction = listInstructions [ 0 ]
            #
            # save finish timestamp and return value
            instruction.finishTimestamp = self.finishInstruction.finishTimestamp
            instruction.returnValue = self.finishInstruction.returnValue
            #
            # calculate duration
            instruction.duration: int = instruction.finishTimestamp - instruction.startTimestamp

            print(instruction)
            #
            # add actual measure in analyses tool
            self.analyses.addMeasurement ( instruction.name , instruction.duration )
    
    # function used to set pid
    def setPid ( self , record: str ) -> None :
        #
        # input: PID: 30074
        #
        # split the input string using the space character
        listInputWords: list [ str ] = record.split ( )
        #
        # if len is valid
        if len ( listInputWords ) == 2 :
            #
            # save input pid
            pid: int = int ( listInputWords [ 1 ] )
            #
            # if it is the start part
            if self.startPartInstructionLogs :
                #
                # get last element of the list of instructions
                instruction: Instruction = self.listInstruction [ -1 ]
                #
                # set pid of last instruction of the list
                instruction.pid: int = pid
            #
            # else if it is the final part
            else :
                #
                # set pid on finish instruction
                self.finishInstruction.pid: int = pid
    
    # function used to set spid
    def setSpid ( self , record: str ) -> None :
        #
        # input: SPID: 30074
        #
        # split the input string using the space character
        listInputWords: list [ str ] = record.split ( )
        #
        # save input spid
        spid: int = int ( listInputWords [ 1 ] )
        #
        # if it is the start part
        if self.startPartInstructionLogs :
            #
            # get last element of the list of instructions
            instruction: Instruction = self.listInstruction [ -1 ]
            #
            # set spid of last instruction of the list
            instruction.spid: int = spid
        #
        # else if it is the final part
        else :
            #
            # set spid on finish instruction
            self.finishInstruction.spid: int = spid
    
    # function used to set name
    def setName ( self , record: str ) -> None :
        #
        # input: Syscall = clock_gettime (113)
        #
        # split the input string using the space character
        listInputWords: list [ str ] = record.split ( )
        #
        # save input name
        name: str = listInputWords [ 2 ]
        #
        # get last element of the list of instructions
        instruction: Instruction = self.listInstruction [ -1 ]
        #
        # set name last instruction of the list
        instruction.name: str = name
    
    # function used to set timestamp
    def setTimestamp ( self , record: str ) -> None :
        #
        # input: Timestamp: 1677745254687394
        #
        # split the input string using the space character
        listInputWords: list [ str ] = record.split ( )
        #
        # save input timestamp
        timestamp: int = int ( listInputWords [ 1 ] )
        #
        # if it is the start part
        if self.startPartInstructionLogs :
            #
            # get last element of the list of instructions
            instruction: Instruction = self.listInstruction [ -1 ]
            #
            # set start timestamp of last instruction of the list
            instruction.startTimestamp: int = timestamp
        #
        # else if it is the final part
        else :
            #
            # set finish timestamp on finish instruction
            self.finishInstruction.finishTimestamp: int = timestamp
    
    # function used to set return value
    def setReturnValue ( self , record: str ) -> None :
        #
        # input: Return value: 000000000000000000
        #
        # split the input string using the space character
        listInputWords: list [ str ] = record.split ( )
        #
        # save input return value
        returnValue: int = int ( listInputWords [ 2 ] )
        #
        # set return value on finish instruction
        self.finishInstruction.returnValue: int = returnValue
    
    # function used to set duration
    def setDuration ( self ) -> None :
        #
        # get last element of the list of instructions
        instruction: Instruction = self.listInstruction [ -1 ]
        #
        # set duration of last instruction of the list
        instruction.duration: int = instruction.finishTimestamp - instruction.startTimestamp
    
    #
    #
    #
    #
    #
    #
    #
    
    # function used to save the all ptracer logs
    def savePtracerLogs ( self , mainDirOutputStructureLogs: str ) :
        #
        # create the file for analyses manager
        fileAnalysesManager = File ( mainDirOutputStructureLogs + "\\ptracer\\Analyses" + self.settings.extensionLogFile , "w" )
        fileAnalysesManager.writeIntoFile ( self.analyses )
