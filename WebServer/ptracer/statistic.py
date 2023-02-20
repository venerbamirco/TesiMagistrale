"""
Dictionary of syscall, each instruction a dictionary

syscall
		Min_measure: 1
		Max_measure: 6
		Avg_measure: 3.5
		Variance: 2.9166666666666665
		Number_measurements: 6
		Good_terminations: 2
		Bad_terminations: 4
		List_measurements: [1, 2, 3, 4, 5, 6]
"""

from statistics import mean

from numpy import var

# class used to manage statistics of each instruction
class Statistic :
    
    # constructor to initialize the structure for statistics
    def __init__ ( self ) -> None :
        #
        # create an empty dictionary
        self.dictionary = dict ( )
    
    # function used to insert a new instruction into statistics
    def insertNewInstruction ( self , syscall: str ) -> None :
        #
        # if the syscall is not in the dictionary
        if syscall not in self.dictionary.keys ( ) :
            #
            # create an empty dictionary
            dictionary: dict = dict ( )
            #
            # insert all keys for a new instruction
            dictionary [ "Min_measure" ]: int = 0
            dictionary [ "Max_measure" ]: int = 0
            dictionary [ "Avg_measure" ]: int = 0
            dictionary [ "Variance" ]: int = 0
            dictionary [ "Number_measurements" ]: int = 0
            dictionary [ "Good_terminations" ]: int = 0
            dictionary [ "Bad_terminations" ]: int = 0
            dictionary [ "List_measurements" ]: list = list ( )
            #
            # initialize the entry of the new instruction
            self.dictionary [ syscall ]: dict = dictionary
    
    # function used to insert a new measurement for an instruction
    def addMeasurement ( self , syscall: str , duration: int , success: bool ) -> None :
        #
        # if the instruction is not in the dictionary
        if syscall not in self.dictionary.keys ( ) :
            #
            # initialize the new instruction
            self.insertNewInstruction ( syscall )
        #
        # increment the number of measurements
        self.dictionary [ syscall ] [ "Number_measurements" ]: int = self.dictionary [ syscall ] [ "Number_measurements" ] + 1
        #
        # add the new measure in the list
        self.dictionary [ syscall ] [ "List_measurements" ].append ( duration )
        #
        # update the min duration
        self.dictionary [ syscall ] [ "Min_measure" ] = min ( self.dictionary [ syscall ] [ "List_measurements" ] )
        #
        # update the max duration
        self.dictionary [ syscall ] [ "Max_measure" ] = max ( self.dictionary [ syscall ] [ "List_measurements" ] )
        #
        # update the avg duration
        self.dictionary [ syscall ] [ "Avg_measure" ] = mean ( self.dictionary [ syscall ] [ "List_measurements" ] )
        #
        # update the variance of durations
        self.dictionary [ syscall ] [ "Variance" ] = var ( self.dictionary [ syscall ] [ "List_measurements" ] )
        #
        # if the instruction is terminated in a good manner
        if success :
            #
            # increment the counter of good terminations
            self.dictionary [ syscall ] [ "Good_terminations" ] = self.dictionary [ syscall ] [ "Good_terminations" ] + 1
        #
        # if the instruction is terminated in a bad manner
        else :
            #
            # increment the counter of bad terminations
            self.dictionary [ syscall ] [ "Bad_terminations" ] = self.dictionary [ syscall ] [ "Bad_terminations" ] + 1
    
    # function used to get the statistics of a particular instruction
    def getDictionaryOfInstruction ( self , syscall: str ) -> dict :
        #
        # return the dictionary of that syscall
        return self.dictionary [ syscall ]
    
    # function used to get the whole dictionary
    def getDictionary ( self ) -> dict :
        #
        # return the dictionary
        return self.dictionary
    
    # function used to print the dictionary of statistics of each instruction
    def __str__ ( self ) -> str :
        #
        # variable to store the output
        output: str = ""
        #
        # for each instruction
        for instruction in self.dictionary.keys ( ) :
            #
            # print the actual instruction
            output += f"{instruction}\n"
            #
            # for each statistic of actual instruction
            for statistic in self.dictionary [ instruction ] :
                #
                # print actual element of the list
                output += f"\t\t{statistic}: {self.dictionary [ instruction ] [ statistic ]}\n"
        #
        # return the output
        return output

if __name__ == "__main__" :
    d = Statistic ( )
    d.addMeasurement ( "syscall" , 1 , True )
    d.addMeasurement ( "syscall" , 2 , False )
    d.addMeasurement ( "syscall" , 3 , True )
    d.addMeasurement ( "syscall" , 4 , False )
    d.addMeasurement ( "syscall" , 5 , False )
    d.addMeasurement ( "syscall" , 6 , False )
    print ( d )
