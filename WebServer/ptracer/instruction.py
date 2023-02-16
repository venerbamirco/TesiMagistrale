from ptracer.instruction import Instruction

# class to create the structure for the single instruction
class Instruction :
    
    # constructor to initialize the object for the instruction
    def __init__ ( self , syscall , pid , spid , start_timestamp ) -> None :
        #
        # reference to the previous instruction
        self.previous_instruction = None
        #
        # reference to the next instruction
        self.next_instruction = None
        #
        # save the name of the ptracer
        self.syscall = syscall
        #
        # save the pid
        self.pid = pid
        #
        # save the spid
        self.spid = spid
        #
        # save the start_timestamp
        self.start_timestamp = start_timestamp
        #
        # finish timestamp not defined in this moment
        self.finish_timestamp = None
        #
        # variable used to check if the actual instruction is finished
        self.finished = False
    
    def set_finish_timestamp ( self , finish_timestamp ) -> None :
        #
        # the instruction is finished
        self.finished = True
        #
        # save the finish timestamp
        self.finish_timestamp = finish_timestamp
    
    # function used to get the duration of actual instruction
    def get_duration_instruction ( self ) -> int :
        #
        # if the instruction is finished
        if self.finished :
            #
            # return the duration in milliseconds
            return self.finish_timestamp - self.start_timestamp
        #
        # else if the instruction is not finished
        else :
            #
            # return a zero duration
            return 0
    
    # function used to set the reference of the previous instruction
    def set_previous_instruction ( self , previous_instruction: Instruction ) :
        #
        # set the reference for the previous instruction
        self.previous_instruction = previous_instruction
    
    # function used to set the reference of the next instruction
    def set_next_instruction ( self , next_instruction: Instruction ) :
        #
        # set the reference for the next instruction
        self.next_instruction = next_instruction
