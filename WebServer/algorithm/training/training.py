from algorithm.dataStructure.ptracer.analyses import Analyses
from algorithm.dataStructure.ptracer.sequences import Sequences
from algorithm.settings.settings import Settings
from algorithm.training.recover import Recover
from algorithm.training.update import Update

class Training :
    
    def __init__ ( self , settings: Settings ) :
        #
        # training analyses data
        self.analyses: Analyses = Analyses ( settings )
        #
        # training sequences data
        self.sequences: Sequences = Sequences ( settings )
        #
        # object used to load all check data
        self.recover: Recover = Recover ( self.analyses , self.sequences , settings )
        #
        # object used to update training data
        self.update: Update = Update ( self.analyses , self.sequences , settings )
