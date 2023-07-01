import os

from algorithm.dataStructure.other.file import File
from algorithm.dataStructure.other.instruction import Instruction
from algorithm.dataStructure.ptracer.analyses import Analyses
from algorithm.dataStructure.ptracer.instructions import Instructions
from algorithm.dataStructure.ptracer.sequences import Sequences
from algorithm.settings.settings import Settings
from algorithm.training.training import Training
from functions.functions import lcs_algo

# class used for the ptracer manager
class PtracerManager :
    
    # constructor to initialize the ptracer manager
    def __init__ ( self , training: Training ) -> None :
        #
        # save the reference for training manager
        self.training: Training = training
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
        #
        # list of subsequence in relation last execution
        self.listAllSubsequences: list [ str ] = list ( )
    
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
            actualInstruction , actualDuration = self.instructions.finishInstruction ( instruction.pid , instruction.spid , instruction.returnValue , instruction.finishTimestamp )
            #
            # if actual instruction valid
            if actualInstruction is not None :
                #
                # check sequence
                returnValue: bool = self.training.sequences.getActualSequence ( instruction , actualInstruction )
                #
                # if false because sequence non valid
                if not returnValue :
                    #
                    # increment security level
                    self.training.devices.incrementLevelSecurity ( self.training.devices.listDevices [ 0 ].ipAddress , "Sequence not secure" )
                #
                # check duration
                returnValue: bool = self.training.analyses.checkDurationActualInstruction ( actualInstruction , actualDuration )
                #
                # if false because longer duration
                if not returnValue :
                    #
                    # increment security level
                    self.training.devices.incrementLevelSecurity ( self.training.devices.listDevices [ 0 ].ipAddress , "Instructions much time" )
                
                #
                # if not training mode
                if not Settings.training :
                    #
                    # if there are previous executions
                    if len ( self.training.instructionsLists.instructionsList ) > 0 :
                        #
                        # get last execution instructions
                        instructionsLastExecutions: list [ str ] = self.training.instructionsLists.instructionsList [ -1 ]
                        #
                        # get actual sequence instructions
                        actualInstructions: list [ str ] = self.sequences.dictionaryPidSpid [ instruction.pid , instruction.spid ]
                        #
                        # get list of subsequence with last execution
                        listSubsequence: list [ str ] = lcs_algo ( instructionsLastExecutions , actualInstructions , len ( instructionsLastExecutions ) , len ( actualInstructions ) )
                        #
                        # for each subsequence
                        for subsequence in listSubsequence :
                            #
                            # if actual subsequence is longer than a tot
                            if subsequence.count ( "," ) > Settings.numberInstructionInSubsequence :
                                #
                                # flag for insertion
                                insertionFlag: bool = False
                                #
                                # number of found subsequences
                                numberOfFoundSubsequences: int = len ( self.listAllSubsequences )
                                #
                                # for each subsequence in the list already saved
                                for i in range ( 0 , len ( self.listAllSubsequences ) ) :
                                    #
                                    # if sub is longer than actual
                                    if subsequence in self.listAllSubsequences [ i ] :
                                        #
                                        # subsequence already in the list
                                        insertionFlag: bool = True
                                    #
                                    # if sub is less than actual
                                    elif self.listAllSubsequences [ i ] in subsequence :
                                        #
                                        # remove the shortest subsequence
                                        self.listAllSubsequences.remove ( self.listAllSubsequences [ i ] )
                                        #
                                        # addd the longest subsequence
                                        self.listAllSubsequences.append ( subsequence )
                                        #
                                        # subsequence inserted in the list
                                        insertionFlag: bool = True
                                        #
                                        # rerun the whole list
                                        i = 0
                                #
                                # if the insertion flag is false
                                if not insertionFlag :
                                    #
                                    # insert actual subsequence
                                    self.listAllSubsequences.append ( subsequence )
                                #
                                # if we add a new subsequence
                                if numberOfFoundSubsequences < len ( self.listAllSubsequences ) :
                                    #
                                    # print found new subsequence
                                    self.training.devices.incrementLevelSecurity ( self.training.devices.listDevices [ 0 ].ipAddress , "Subsequences found" )
                                    #
                                    # update number of found sequences
                                    numberOfFoundSubsequences: int = len ( self.listAllSubsequences )
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
                #
                # if duration is negative
                if instruction.duration < 0 :
                    #
                    # set positive duration
                    instruction.duration: int = instruction.duration * (-1)
    
    # function used to get the list of changed flags inside a specific timestamp range
    def getListOfCHangedFlags ( self , flagAndroid: list [ str ] , startTimestamp: str , finishTimestamp: str ) :
        #
        # flags in this timestamp range
        flagActualTimestamp: list [ str ] = [ ]
        #
        # for each flag
        for flag in flagAndroid :
            #
            # decode actual flag
            x , y = flag
            #
            # if flag in actual range
            if str ( startTimestamp ) <= str ( x ) < str ( finishTimestamp ) :
                #
                # append actual flag
                flagActualTimestamp.append ( flag )
        #
        # return actual flag value
        return flagActualTimestamp
    
    def savePtracerLogs ( self , mainDirOutputStructureLogs: str , flagAndroid: list [ str ] ) :
        #
        # create the file for analyses manager
        fileAnalysesManager = File ( mainDirOutputStructureLogs + "\\ptracer\\Analyses" + Settings.extensionLogFile , "w" )
        fileAnalysesManager.writeIntoFile ( self.analyses )
        #
        # create the file for instructions manager
        fileInstructionsManager = File ( mainDirOutputStructureLogs + "\\ptracer\\Instructions" + Settings.extensionLogFile , "w" )
        fileInstructionsManager.writeIntoFile ( self.instructions )
        #
        # create the file for sequences manager
        fileSequencesManager = File ( mainDirOutputStructureLogs + "\\ptracer\\Sequences" + Settings.extensionLogFile , "w" )
        fileSequencesManager.writeIntoFile ( self.sequences )
        #
        # create the file for instructions list manager
        fileInstructionsListManager = File ( mainDirOutputStructureLogs + "\\ptracer\\InstructionsList" + Settings.extensionLogFile , "w" )
        for pair in self.sequences.dictionaryPidSpid :
            fileInstructionsListManager.writeIntoFile ( str ( pair ) + " -> " + str ( self.sequences.dictionaryPidSpid [ pair ] ) )
        #
        # update training data of sequences
        fileSequencesTraining: File = File ( os.path.abspath ( "./logs/training/ptracer/Sequences.log" ) , "w" )
        fileSequencesTraining.writeIntoFile ( str ( self.training.sequences ) )
        #
        # update training data of analyses
        fileAnalysesTraining: File = File ( os.path.abspath ( "./logs/training/ptracer/Analyses.log" ) , "w" )
        fileAnalysesTraining.writeIntoFile ( str ( self.training.analyses ) )
        #
        # create the file for instructions list manager
        fileInstructionsListsManager = File ( os.path.abspath ( "./logs/training/ptracer/InstructionsLists.log" ) , "w" )
        fileInstructionsListsManager.writeIntoFile ( str ( self.training.instructionsLists ) )
        #
        # number of total instructions
        totalInstruction: int = 0
        #
        # list of all sequences
        listAllSequences: list [ str ] = list ( )
        for pair in self.sequences.dictionaryPidSpid :
            for element in self.sequences.dictionaryPidSpid [ pair ] :
                totalInstruction: int = totalInstruction + 1
                listAllSequences.append ( element )
        fileInstructionsListsManager.writeIntoFile ( "\t" + str ( listAllSequences ) + "\n" )
        #
        # create the file for found subsequences
        fileFoundSubsequencesManager = File ( os.path.abspath ( mainDirOutputStructureLogs + "\\ptracer\\FoundSubsequences.log" ) , "w" )
        fileFoundSubsequencesManager.writeIntoFile ( "\nLIST OF FOUND SUBSEQUENCES\n" )
        for subsequence in self.listAllSubsequences :
            fileFoundSubsequencesManager.writeIntoFile ( "\tSUBSEQUENCE" )
            fileFoundSubsequencesManager.writeIntoFile ( "\t\tPortion of code: " + str ( 100 / totalInstruction * (subsequence.count ( "," ) + 1) ) + "%" )
            fileFoundSubsequencesManager.writeIntoFile ( "\t\tSubsequence:" + str ( subsequence ) + "\n" )
        
        #
        # create the csv file for instructions
        fileCsvInstructions = File ( os.path.abspath ( mainDirOutputStructureLogs + "\\ptracer\\csvFile.csv" ) , "w" )
        fileCsvInstructions.writeIntoFile ( "macrodroid=" + str ( Settings.macroDroid ) )
        fileCsvInstructions.writeIntoFile ( "fakeclient=" + str ( Settings.fakeClient ) )
        fileCsvInstructions.writeIntoFile ( "Id,Pid,Spid,Name,Finished,StartTimestamp,FinishTimestamp,ReturnValue,Timestamp,DebugApp,DeveloperOptions,ChargingType,PtracerStarted,StationaryDevice,SensorAlert,DebuggerFound,InstructionMuchTime,SubsequenceFound,SequenceNotSecure" )
        id = 1
        print ( flagAndroid )
        prev = ",no,no,no,no,no,no,no,no,no,no"
        for i in self.instructions.listAllInstructions :
            if i.startTimestamp is not None and i.finishTimestamp is not None :
                if id == 1 :
                    fileCsvInstructions.writeIntoFile ( str ( id ) + "," + str ( i.pid ) + "," + str ( i.spid ) + "," + str ( i.name ) + "," + str ( i.finished ) + "," + str ( i.startTimestamp ) + "," + str ( i.finishTimestamp ) + "," + str ( i.returnValue ) + str ( i.startTimestamp ) + str ( prev ) )
                else :
                    #
                    # get list of flag that change in actual timestamp range
                    actualFlags = self.getListOfCHangedFlags ( flagAndroid , i.startTimestamp , i.finishTimestamp )
                    if len ( actualFlags ) > 0 :
                        #
                        # for each flag
                        for flag in actualFlags :
                            x , y = flag
                            x = int ( x )
                            y = "," + y
                            print ( "--------" )
                            print ( x )
                            print ( y )
                            # print ( "ciao" )
                            print ( str ( int ( i.startTimestamp / 1000 ) ) + " <= " + str ( int ( x / 1000 ) ) + " <= " + str ( int ( i.finishTimestamp / 1000 ) ) )
                            print ( "ciao" )
                            if str ( i.startTimestamp ) <= str ( x ) <= str ( i.finishTimestamp ) :
                                print ( "ciao1" )
                                if str ( i.startTimestamp ) == str ( x ) :
                                    print ( "ciao2" )
                                    fileCsvInstructions.writeIntoFile ( str ( id ) + "," + str ( i.pid ) + "," + str ( i.spid ) + "," + str ( i.name ) + "," + str ( i.finished ) + "," + str ( i.startTimestamp ) + "," + str ( i.finishTimestamp ) + "," + str ( i.returnValue ) + "," + str ( x ) + str ( y ) )
                                    prev = y
                                else :
                                    print ( "ciao3" )
                                    fileCsvInstructions.writeIntoFile ( str ( id ) + "," + str ( i.pid ) + "," + str ( i.spid ) + "," + str ( i.name ) + "," + str ( i.finished ) + "," + str ( i.startTimestamp ) + "," + str ( i.finishTimestamp ) + "," + str ( i.returnValue ) + "," + str ( i.startTimestamp ) + str ( prev ) )
                                    fileCsvInstructions.writeIntoFile ( str ( id ) + "," + str ( i.pid ) + "," + str ( i.spid ) + "," + str ( i.name ) + "," + str ( i.finished ) + "," + str ( i.startTimestamp ) + "," + str ( i.finishTimestamp ) + "," + str ( i.returnValue ) + "," + str ( x ) + str ( y ) )
                                    prev = y
                    else :
                        print ( "ciao4" )
                        fileCsvInstructions.writeIntoFile ( str ( id ) + "," + str ( i.pid ) + "," + str ( i.spid ) + "," + str ( i.name ) + "," + str ( i.finished ) + "," + str ( i.startTimestamp ) + "," + str ( i.finishTimestamp ) + "," + str ( i.returnValue ) + "," + str ( i.startTimestamp ) + str ( prev ) )
                
                id = id + 1
