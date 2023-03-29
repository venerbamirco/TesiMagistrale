import os

from algorithm.trainingAndCheck.ptracer.checkAnalyses import CheckAnalyses
from algorithm.trainingAndCheck.ptracer.checkSequences import CheckSequences
from dataStructure.other.file import File

# class used to recover all trainingAndCheck data
class Recover :
    
    # constructor to initialize the recover object
    def __init__ ( self , analyses: CheckAnalyses , sequences: CheckSequences ) -> None :
        #
        # save the reference for analyses manager
        self.analyses: CheckAnalyses = analyses
        #
        # save the reference for sequences manager
        self.sequences: CheckSequences = sequences
        #
        # file used for instructions analyses
        self.fileInstruction: File = File ( os.path.abspath ( "./logs/training/ptracer/Analyses.log" ) , "r" )
        #
        # file used for instructions analyses
        self.fileSequences: File = File ( os.path.abspath ( "./logs/training/ptracer/Sequences.log" ) , "r" )
        #
        # trainingAndCheck for instruction analyses
        self.recoverInformationsInstruction ( )
        #
        # trainingAndCheck for sequences analyses
        self.recoverInformationsSequences ( )
    
    # function used to recover all informations about each instruction
    def recoverInformationsInstruction ( self ) -> None :
        #
        # name of last found instruction
        name: str = ""
        #
        # until the file is not finished
        while True :
            #
            # get next line from file
            line: str = self.fileInstruction.file.readline ( )
            #
            # if the end of file is reached
            if not line :
                #
                # break the loop
                break
            #
            # if actual row contains the name of instruction Name: clock_gettime
            if "Name" in line :
                #
                # save the actual name
                name: str = line.split ( ":" ) [ 1 ].strip ( )
                #
                # add the instruction in analyses of each instruction
                self.analyses.addInstruction ( line.split ( ":" ) [ 1 ].strip ( ) )
            #
            # else if actual row contains the list of measurements List measurements: [3718, 5542, 517, 721, 728]
            elif "List measurements" in line :
                #
                # get list of measurements
                listMeasurements: str = line.split ( ":" ) [ 1 ].strip ( " []\n" )
                #
                # for each measure
                for measure in listMeasurements.split ( "," ) :
                    #
                    # add the measure in analyses
                    self.analyses.addMeasurement ( name , int ( measure.strip ( ) ) )
    
    # function used to recover all informations about sequences
    def recoverInformationsSequences ( self ) -> None :
        #
        # name of last found instruction
        name: str = ""
        #
        # until the file is not finished
        while True :
            #
            # get next line from file
            line: str = self.fileSequences.file.readline ( )
            #
            # if the end of file is reached
            if not line :
                #
                # break the loop
                break
            #
            # if actual row contains the name of instruction Name: clock_gettime
            if "Name" in line :
                #
                # save the actual name
                name: str = line.split ( ":" ) [ 1 ].strip ( )
                #
                # add the instruction in analyses of each instruction
                self.sequences.insertInstruction ( line.split ( ":" ) [ 1 ].strip ( ) )
            #
            # else if actual row contains the list of measurements Next: [clock_gettime, epoll_ctl, futex]
            elif "Next" in line :
                #
                # get list of measurements
                listMeasurements: str = line.split ( ":" ) [ 1 ].strip ( " []\n" )
                #
                # for each measure
                for measure in listMeasurements.split ( "," ) :
                    #
                    # add the measure in analyses
                    self.sequences.insertNextInstruction ( name , measure.strip ( ) )
