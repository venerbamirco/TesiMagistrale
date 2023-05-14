"""
ANALYSIS OF ALL INSTRUCTIONS

	Instruction
		Name: NameInstruction
		Minimum duration: 1
		Maximum duration: 6
		Average duration: 3.5
		Variance: 2.9166666666666665
		Number measurements: 6
		List measurements: [1, 2, 3, 4, 5, 6]
"""

from statistics import mean

from numpy import var

from algorithm.settings.settings import Settings

# class to manage the analyses for each instruction
class AnalysesRecord :
    
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
        # set as empty the list of measurements of durations
        self.listMeasurements: list [ int ] = list ( )
    
    # function used to insert a new measure for the actual instruction
    def addMeasurement ( self , duration: int ) -> None :
        #
        # if there are less than 1000
        if len(self.listMeasurements)<1000:
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
        self.listAllInstructions: list [ AnalysesRecord ] = list ( )
    
    # function used to insert a new instruction into analyses
    def addInstruction ( self , name: str ) -> None :
        #
        # if the instruction is not in the list
        if not any ( instruction.name == name for instruction in self.listAllInstructions ) :
            #
            # create a new instruction
            instruction: AnalysesRecord = AnalysesRecord ( name )
            #
            # append in the list the new instruction
            self.listAllInstructions.append ( instruction )
            #
            # order the list of all instructions
            self.listAllInstructions.sort ( key = lambda x : x.name )
    
    # function used to insert a new measurement for an instruction
    def addMeasurement ( self , name: str , duration: int ) -> None :
        #
        # if the instruction is not in the analyses list
        if not any ( instruction.name == name for instruction in self.listAllInstructions ) :
            #
            # initialize the new instruction
            self.addInstruction ( name )
        #
        # obtain the right instruction
        instruction: AnalysesRecord = [ obj for obj in self.listAllInstructions if obj.name == name ] [ 0 ]
        #
        # insert the new measurement in the right instruction
        instruction.addMeasurement ( duration )
    
    # function used to get analyses of a specific instruction
    def getInstruction ( self , name: str ) -> AnalysesRecord :
        #
        # obtain the list of possible instructions
        listInstructions: list [ AnalysesRecord ] = [ obj for obj in self.listAllInstructions if obj.name == name ]
        #
        # if there is at least one instruction
        if len ( listInstructions ) > 0 :
            #
            # get right instruction
            instruction: AnalysesRecord = [ obj for obj in self.listAllInstructions if obj.name == name ] [ 0 ]
            #
            # return the instruction
            return instruction
        #
        # else if there is no element
        else :
            #
            # return none
            return None
    
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
    
    # function used to check actual duration
    def checkDurationActualInstruction ( self , actualInstruction: str , actualDuration: int ) -> bool :
        #
        # obtain the right instruction
        instruction: AnalysesRecord = self.getInstruction ( actualInstruction )
        #
        # if there is an instruction
        if instruction is not None :
            #
            # if training mode enabled
            if Settings.training :
                #
                # if shorter duration
                if actualDuration < instruction.minimumMeasure :
                    #
                    # if we can show new duration
                    if Settings.newDurationInstruction :
                        #
                        # new minimum duration actual instruction
                        print ( "\n" + actualInstruction + " has new minimum duration: " + str ( actualDuration ) + " vs " +
                                str ( instruction.minimumMeasure ) + "->" + str ( instruction.maximumMeasure ) )
                    #
                    # add measure of actual instruction
                    self.addMeasurement ( actualInstruction , actualDuration )
                #
                # if longer duration
                elif actualDuration > instruction.maximumMeasure :
                    #
                    # if we can show new duration
                    if Settings.newDurationInstruction :
                        #
                        # new minimum duration actual instruction
                        print ( "\n" + actualInstruction + " has new maximum duration: " + str ( actualDuration ) + " vs " +
                                str ( instruction.minimumMeasure ) + "->" + str ( instruction.maximumMeasure ) )
                    #
                    # add measure of actual instruction
                    self.addMeasurement ( actualInstruction , actualDuration )
                    #
                    # return false because much time
                    return False
                #
                # else normal duration
                else :
                    #
                    # add measure of actual instruction
                    self.addMeasurement ( actualInstruction , actualDuration )
            #
            # else if not training mode
            else :
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
                    # if we can show new duration
                    if Settings.newDurationInstruction :
                        #
                        # print detail about longer duration
                        print ( "\n" + actualInstruction + " has longer duration: " + str ( actualDuration ) + " vs " +
                                str ( instruction.minimumMeasure ) + "->" + str ( instruction.maximumMeasure ) )
                    #
                    # return false because much time
                    return False
        #
        # else if the instruction is not mapped
        else :
            #
            # if training mode enabled
            if Settings.training :
                #
                # map actual instruction
                self.addInstruction ( actualInstruction )
                #
                # add measure of actual instruction
                self.addMeasurement ( actualInstruction , actualDuration )
                #
                # if we can show new duration
                if Settings.newDurationInstruction :
                    #
                    # instruction not mapped
                    print ( "\n" + actualInstruction + " has longer duration: " + str ( actualDuration ) + ", now is mapped" )
            #
            # if not training mode
            else :
                #
                # instruction not mapped
                print ( "\n" + actualInstruction + " not mapped" )
        #
        # return True because perfect time duration
        return True

if __name__ == "__main__" :
    d = Analyses ( )
    d.addMeasurement ( "NameInstruction" , 1 )
    d.addMeasurement ( "NameInstruction" , 2 )
    d.addMeasurement ( "NameInstruction" , 3 )
    d.addMeasurement ( "NameInstruction" , 4 )
    d.addMeasurement ( "NameInstruction" , 5 )
    d.addMeasurement ( "NameInstruction" , 6 )
    print ( d )
