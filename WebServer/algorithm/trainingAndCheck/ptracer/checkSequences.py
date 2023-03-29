import time

from dataStructure.other.instruction import Instruction
from dataStructure.ptracer.sequences import SequenceRecord
from dataStructure.ptracer.sequences import Sequences

# class used to check sequences in whitelist
class CheckSequences ( Sequences ) :
    
    # constructor to initialize the object for sequences check
    def __init__ ( self ) :
        super ( ).__init__ ( )
        #
        # dictionary for previous and next instruction for each pid spid pair
        self.previousNextInstructionDictionary: dict = dict ( )
        #
        # save the number of good sequences
        self.goodSequences: int = 0
        #
        # save the number of bad sequences
        self.badSequences: int = 0
    
    # function used to get the actual sequence previous next instruction pair
    def getActualSequence ( self , instruction: Instruction , actualInstruction: str ) :
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
                self.checkSequence ( self.previousNextInstructionDictionary [ (instruction.pid , instruction.spid , "prev") ] , actualInstruction )
                #
                # update the previous with actual instruction
                self.previousNextInstructionDictionary [ (instruction.pid , instruction.spid , "prev") ] = actualInstruction
    
    # function used to check a sequences in whitelist
    def checkSequence ( self , previousInstruction: str , nextInstruction: str ) -> None :
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
                # it is not a valid sequence
                print ( "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@" )
                print ( "Timestamp: " + str ( time.time_ns ( ) ) )
                print ( "Found: " + previousInstruction + " -> " + nextInstruction )
                self.printStatistics ( )
        #
        # else if the instruction is not mapped
        else :
            #
            # instruction not mapped
            print ( "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@" )
            print ( "Timestamp: " + str ( time.time_ns ( ) ) )
            print ( "Instruction " + str ( previousInstruction ) + " not mapped" )
    
    # function used to print statistics
    def printStatistics ( self ) :
        print ( "Good sequences: " + str ( self.goodSequences ) + " " + str ( 100 / (self.goodSequences + self.badSequences) * self.goodSequences ) + "%" )
        print ( "Bad sequences: " + str ( self.badSequences ) + " " + str ( 100 / (self.goodSequences + self.badSequences) * self.badSequences ) + "%" )
