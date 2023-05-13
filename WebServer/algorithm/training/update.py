from algorithm.dataStructure.ptracer.analyses import Analyses
from algorithm.dataStructure.ptracer.sequences import Sequences

# class used to recover all check data
class Update :
    
    # constructor to initialize the recover object
    def __init__ ( self , analyses: Analyses , sequences: Sequences ) -> None :
        #
        # save the reference for analyses manager
        self.analyses: Analyses = analyses
        #
        # save the reference for sequences manager
        self.sequences: Sequences = sequences
        #
        # file used for instructions analyses
        # self.fileInstruction: File = File ( os.path.abspath ( "./logs/training/ptracer/Analyses.log" ) , "w" )
        #
        # file used for instructions analyses
        # self.fileSequences: File = File ( os.path.abspath ( "./logs/training/ptracer/Sequences.log" ) , "w" )
    
    # function used to update sequences training file data
    def updateSequencesTrainingData ( self ) :
        #
        # save sequences
        # self.fileSequences.writeIntoFile ( str ( self.sequences ) )
        pass
    
    # function used to update analyses training file data
    def updateAnalysesTrainingData ( self ) :
        #
        # save analyses
        # self.fileInstruction.writeIntoFile ( str ( self.analyses ) )
        pass
