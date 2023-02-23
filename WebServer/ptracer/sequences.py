"""
LIST OF ALL SEQUENCES FOR EACH INSTRUCTION

	Instruction
		Name: nameinstruction
		Next: [nameinstruction1, nameinstruction2]

	Instruction
		Name: nameinstruction1
		Next: [nameinstruction2]

	Instruction
		Name: nameinstruction2
		Next: []
"""

# class to manage the single instruction
class Instruction :
    
    # constructor to initialize a single instruction
    def __init__ ( self , name: str ) -> None :
        #
        # save the name of the instruction
        self.name: str = name
        #
        # empty list of possible next instructions
        self.nextInstructions: list [ Instruction ] = list ( )
    
    # function used to add an instruction
    def addNextInstruction ( self , name: str ) -> None :
        #
        # create a simple instruction object
        instruction: Instruction = Instruction ( name )
        #
        # append the instruction in the list of possible instructions
        self.nextInstructions.append ( instruction )
        #
        # order the list of next instructions
        self.nextInstructions.sort ( key = lambda x : x.name )
    
    # function used to represent the object with only the name
    def __repr__ ( self ) -> str :
        #
        # return only the name
        return f"{self.name}"
    
    # function used to print the instruction object
    def __str__ ( self ) -> str :
        #
        # variable to store the output
        output: str = "\n\tInstruction\n"
        #
        # add the name
        output: str = f"{output}\t\tName: {self.name}\n"
        #
        # add the next possible instructions
        output: str = f"{output}\t\tNext: {self.nextInstructions}\n"
        #
        # return the output
        return output

# class to manage sequence of instructions
class Sequences :
    
    # constructor to initialize the structure for sequences
    def __init__ ( self ) -> None :
        #
        # create a list of all instructions
        self.listInstructions: list [ Instruction ] = list ( )
    
    # function used to insert a new instruction in the dictionary
    def addInstruction ( self , name: str ) -> None :
        #
        # if the instruction is not in the list
        if not any ( instruction.name == name for instruction in self.listInstructions ) :
            #
            # create a new instruction object with an empty list of next instructions
            instruction: Instruction = Instruction ( name )
            #
            # append the actual instruction in the list of all instructions
            self.listInstructions.append ( instruction )
            #
            # order instructions in the list
            self.listInstructions.sort ( key = lambda x : x.name )
    
    # function used to insert a next instruction for a specific instruction
    def addNextInstruction ( self , previousInstruction: str , nextInstruction: str ) -> None :
        #
        # if the previous instruction is not in dictionary
        if not any ( instruction.name == previousInstruction for instruction in self.listInstructions ) :
            #
            # insert a new instruction in the dictionary for the previous instruction
            self.addInstruction ( previousInstruction )
        #
        # if the next instruction is not in dictionary
        elif not any ( instruction.name == nextInstruction for instruction in self.listInstructions ) :
            #
            # insert a new instruction in the dictionary for the next instruction
            self.addInstruction ( nextInstruction )
        #
        # obtain the object in the list for the previous instruction
        prevInstruction:Instruction = [ obj for obj in self.listInstructions if obj.name == previousInstruction ] [ 0 ]
        #
        # add the next instruction in the actual instruction next instructions list
        self.listInstructions [ self.listInstructions.index ( prevInstruction ) ].addNextInstruction ( nextInstruction )
    
    # function used to get a specific instruction
    def getInstruction ( self , name: str ) -> Instruction :
        #
        # obtain the right instruction
        instruction: Instruction = [ obj for obj in self.listInstructions if obj.name == name ] [ 0 ]
        #
        # return the specific instruction
        return instruction
    
    # function used to print the dictionary of sequences of each instruction
    def __str__ ( self ) -> str :
        #
        # variable to store the output
        output: str = ""
        #
        # print debug row of sequences for each instruction
        output: str = f"{output}\nLIST OF ALL SEQUENCES FOR EACH INSTRUCTION\n"
        #
        # for each instruction
        for instruction in self.listInstructions :
            #
            # print debug row for another instruction fragment
            output: str = f"{output}{instruction}"
        #
        # return the output
        return output

if __name__ == "__main__" :
    d = Sequences ( )
    d.addNextInstruction ( "nameinstruction" , "nameinstruction2" )
    d.addNextInstruction ( "nameinstruction" , "nameinstruction1" )
    d.addNextInstruction ( "nameinstruction1" , "nameinstruction2" )
    print ( d )
