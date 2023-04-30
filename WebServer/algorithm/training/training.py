from algorithm.dataStructure.device.devices import Devices
from algorithm.dataStructure.ptracer.analyses import Analyses
from algorithm.dataStructure.ptracer.instructionsLists import InstructionsLists
from algorithm.dataStructure.ptracer.sequences import Sequences
from algorithm.settings.settings import Settings
from algorithm.training.recover import Recover
from algorithm.training.update import Update

class Training :
    
    def __init__ ( self , settings: Settings ) -> None :
        #
        # training analyses data
        self.analyses: Analyses = Analyses ( settings )
        #
        # training sequences data
        self.sequences: Sequences = Sequences ( settings )
        #
        # training instructions lists data
        self.instructionsLists: InstructionsLists = InstructionsLists ( )
        #
        # training devices data
        self.devices: Devices = Devices ( settings )
        #
        # object used to load all check data
        self.recover: Recover = Recover ( self.analyses , self.sequences , self.devices , self.instructionsLists , settings )
        #
        # object used to update training data
        self.update: Update = Update ( self.analyses , self.sequences , settings )
