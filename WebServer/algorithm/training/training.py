from algorithm.dataStructure.device.devices import Devices
from algorithm.dataStructure.ptracer.analyses import Analyses
from algorithm.dataStructure.ptracer.instructionsLists import InstructionsLists
from algorithm.dataStructure.ptracer.sequences import Sequences
from algorithm.training.recover import Recover
from algorithm.training.update import Update

class Training :
    
    def __init__ ( self ) -> None :
        #
        # training analyses data
        self.analyses: Analyses = Analyses ( )
        #
        # training sequences data
        self.sequences: Sequences = Sequences ( )
        #
        # training instructions lists data
        self.instructionsLists: InstructionsLists = InstructionsLists ( )
        #
        # training devices data
        self.devices: Devices = Devices ( )
        #
        # object used to load all check data
        self.recover: Recover = Recover ( self.analyses , self.sequences , self.devices , self.instructionsLists )
        #
        # object used to update training data
        self.update: Update = Update ( self.analyses , self.sequences )
