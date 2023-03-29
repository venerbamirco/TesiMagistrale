from algorithm.trainingAndCheck.android.checkDebuggers import CheckDebuggers
from algorithm.trainingAndCheck.ptracer.checkAnalyses import CheckAnalyses
from algorithm.trainingAndCheck.ptracer.checkSequences import CheckSequences
from algorithm.trainingAndCheck.recover import Recover

class Training :
    
    def __init__ ( self ) :
        #
        # initialize the analyses manager
        self.analysesTraining: CheckAnalyses = CheckAnalyses ( )
        #
        # initialize the sequences manager
        self.sequencesTraining: CheckSequences = CheckSequences ( )
        #
        # initialize the debugger manager
        self.debuggerCheck: CheckDebuggers = CheckDebuggers ( )
        #
        # object used to load all trainingAndCheck data
        self.recover: Recover = Recover ( self.analysesTraining , self.sequencesTraining )
