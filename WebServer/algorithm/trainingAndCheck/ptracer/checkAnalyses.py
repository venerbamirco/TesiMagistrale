import time

from dataStructure.ptracer.analyses import Analyses
from dataStructure.ptracer.analyses import AnalysesRecord

class CheckAnalyses ( Analyses ) :
    
    # constructor to initialize the object for analyses check
    def __init__ ( self ) :
        super ( ).__init__ ( )
    
    # function used to check actual duration
    def checkDurationActualInstruction ( self , actualInstruction: str , actualDuration: int ) :
        #
        # obtain the right instruction
        instruction: AnalysesRecord = self.getInstruction ( actualInstruction )
        #
        # if there is an instruction
        if instruction is not None :
            #
            # if shorter duration
            if actualDuration < instruction.minimumMeasure :
                #
                # do nothing because is not possible debugger
                pass
            #
            # if longer duration
            if actualDuration > instruction.maximumMeasure :
                #
                #
                print ( "----------------------------------------------------------------" )
                print ( "Timestamp: " + str ( time.time_ns ( ) ) )
                print ( actualInstruction + " has longer duration: " + str ( actualDuration ) + " vs " +
                        str ( instruction.minimumMeasure ) + "->" + str ( instruction.maximumMeasure ) )
        #
        # else if the instruction is not mapped
        else :
            #
            # instruction not mapped
            print ( "----------------------------------------------------------------" )
            print ( "Timestamp: " + str ( time.time_ns ( ) ) )
            print ( "Instruction " + actualInstruction + " not mapped" )
