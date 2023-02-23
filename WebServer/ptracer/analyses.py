"""
ANALYSIS OF ALL INSTRUCTIONS

	Instruction
		Name: NameInstruction
		Minimum duration: 1
		Maximum duration: 6
		Average duration: 3.5
		Variance: 2.9166666666666665
		Number measurements: 6
		Good terminations: 2
		Bad terminations: 4
		List measurements: [1, 2, 3, 4, 5, 6]
"""

from statistics import mean

from numpy import var

# class to manage the analyses for each instruction
class Instruction :
    
    # constructor to initialize the analyses of actual instruction
    def __init__ ( self , name: str ) -> None :
        #
        # set the name
        self.name: str = name
        #
        # set the minimum measure of duration
        self.minimumMeasure: int = 0
        #
        # set the maximum measure of duration
        self.maximumMeasure: int = 0
        #
        # set the average measure of duration
        self.averageMeasure: float = 0
        #
        # set the variance measure
        self.varianceMeasure: float = 0
        #
        # set the number of measurements
        self.numberMeasurements: int = 0
        #
        # set the number of good terminations
        self.numberGoodTerminations: int = 0
        #
        # set the number of bad terminations
        self.numberBadTerminations: int = 0
        #
        # set as empty the list of measurements of durations
        self.listMeasurements: list [ int ] = list ( )
    
    # function used to insert a new measure for the actual instruction
    def addMeasurement ( self , duration: int , success: bool ) -> None :
        #
        # increment the number of measurements
        self.numberMeasurements: int = self.numberMeasurements + 1
        #
        # add the new measure in the list
        self.listMeasurements.append ( duration )
        #
        # update the minimum measure of duration
        self.minimumMeasure: int = min ( self.listMeasurements )
        #
        # update the maximum measure of duration
        self.maximumMeasure: int = max ( self.listMeasurements )
        #
        # update the average measure of duration
        self.averageMeasure: float = mean ( self.listMeasurements )
        #
        # update the variance of durations
        self.varianceMeasure: float = var ( self.listMeasurements )
        #
        # if the instruction is terminated in a good manner
        if success :
            #
            # increment the counter of good terminations
            self.numberGoodTerminations: int = self.numberGoodTerminations + 1
        #
        # if the instruction is terminated in a bad manner
        else :
            #
            # increment the counter of bad terminations
            self.numberBadTerminations: int = self.numberBadTerminations + 1
    
    # function used to print an instruction object
    def __str__ ( self ) -> str :
        #
        # variable to store the output
        output: str = "\n\tInstruction\n"
        #
        # add name
        output: str = f"{output}\t\tName: {self.name}\n"
        #
        # add minimum measure of duration
        output: str = f"{output}\t\tMinimum duration: {self.minimumMeasure}\n"
        #
        # add maximum measure of duration
        output: str = f"{output}\t\tMaximum duration: {self.maximumMeasure}\n"
        #
        # add average measure of duration
        output: str = f"{output}\t\tAverage duration: {self.averageMeasure}\n"
        #
        # add variance measure of duration
        output: str = f"{output}\t\tVariance: {self.varianceMeasure}\n"
        #
        # add number of measurements of duration
        output: str = f"{output}\t\tNumber measurements: {self.numberMeasurements}\n"
        #
        # add number of good terminations
        output: str = f"{output}\t\tGood terminations: {self.numberGoodTerminations}\n"
        #
        # add number of bad terminations
        output: str = f"{output}\t\tBad terminations: {self.numberBadTerminations}\n"
        #
        # add list of measurements
        output: str = f"{output}\t\tList measurements: {self.listMeasurements}\n"
        #
        # return the output
        return output

# class used to manage analyses of each instruction
class Analyses :
    
    # constructor to initialize the structure for analyses
    def __init__ ( self ) -> None :
        #
        # create an empty list of analyses instructions
        self.listAllInstructions: list [ Instruction ] = list ( )
    
    # function used to insert a new instruction into analyses
    def addInstruction ( self , name: str ) -> None :
        #
        # if the instruction is not in the list
        if not any ( instruction.name == name for instruction in self.listAllInstructions ) :
            #
            # create a new instruction
            instruction: Instruction = Instruction ( name )
            #
            # append in the list the new instruction
            self.listAllInstructions.append ( instruction )
            #
            # order the list of all instructions
            self.listAllInstructions.sort ( key = lambda x : x.name )
    
    # function used to insert a new measurement for an instruction
    def addMeasurement ( self , name: str , duration: int , success: bool ) -> None :
        #
        # if the instruction is not in the analyses list
        if not any ( instruction.name == name for instruction in self.listAllInstructions ) :
            #
            # initialize the new instruction
            self.addInstruction ( name )
        #
        # obtain the right instruction
        instruction: Instruction = [ obj for obj in self.listAllInstructions if obj.name == name ] [ 0 ]
        #
        # insert the new measurement in the right instruction
        self.listAllInstructions [ self.listAllInstructions.index ( instruction ) ].addMeasurement ( duration , success )
    
    # function used to get analyses of a specific instruction
    def getInstruction ( self , name: str ) -> Instruction :
        #
        # obtain the right instruction
        instruction: Instruction = [ obj for obj in self.listAllInstructions if obj.name == name ] [ 0 ]
        #
        # return the instruction
        return instruction
    
    # function used to print the analyses of statistics of each instruction
    def __str__ ( self ) -> str :
        #
        # variable to store the output
        output: str = ""
        #
        # print debug row of analysis of each instruction
        output: str = f"{output}\nANALYSIS OF ALL INSTRUCTIONS\n"
        #
        # for each instruction
        for instruction in self.listAllInstructions :
            #
            # print the analyses of actual instruction
            output: str = f"{output}{instruction}"
        #
        # return the output
        return output

if __name__ == "__main__" :
    d = Analyses ( )
    d.addMeasurement ( "NameInstruction" , 1 , True )
    d.addMeasurement ( "NameInstruction" , 2 , False )
    d.addMeasurement ( "NameInstruction" , 3 , True )
    d.addMeasurement ( "NameInstruction" , 4 , False )
    d.addMeasurement ( "NameInstruction" , 5 , False )
    d.addMeasurement ( "NameInstruction" , 6 , False )
    print ( d )
