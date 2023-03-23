# class used for the ptracer manager
from algorithm.training.training import Training
from dataStructure.other.file import File
from dataStructure.other.instruction import Instruction
from dataStructure.ptracer.analyses import Analyses
from dataStructure.ptracer.instructions import Instructions
from dataStructure.ptracer.sequences import Sequences
from settings.settings import Settings

class PtracerManager :
    
    # constructor to initialize the ptracer manager
    def __init__ ( self , settings: Settings , training: Training ) -> None :
        #
        # save the reference for training manager
        self.training: Training = training
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
        # initialize the instruction manager
        self.instructions: Instructions = Instructions ( self.analyses )
        #
        # initialize the sequences manager
        self.sequences: Sequences = Sequences ( )
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
    
    # function used to insert the first part of an instruction
    def setFirstPartInstruction ( self ) -> None :
        #
        # input: ------------------ SYSCALL ENTRY STOP ------------------
        #
        # if there are more than one instruction in the list
        if len ( self.listInstruction ) > 0 :
            #
            # get last instruction from the list
            instruction: Instruction = self.listInstruction [ -1 ]
            #
            # insert the instruction in the relative manager
            self.instructions.addInstruction ( instruction.name , instruction.pid , instruction.spid , instruction.startTimestamp )
            #
            # delete from the list the actual instruction
            self.listInstruction.remove ( instruction )
            #
            # add the sequence of actual instruction
            self.sequences.addInstruction ( instruction.pid , instruction.spid , instruction.name )
    
    # function used to delete a new instruction
    def deleteNewInstruction ( self ) -> None :
        #
        # if there are more than one instruction in the list
        if len ( self.listInstruction ) > 0 :
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
        #
        # create a new instruction element
        instruction: Instruction = Instruction ( )
        #
        # append the new element in the list
        self.listInstruction.append ( instruction )
    
    # function used to finish a specific instruction
    def finishSpecificInstruction ( self ) -> None :
        #
        # input: ------------------ SYSCALL EXIT STOP ------------------
        #
        # if there are more than one instruction in the list
        if len ( self.listInstruction ) > 0 :
            #
            # get last instruction from the list
            instruction: Instruction = self.listInstruction [ -1 ]
            #
            # insert the instruction in the relative manager and save the name of actual instruction
            actualInstruction: str = self.instructions.finishInstruction ( instruction.pid , instruction.spid , instruction.returnValue , instruction.finishTimestamp )
            self.training.sequencesTraining.f ( instruction , actualInstruction )
            
            #
            # delete from the list the actual instruction
            self.listInstruction.remove ( instruction )
    
    # function used to set pid
    def setPid ( self , record: str ) -> None :
        #
        # input: PID: 30074
        #
        # if there are more than one instruction in the list
        if len ( self.listInstruction ) > 0 :
            #
            # save input pid
            pid: int = int ( record.split ( ":" ) [ 1 ].strip ( ) , 10 )
            #
            # get last element of the list of instructions
            instruction: Instruction = self.listInstruction [ -1 ]
            #
            # set pid of last instruction of the list
            instruction.pid: int = pid
    
    # function used to set spid
    def setSpid ( self , record: str ) -> None :
        #
        # input: SPID: 30074
        #
        # if there are more than one instruction in the list
        if len ( self.listInstruction ) > 0 :
            #
            # save input spid
            spid: int = int ( record.split ( ":" ) [ 1 ].strip ( ) , 10 )
            #
            # get last element of the list of instructions
            instruction: Instruction = self.listInstruction [ -1 ]
            #
            # set spid of last instruction of the list
            instruction.spid: int = spid
    
    # function used to set name
    def setName ( self , record: str ) -> None :
        #
        # input: Syscall = clock_gettime (113)
        #
        # if there are more than one instruction in the list
        if len ( self.listInstruction ) > 0 :
            #
            # save input name
            name: str = record.split ( "=" ) [ 1 ].split ( "(" ) [ 0 ].strip ( )
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
        # if there are more than one instruction in the list
        if len ( self.listInstruction ) > 0 :
            #
            # save input timestamp
            timestamp: int = int ( record.split ( ":" ) [ 1 ].strip ( ) , 10 )
            #
            # get last element of the list of instructions
            instruction: Instruction = self.listInstruction [ -1 ]
            #
            # if it is the start part
            if self.startPartInstructionLogs :
                #
                # set start timestamp of last instruction of the list
                instruction.startTimestamp: int = timestamp
            #
            # else if it is the final part
            else :
                #
                # set finish timestamp of last instruction of the list
                instruction.finishTimestamp: int = timestamp
    
    # function used to set return value
    def setReturnValue ( self , record: str ) -> None :
        #
        # input: Return value: 000000000000000000
        #
        # if there are more than one instruction in the list
        if len ( self.listInstruction ) > 0 :
            #
            # get last element of the list of instructions
            instruction: Instruction = self.listInstruction [ -1 ]
            #
            # variable to store return value
            returnValue: int = 0
            #
            # if the number is hex
            if "x" in record :
                #
                # save input return value
                returnValue: int = int ( record.split ( ":" ) [ 1 ].strip ( ) , 16 )
            #
            # if the number is dec
            else :
                #
                # save input return value
                returnValue: int = int ( record.split ( ":" ) [ 1 ].strip ( ) , 10 )
            #
            # set return value of last element of the list
            instruction.returnValue: int = returnValue
    
    # function used to set duration
    def setDuration ( self ) -> None :
        #
        # if there are more than one instruction in the list
        if len ( self.listInstruction ) > 0 :
            #
            # get last element of the list of instructions
            instruction: Instruction = self.listInstruction [ -1 ]
            #
            # if all data are correctly typed
            if instruction.finishTimestamp is not None and instruction.startTimestamp is not None :
                #
                # set duration of last instruction of the list
                instruction.duration: int = instruction.finishTimestamp - instruction.startTimestamp
    
    # function used to save the all ptracer logs
    def savePtracerLogs ( self , mainDirOutputStructureLogs: str ) :
        #
        # create the file for analyses manager
        fileAnalysesManager = File ( mainDirOutputStructureLogs + "\\ptracer\\Analyses" + self.settings.extensionLogFile , "w" )
        fileAnalysesManager.writeIntoFile ( self.analyses )
        #
        # create the file for instructions manager
        fileInstructionsManager = File ( mainDirOutputStructureLogs + "\\ptracer\\Instructions" + self.settings.extensionLogFile , "w" )
        fileInstructionsManager.writeIntoFile ( self.instructions )
        #
        # create the file for instructions manager
        fileSequencesManager = File ( mainDirOutputStructureLogs + "\\ptracer\\Sequences" + self.settings.extensionLogFile , "w" )
        fileSequencesManager.writeIntoFile ( self.sequences )
