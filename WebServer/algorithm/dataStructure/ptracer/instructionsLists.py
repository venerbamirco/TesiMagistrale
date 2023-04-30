"""
LIST OF ALL EXECUTION PATHS

		['ciao']

		['sfdsfdsf', 'ciadfsdfsdfdsfo']
"""

# class to manage the structure of a single instruction
class InstructionRecord :
    
    # constructor to initialize an instruction
    def __init__ ( self , name: str ) -> None :
        #
        # save the name of the instruction
        self.name: str = name
    
    # function used to print an instruction object
    def __str__ ( self ) -> str :
        #
        # variable to store the output
        output: str = "\n\tInstruction\n"
        #
        # add name
        output: str = f"{output}\t\tName: {self.name}\n"
        #
        # return the output
        return output

# class used for instructions lists
class InstructionsLists :
    
    # constructor to initialize the instructions lists
    def __init__ ( self ) :
        #
        # instructions lists
        self.instructionsList: list [ list [ str ] ] = list ( )
    
    # function used to append a new list of instructions
    def appendNewListInstructions ( self ) :
        #
        # create a new list in the last position
        self.instructionsList.append ( list ( ) )
    
    # function used to append an element to the last list
    def appendElementLastList ( self , element: str ) :
        #
        # append actual element in the last list
        self.instructionsList [ -1 ].append ( element )
    
    # function used to print instructions lists
    def __str__ ( self ) -> str :
        #
        # variable to store the output
        output: str = f"\nLIST OF ALL EXECUTION PATHS\n"
        #
        # counter
        cont: int = 1
        #
        # for each sequence
        for instructionList in self.instructionsList :
            #
            # add to output actual list
            output: str = f"{output}\n\t{instructionList}\n"
            #
            # increment counter
            cont: int = cont + 1
        #
        # return the output
        return output

if __name__ == "__main__" :
    i = InstructionsLists ( )
    i.appendNewListInstructions ( )
    i.appendElementLastList ( "ciao" )
    i.appendNewListInstructions ( )
    i.appendElementLastList ( "sfdsfdsf" )
    i.appendElementLastList ( "ciadfsdfsdfdsfo" )
    print ( i )
