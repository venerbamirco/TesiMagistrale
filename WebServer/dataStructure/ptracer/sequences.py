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
class SequenceRecord :
    
    # constructor to initialize a single instruction
    def __init__ ( self , name: str ) -> None :
        #
        # save the name of the instruction
        self.name: str = name
        #
        # empty list of possible next instructions
        self.nextInstructions: list [ SequenceRecord ] = list ( )
    
    # function used to add an instruction
    def addNextInstruction ( self , name: str ) -> None :
        #
        # if there is not the next instruction in the list
        if not any ( instruction.name == name for instruction in self.nextInstructions ) :
            #
            # create a simple instruction object
            instruction: SequenceRecord = SequenceRecord ( name )
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
        self.listInstructions: list [ SequenceRecord ] = list ( )
        #
        # dictionary of list of instructions for each pair pid spid
        self.dictionaryPidSpid: dict [ list [ str ] ] = dict ( )
    
    # function used to insert a new instruction in the dictionary
    def addInstruction ( self , pid: int , spid: int , name: str ) -> None :
        #
        # if the pair pid spid is not in the dictionary
        if (pid , spid) not in self.dictionaryPidSpid :
            #
            # insert in the actual position an empty list
            self.dictionaryPidSpid [ pid , spid ]: list [ str ] = list ( )
        #
        # append in the right index the actual instruction
        self.dictionaryPidSpid [ pid , spid ].append ( name )
        #
        # if the instruction is not in the list
        if not any ( instruction.name == name for instruction in self.listInstructions ) :
            #
            # create a new instruction object with an empty list of next instructions
            instruction: SequenceRecord = SequenceRecord ( name )
            #
            # append the actual instruction in the list of all instructions
            self.listInstructions.append ( instruction )
            #
            # order instructions in the list
            self.listInstructions.sort ( key = lambda x : x.name )
        #
        # if there are other previous instructions of actual pid spid pair
        if len ( self.dictionaryPidSpid [ pid , spid ] ) > 1 :
            #
            # obtain the previous instruction
            previousInstruction: str = self.dictionaryPidSpid [ pid , spid ] [ -2 ]
            #
            # obtain the next instruction
            nextInstruction: str = self.dictionaryPidSpid [ pid , spid ] [ -1 ]
            #
            # obtain the object in the list for the previous instruction
            prev: SequenceRecord = [ obj for obj in self.listInstructions if obj.name == previousInstruction ] [ 0 ]
            #
            # add the next instruction in the actual instruction next instructions list
            prev.addNextInstruction ( nextInstruction )
    
    # function used to get a specific instruction
    def getInstruction ( self , name: str ) -> SequenceRecord :
        #
        # obtain the list of possible instructions
        instructionsList: list [ SequenceRecord ] = [ obj for obj in self.listInstructions if obj.name == name ]
        #
        # if there is one instruction
        if len ( instructionsList ) > 0 :
            #
            # return the first element
            return instructionsList [ 0 ]
        #
        # else if there are no instructions
        else :
            #
            # return None
            return None
    
    # function used to insert a new instruction in the analyses
    def insertInstruction ( self , name: str ) -> None :
        #
        # if instruction not in the list
        if not any ( instruction.name == name for instruction in self.listInstructions ) :
            #
            # create a new instruction object with an empty list of next instructions
            i: SequenceRecord = SequenceRecord ( name )
            #
            # append the actual instruction in the list of all instructions
            self.listInstructions.append ( i )
            #
            # order instructions in the list
            self.listInstructions.sort ( key = lambda x : x.name )
    
    # function used to insert a next instruction in the analyses
    def insertNextInstruction ( self , previousInstruction: str , nextInstruction: str ) -> None :
        #
        # if previous instruction not in the list
        if not any ( instruction.name == previousInstruction for instruction in self.listInstructions ) :
            #
            # add previous instruction in the list
            self.listInstructions.append ( SequenceRecord ( previousInstruction ) )
        #
        # if next instruction not in the list
        if not any ( instruction.name == nextInstruction for instruction in self.listInstructions ) :
            #
            # add nextInstruction instruction in the list
            self.listInstructions.append ( SequenceRecord ( nextInstruction ) )
        #
        # obtain the right instruction
        instruction: SequenceRecord = [ obj for obj in self.listInstructions if obj.name == previousInstruction ] [ 0 ]
        #
        # add the next instruction in the actual instruction list
        instruction.addNextInstruction ( nextInstruction )
        #
        # order instructions in the list
        self.listInstructions.sort ( key = lambda x : x.name )
    
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
    d.insertInstruction ( "Nome" )
    d.insertNextInstruction ( "Nome" , "nome1" )
    d.insertNextInstruction ( "Nome" , "nome2" )
    d.insertNextInstruction ( "nome2" , "nome3" )
    print ( d )
