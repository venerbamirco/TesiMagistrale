"""
LIST OF ALL SEQUENCES FOR EACH SYSCALL
	Syscall
		Name: namesyscall
		Next:['namesyscall1', 'namesyscall2']
	Syscall
		Name: namesyscall1
		Next:['namesyscall2']
	Syscall
		Name: namesyscall2
		Next:[]
"""

# class to manage sequence of instructions
class Sequences :
    
    # constructor to initialize the structure for sequences
    def __init__ ( self ) -> None :
        #
        # create an empty dictionary
        self.dictionary: dict [ list [ str ] ] = dict ( )
    
    # function used to insert a new instruction in the dictionary
    def insertNewInstruction ( self , syscall: str ) -> None :
        #
        # if the syscall is not in the dictionary
        if syscall not in self.dictionary.keys ( ) :
            #
            # initialize as empty list the sequences of actual syscall
            self.dictionary [ syscall ]: list [ str ] = [ ]
    
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
        # if all syscall are in dictionary
        else :
            #
            # append the next instruction in the actual instruction
            self.dictionary.get ( previousSyscall ).append ( nextSyscall )
    
    # function used to get the sequences of a particular instruction
    def getSequencesOfInstruction ( self , syscall: str ) -> list [ str ] :
        #
        # return the dictionary of that syscall
        return self.dictionary [ syscall ]
    
    # function used to get the whole dictionary
    def getDictionary ( self ) -> dict [ list [ str ] ] :
        #
        # return the dictionary
        return self.dictionary
    
    # function used to print the dictionary of sequences of each instruction
    def __str__ ( self ) -> str :
        #
        # variable to store the output
        output: str = ""
        #
        # print debug row of sequences for each syscall
        output: str = f"{output}\nLIST OF ALL SEQUENCES FOR EACH SYSCALL\n"
        #
        # for each instruction
        for syscall in self.dictionary.keys ( ) :
            #
            # print debug row for another syscall fragment
            output: str = f"{output}\tSyscall\n"
            #
            # print the actual key
            output: str = f"{output}\t\tName: {syscall}\n"
            #
            # print next possible syscall
            output: str = f"{output}\t\tNext:{self.dictionary [ syscall ]}\n"
        #
        # return the output
        return output

if __name__ == "__main__" :
    d = Sequences ( )
    d.insertNewSequence ( "namesyscall" , "namesyscall1" )
    d.insertNewSequence ( "namesyscall" , "namesyscall2" )
    d.insertNewSequence ( "namesyscall1" , "namesyscall2" )
    print ( d )
