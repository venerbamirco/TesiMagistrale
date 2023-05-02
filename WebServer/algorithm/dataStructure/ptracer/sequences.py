"""
LIST OF ALL SEQUENCES FOR EACH INSTRUCTION

	Instruction
		Name: nameinstruction
		Next: [nameinstruction1, nameinstruction2]

	Instruction
		Name: nameinstruction1
		Next: [nameinstruction2]

	Instruction
		Name: nameinstruction2
		Next: []
"""

import time

from algorithm.dataStructure.other.instruction import Instruction
from algorithm.settings.settings import Settings

# class to manage the single instruction
class SequenceRecord :
    
    # constructor to initialize a single instruction
    def __init__ ( self , name: str ) -> None :
        #
        # save the name of the instruction
        self.name: str = name
        #
        # empty list of possible next instructions
        self.nextInstructions: list [ SequenceRecord ] = list ( )
    
    # function used to add an instruction
    def addNextInstruction ( self , name: str ) -> None :
        #
        # if there is not the next instruction in the list
        if not any ( instruction.name == name for instruction in self.nextInstructions ) :
            #
            # create a simple instruction object
            instruction: SequenceRecord = SequenceRecord ( name )
            #
            # append the instruction in the list of possible instructions
            self.nextInstructions.append ( instruction )
            #
            # order the list of next instructions
            self.nextInstructions.sort ( key = lambda x : x.name )
    
    # function used to represent the object with only the name
    def __repr__ ( self ) -> str :
        #
        # return only the name
        return f"{self.name}"
    
    # function used to print the instruction object
    def __str__ ( self ) -> str :
        #
        # variable to store the output
        output: str = "\n\tInstruction\n"
        #
        # add the name
        output: str = f"{output}\t\tName: {self.name}\n"
        #
        # add the next possible instructions
        output: str = f"{output}\t\tNext: {self.nextInstructions}\n"
        #
        # return the output
        return output

# class to manage sequence of instructions
class Sequences :
    
    # constructor to initialize the structure for sequences
    def __init__ ( self , settings: Settings ) -> None :
        #
        # create a list of all instructions
        self.listInstructions: list [ SequenceRecord ] = list ( )
        #
        # dictionary of list of instructions for each pair pid spid
        self.dictionaryPidSpid: dict [ list [ str ] ] = dict ( )
        #
        # save reference for settings
        self.settings = settings
        #
        # dictionary for previous and next instruction for each pid spid pair
        self.previousNextInstructionDictionary: dict = dict ( )
        #
        # save the number of good sequences
        self.goodSequences: int = 0
        #
        # save the number of bad sequences
        self.badSequences: int = 0
    
    # function used to insert a new instruction in the dictionary
    def addInstruction ( self , pid: int , spid: int , name: str ) -> None :
        #
        # if the pair pid spid is not in the dictionary
        if (pid , spid) not in self.dictionaryPidSpid :
            #
            # insert in the actual position an empty list
            self.dictionaryPidSpid [ pid , spid ]: list [ str ] = list ( )
        #
        # append in the right index the actual instruction
        self.dictionaryPidSpid [ pid , spid ].append ( name )
        #
        # if the instruction is not in the list
        if not any ( instruction.name == name for instruction in self.listInstructions ) :
            #
            # create a new instruction object with an empty list of next instructions
            instruction: SequenceRecord = SequenceRecord ( name )
            #
            # append the actual instruction in the list of all instructions
            self.listInstructions.append ( instruction )
            #
            # order instructions in the list
            self.listInstructions.sort ( key = lambda x : x.name )
        #
        # if there are other previous instructions of actual pid spid pair
        if len ( self.dictionaryPidSpid [ pid , spid ] ) > 1 :
            #
            # obtain the previous instruction
            previousInstruction: str = self.dictionaryPidSpid [ pid , spid ] [ -2 ]
            #
            # obtain the next instruction
            nextInstruction: str = self.dictionaryPidSpid [ pid , spid ] [ -1 ]
            #
            # obtain the object in the list for the previous instruction
            prev: SequenceRecord = [ obj for obj in self.listInstructions if obj.name == previousInstruction ] [ 0 ]
            #
            # add the next instruction in the actual instruction next instructions list
            prev.addNextInstruction ( nextInstruction )
    
    # function used to get a specific instruction
    def getInstruction ( self , name: str ) -> SequenceRecord :
        #
        # obtain the list of possible instructions
        instructionsList: list [ SequenceRecord ] = [ obj for obj in self.listInstructions if obj.name == name ]
        #
        # if there is one instruction
        if len ( instructionsList ) > 0 :
            #
            # return the first element
            return instructionsList [ 0 ]
        #
        # else if there are no instructions
        else :
            #
            # return None
            return None
    
    # function used to insert a new instruction in the analyses
    def insertInstruction ( self , name: str ) -> None :
        #
        # if instruction not in the list
        if not any ( instruction.name == name for instruction in self.listInstructions ) :
            #
            # create a new instruction object with an empty list of next instructions
            i: SequenceRecord = SequenceRecord ( name )
            #
            # append the actual instruction in the list of all instructions
            self.listInstructions.append ( i )
            #
            # order instructions in the list
            self.listInstructions.sort ( key = lambda x : x.name )
    
    # function used to insert a next instruction in the analyses
    def insertNextInstruction ( self , previousInstruction: str , nextInstruction: str ) -> None :
        #
        # if previous instruction not in the list
        if not any ( instruction.name == previousInstruction for instruction in self.listInstructions ) :
            #
            # add previous instruction in the list
            self.listInstructions.append ( SequenceRecord ( previousInstruction ) )
        #
        # if next instruction not in the list
        if not any ( instruction.name == nextInstruction for instruction in self.listInstructions ) :
            #
            # add nextInstruction instruction in the list
            self.listInstructions.append ( SequenceRecord ( nextInstruction ) )
        #
        # obtain the right instruction
        instruction: SequenceRecord = [ obj for obj in self.listInstructions if obj.name == previousInstruction ] [ 0 ]
        #
        # add the next instruction in the actual instruction list
        instruction.addNextInstruction ( nextInstruction )
        #
        # order instructions in the list
        self.listInstructions.sort ( key = lambda x : x.name )
    
    # function used to print the dictionary of sequences of each instruction
    def __str__ ( self ) -> str :
        #
        # variable to store the output
        output: str = ""
        #
        # print debug row of sequences for each instruction
        output: str = f"{output}\nLIST OF ALL SEQUENCES FOR EACH INSTRUCTION\n"
        #
        # for each instruction
        for instruction in self.listInstructions :
            #
            # print debug row for another instruction fragment
            output: str = f"{output}{instruction}"
        #
        # return the output
        return output
    
    # function used to get the actual sequence previous next instruction pair
    def getActualSequence ( self , instruction: Instruction , actualInstruction: str ) -> bool :
        #
        # if actual instruction is not none
        if actualInstruction is not None :
            #
            # if there is not a previous instruction
            if (instruction.pid , instruction.spid , "prev") not in self.previousNextInstructionDictionary.keys ( ) :
                #
                # save the previous instruction
                self.previousNextInstructionDictionary [ (instruction.pid , instruction.spid , "prev") ] = actualInstruction
            #
            # if there is a previous instruction
            else :
                #
                # check sequences previous actual instruction
                returnValue: bool = self.checkSequence ( self.previousNextInstructionDictionary [ (instruction.pid , instruction.spid , "prev") ] , actualInstruction )
                #
                # update the previous with actual instruction
                self.previousNextInstructionDictionary [ (instruction.pid , instruction.spid , "prev") ] = actualInstruction
                #
                # return the result of actual sequence
                return returnValue
        #
        # return true because it is valid
        return True
    
    # function used to check a sequences in whitelist
    def checkSequence ( self , previousInstruction: str , nextInstruction: str ) -> bool :
        #
        # obtain the right instruction
        listInstructions: list [ SequenceRecord ] = [ obj for obj in self.listInstructions if obj.name == previousInstruction ]
        #
        # if there is at least one element
        if len ( listInstructions ) > 0 :
            #
            # obtain the right instruction
            instruction: SequenceRecord = listInstructions [ 0 ]
            #
            # if next instruction is in the list of next instructions
            if nextInstruction in [ i.name for i in instruction.nextInstructions ] :
                #
                # increment the number of good sequences
                self.goodSequences: int = self.goodSequences + 1
            #
            # else if it is not a valid sequence
            else :
                #
                # increment the number of bad sequences
                self.badSequences: int = self.badSequences + 1
                #
                # if training mode enabled
                if self.settings.training :
                    #
                    # debug row
                    print ( "----------------------------------------------------------------" )
                    #
                    # insert in input if we want to map this sequence
                    mapThisSequences = input ( "Insert " + previousInstruction + " -> " + nextInstruction + " sequence? [yes/no] " )
                    #
                    # if we want to map this sequence
                    if mapThisSequences == "yes" :
                        #
                        # map actual instruction
                        self.insertNextInstruction ( previousInstruction , nextInstruction )
                    #
                    # else if it is a insecure sequence
                    else:
                        #
                        # return false because invalid sequence
                        return False
                #
                # if not training mode
                else :  #
                    #
                    # if we can show invalid sequence
                    if Settings.invalidSequence:
                        # it is not a valid sequence
                        print ( "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@" )
                        print ( "Timestamp: " + str ( time.time_ns ( ) ) )
                        print ( "Found: " + previousInstruction + " -> " + nextInstruction )
                    #
                    # print statistics
                    self.printStatistics ( )
                    #
                    # return false because invalid sequence
                    return False
        #
        # else if the instruction is not mapped
        else :
            #
            # map actual instruction
            self.insertInstruction ( previousInstruction )
            #
            # if training mode enabled
            if self.settings.training :
                #
                # if we can show invalid sequence
                if Settings.invalidSequence :
                    #
                    # instruction not mapped
                    print ( "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@" )
                    print ( "Timestamp: " + str ( time.time_ns ( ) ) )
                    print ( "Instruction " + previousInstruction + " not mapped" )
            #
            # print statistics
            self.printStatistics ( )
        #
        # return true because valid sequence
        return True
    
    # function used to print statistics
    def printStatistics ( self ) :
        #
        # if we can show invalid sequence
        if Settings.percentageValidInvalidSequence :
            print ( "Good sequences: " + str ( self.goodSequences ) + " " + str ( 100 / (self.goodSequences + self.badSequences) * self.goodSequences ) + "%" )
            print ( "Bad sequences: " + str ( self.badSequences ) + " " + str ( 100 / (self.goodSequences + self.badSequences) * self.badSequences ) + "%" )

if __name__ == "__main__" :
    d = Sequences ( )
    d.insertInstruction ( "Nome" )
    d.insertNextInstruction ( "Nome" , "nome1" )
    d.insertNextInstruction ( "Nome" , "nome2" )
    d.insertNextInstruction ( "nome2" , "nome3" )
    print ( d )
