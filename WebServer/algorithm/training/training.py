from algorithm.training.ptracer.checkAnalyses import CheckAnalyses
from algorithm.training.ptracer.checkSequences import CheckSequences
from algorithm.training.recover import Recover

class Training :
    
    def __init__ ( self ) :
        #
        # initialize the analyses manager
        self.analysesTraining: CheckAnalyses = CheckAnalyses ( )
        #
        # initialize the sequences manager
        self.sequencesTraining: CheckSequences = CheckSequences ( )
        #
        # object used to load all training data
        self.recover: Recover = Recover ( self.analysesTraining , self.sequencesTraining )
