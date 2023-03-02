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
        self.analyses = Analyses ( )
        #
        # variable used to say that we are in the start part or in the finish part of the instruction
        self.startPartInstructionLogs = None
    
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
    
    # function used to finish actual instruction
    def finishActualInstruction ( self ) -> None :
        #
        # input: ------------------ SYSCALL EXIT START ------------------
        #
        # we are in the end part of the instruction
        self.startPartInstructionLogs = False
    
    # function used to set pid
    def setPid ( self , record: str ) -> None :
        #
        # input: PID: 30074
        #
        # if it is the start part
        if self.startPartInstructionLogs :
            #
            # get last element of the list of instructions
            instruction: Instruction = self.listInstruction [ -1 ]
            #
            # set pid of last instruction of the list
            instruction.pid: int = record
    
    # function used to set spid
    def setSpid ( self , record: str ) -> None :
        #
        # input: SPID: 30074
        #
        # if it is the start part
        if self.startPartInstructionLogs :
            #
            # get last element of the list of instructions
            instruction: Instruction = self.listInstruction [ -1 ]
            #
            # set spid of last instruction of the list
            instruction.spid: int = record
    
    # function used to set name
    def setName ( self , record: str ) -> None :
        #
        # input: Syscall = clock_gettime (113)
        #
        # get last element of the list of instructions
        instruction: Instruction = self.listInstruction [ -1 ]
        #
        # set name last instruction of the list
        instruction.name: str = record
    
    # function used to set timestamp
    def setTimestamp ( self , record: str ) -> None :
        #
        # input: Timestamp: 1677745254687394
        #
        # get last element of the list of instructions
        instruction: Instruction = self.listInstruction [ -1 ]
        #
        # if it is the start part
        if self.startPartInstructionLogs :
            #
            # set start timestamp of last instruction of the list
            instruction.startTimestamp: int = record
        #
        # if it is the end part
        else :
            #
            # set finish timestamp of last instruction of the list
            instruction.finishTimestamp: int = record
    
    # function used to set return value
    def setReturnValue ( self , record: str ) -> None :
        #
        # input: Return value: 000000000000000000
        #
        # get last element of the list of instructions
        instruction: Instruction = self.listInstruction [ -1 ]
        #
        # set return value of last instruction of the list
        instruction.returnValue: int = record
    
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
        # create the file for sequences manager
        fileSequencesManager = File ( mainDirOutputStructureLogs + "\\ptracer\\Sequences" + self.settings.extensionLogFile , "w" )
        fileSequencesManager.writeIntoFile ( self.sequences )
