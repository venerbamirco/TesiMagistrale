"""
Dictionary of syscall where each syscall has a list of all possible syscall

syscall
		syscall1
		syscall2
syscall1
		syscall2
syscall2
"""

# class to manage sequence of instructions
class Sequence :
    
    # constructor to initialize the structure for sequences
    def __init__ ( self ) -> None :
        #
        # create an empty dictionary
        self.dictionary: dict = dict ( )
    
    # function used to insert a new instruction in the dictionary
    def insertNewInstruction ( self , syscall: str ) -> None :
        #
        # if the syscall is not in the dictionary
        if syscall not in self.dictionary.keys ( ) :
            #
            # initialize as empty list the sequences of actual syscall
            self.dictionary [ syscall ]: list = [ ]
    
    # function used to insert a new element in a certain key
    def insertNewSequence ( self , previousSyscall: str , nextSyscall: str ) -> None :
        #
        # if the previous instruction is not in dictionary
        if previousSyscall not in self.dictionary.keys ( ) :
            #
            # insert a new instruction in the dictionary for the previous instruction
            self.insertNewInstruction ( previousSyscall )
            #
            # insert the sequence
            self.insertNewSequence ( previousSyscall , nextSyscall )
        
        #
        # if the next instruction is not in dictionary
        elif nextSyscall not in self.dictionary.keys ( ) :
            #
            # insert a new instruction in the dictionary for the next instruction
            self.insertNewInstruction ( nextSyscall )
            #
            # insert the sequence
            self.insertNewSequence ( previousSyscall , nextSyscall )
        #
        # if key in dictionary
        else :
            #
            # append the next instruction in the actual instruction
            self.dictionary.get ( previousSyscall ).append ( nextSyscall )
    
    # function used to get the sequences of a particular instruction
    def getDictionaryOfInstruction ( self , syscall: str ) -> dict :
        #
        # return the dictionary of that syscall
        return self.dictionary [ syscall ]
    
    # function used to get the whole dictionary
    def getDictionary ( self ) -> dict :
        #
        # return the dictionary
        return self.dictionary
    
    # function used to print the dictionary of sequences of each instruction
    def __str__ ( self ) -> str :
        #
        # variable to store the output
        output: str = ""
        #
        # for each instruction
        for syscall in self.dictionary.keys ( ) :
            #
            # print the actual key
            output += f"{syscall}\n"
            #
            # for each next syscall of actual instruction
            for nextSyscall in self.dictionary [ syscall ] :
                #
                # print next syscall
                output += f"\t\t{nextSyscall}\n"
        #
        # return the output
        return output

if __name__ == "__main__" :
    d = Sequence ( )
    d.insertNewSequence ( "syscall" , "syscall1" )
    d.insertNewSequence ( "syscall" , "syscall2" )
    d.insertNewSequence ( "syscall1" , "syscall2" )
    print ( d )
