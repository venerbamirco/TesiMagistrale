import os

from algorithm.dataStructure.other.file import File
from algorithm.dataStructure.ptracer.analyses import Analyses
from algorithm.dataStructure.ptracer.sequences import Sequences
from algorithm.device.devices import Devices
from algorithm.settings.settings import Settings

# class used to recover all check data
class Recover :
    
    # constructor to initialize the recover object
    def __init__ ( self , analyses: Analyses , sequences: Sequences , devices: Devices , settings: Settings ) -> None :
        #
        # save the reference for analyses manager
        self.analyses: Analyses = analyses
        #
        # save the reference for sequences manager
        self.sequences: Sequences = sequences
        #
        # save the reference for devices manager
        self.devices: Devices = devices
        #
        # file used for instructions analyses
        self.fileInstruction: File = File ( os.path.abspath ( "../../logs/training/ptracer/Analyses.log" ) , "r" )
        #
        # file used for instructions analyses
        self.fileSequences: File = File ( os.path.abspath ( "../../logs/training/ptracer/Sequences.log" ) , "r" )
        #
        # file used for devices analyses
        self.fileDevices: File = File ( os.path.abspath ( "../../logs/training/other/Devices.log" ) , "r" )
        #
        # recover of instruction analyses
        self.recoverInformationsInstruction ( )
        #
        # recover of sequences analyses
        self.recoverInformationsSequences ( )
        #
        # recover of devices
        self.recoverDevices ( )
    
    # function used to recover all informations about each instruction
    def recoverInformationsInstruction ( self ) -> None :
        #
        # name of last found instruction
        name: str = ""
        #
        # until the file is not finished
        while True :
            #
            # get next line from file
            line: str = self.fileInstruction.file.readline ( )
            #
            # if the end of file is reached
            if not line :
                #
                # break the loop
                break
            #
            # if actual row contains the name of instruction Name: clock_gettime
            if "Name" in line :
                #
                # save the actual name
                name: str = line.split ( ":" ) [ 1 ].strip ( )
                #
                # add the instruction in analyses of each instruction
                self.analyses.addInstruction ( line.split ( ":" ) [ 1 ].strip ( ) )
            #
            # else if actual row contains the list of measurements List measurements: [3718, 5542, 517, 721, 728]
            elif "List measurements" in line :
                #
                # get list of measurements
                listMeasurements: str = line.split ( ":" ) [ 1 ].strip ( " []\n" )
                #
                # for each measure
                for measure in listMeasurements.split ( "," ) :
                    #
                    # add the measure in analyses
                    self.analyses.addMeasurement ( name , int ( measure.strip ( ) ) )
    
    # function used to recover all informations about sequences
    def recoverInformationsSequences ( self ) -> None :
        #
        # name of last found instruction
        name: str = ""
        #
        # until the file is not finished
        while True :
            #
            # get next line from file
            line: str = self.fileSequences.file.readline ( )
            #
            # if the end of file is reached
            if not line :
                #
                # break the loop
                break
            #
            # if actual row contains the name of instruction Name: clock_gettime
            if "Name" in line :
                #
                # save the actual name
                name: str = line.split ( ":" ) [ 1 ].strip ( )
                #
                # add the instruction in analyses of each instruction
                self.sequences.insertInstruction ( line.split ( ":" ) [ 1 ].strip ( ) )
            #
            # else if actual row contains the list of measurements Next: [clock_gettime, epoll_ctl, futex]
            elif "Next" in line :
                #
                # get list of measurements
                listMeasurements: str = line.split ( ":" ) [ 1 ].strip ( " []\n" )
                #
                # for each measure
                for measure in listMeasurements.split ( "," ) :
                    #
                    # add the measure in analyses
                    self.sequences.insertNextInstruction ( name , measure.strip ( ) )
    
    # function used to recover all informations about devices
    def recoverDevices ( self ) -> None :
        #
        # flag for bad things
        badThings: bool = False
        #
        # ip address variable
        ipAddress: str = ""
        #
        # until the file is not finished
        while True :
            #
            # get next line from file
            line: str = self.fileDevices.file.readline ( )
            #
            # if the end of file is reached
            if not line :
                #
                # break the loop
                break
            # if start line of paragraph
            elif "LIST OF ALL" in line :
                #
                # do nothing
                pass
            # if security level
            elif "Security level" in line :
                #
                # do nothing
                pass
            #
            # if ip address in line
            elif "Ip address" in line :
                #
                # save the actual ip address
                ipAddress: str = line.split ( ":" ) [ 1 ].strip ( )
                #
                # add the device in the list
                self.devices.addDevice ( ipAddress )
            #
            # if good things in line
            elif "Good things" in line :
                #
                # flag bad things false
                badThings: bool = False
            #
            # if good things in line
            elif "Bad things" in line :
                #
                # flag bad things false
                badThings: bool = True
            #
            # else if it is a possible value
            elif not line.isspace ( ) :
                #
                # if bad things enabled
                if badThings :
                    self.devices.incrementLevelSecurity ( ipAddress , line.strip ( ) )

if __name__ == "__main__" :
    settings = Settings ( )
    analyses = Analyses ( settings )
    sequences = Sequences ( settings )
    devices = Devices ( settings )
    rec = Recover ( analyses , sequences , devices , settings )
    print ( str ( devices ) )
