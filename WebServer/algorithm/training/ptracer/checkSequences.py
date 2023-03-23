# class used to check sequences in whitelist
from dataStructure.ptracer.sequences import Instruction
from dataStructure.ptracer.sequences import Sequences

class CheckSequences ( Sequences ) :
    
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
    
    def f ( self , instruction , actualInstruction ) :
        #
        # if actual instruction is not none
        if actualInstruction is not None :
            #
            if (instruction.pid , instruction.spid , "prev") not in self.previousNextInstructionDictionary.keys ( ) :
                self.previousNextInstructionDictionary [ (instruction.pid , instruction.spid , "prev") ] = actualInstruction
            else :
                self.checkSequence ( self.previousNextInstructionDictionary [ (instruction.pid , instruction.spid , "prev") ] , actualInstruction )
                self.previousNextInstructionDictionary [ (instruction.pid , instruction.spid , "prev") ] = actualInstruction
    
    # function used to check a sequences in whitelist
    def checkSequence ( self , previousInstruction: str , nextInstruction: str ) -> None :
        #
        # obtain the right instruction
        listInstructions: list [ Instruction ] = [ obj for obj in self.listInstructions if obj.name == previousInstruction ]
        #
        # if there is at least one element
        if len ( listInstructions ) > 0 :
            #
            # obtain the right instruction
            instruction: Instruction = listInstructions [ 0 ]
            #
            # if next instruction is in the list of next instructions
            if nextInstruction in [ i.name for i in instruction.nextInstructions ] :
                #
                # increment the number of good sequences
                self.goodSequences: int = self.goodSequences + 1
                print ( "################################################################" )
                self.printStatistics ( )
            #
            # else if it is not a valid sequence
            else :
                #
                # increment the number of bad sequences
                self.badSequences: int = self.badSequences + 1
                #
                # it is not a valid sequence
                print ( "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@" )
                print ( "Found: " + previousInstruction + " -> " + nextInstruction )
                self.printStatistics ( )
                #
        # else if the instruction is not mapped
        else :
            #
            # instruction not mapped
            print ( "----------------------------------------------------------------" )
            print ( "Instruction " + str ( previousInstruction ) + " not mapped" )
    
    # function used to print statistics
    def printStatistics ( self ) :
        print ( "Good sequences: " + str ( self.goodSequences ) + " " + str ( 100 / (self.goodSequences + self.badSequences) * self.goodSequences ) + "%" )
        print ( "Bad sequences: " + str ( self.badSequences ) + " " + str ( 100 / (self.goodSequences + self.badSequences) * self.badSequences ) + "%" )
