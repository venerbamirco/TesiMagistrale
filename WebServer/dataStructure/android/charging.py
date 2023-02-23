"""
LIST OF ALL CHARGING RECORDS

	Charging record
		Is charging: True
		Usb charging: False
		Ac charging: True
		Start timestamp: 1
		Finish timestamp: 12

	Charging record
		Is charging: False
		Usb charging: False
		Ac charging: False
		Start timestamp: 13
"""

# class used to manage the single record of charging
class ChargingRecord :
    
    # constructor to initialize the single record of charging
    def __init__ ( self , isCharging: bool , usbCharging: bool , acCharging: bool , startTimestamp: int ) -> None :
        #
        # save if it is charging
        self.isCharging: bool = isCharging
        #
        # save if it is charging using usb
        self.usbCharging: bool = usbCharging
        #
        # save if it is charging using ac
        self.acCharging: bool = acCharging
        #
        # save the start timestamp
        self.startTimestamp: int = startTimestamp
        #
        # finish timestamp not defined at this moment
        self.finishTimestamp: int = None
    
    # function used to finish this record
    def finishRecord ( self , finishTimestamp: int ) -> None :
        #
        # remove 1 because in this timestamp start a new record
        rightFinishTimestamp: int = finishTimestamp - 1
        #
        # set the finish timestamp of this record
        self.finishTimestamp: int = rightFinishTimestamp
    
    # function used to get the duration of charging record
    def getDuration ( self ) -> int :
        #
        # if it is possible to calculate the duration
        if self.finishTimestamp :
            #
            # return the duration in milliseconds
            return self.finishTimestamp - self.startTimestamp
        #
        # else if the range is not finished
        else :
            #
            # return a zero duration
            return 0
    
    # function used to print a charging record
    def __str__ ( self ) -> str :
        #
        # variable to store the output
        output: str = "\n\tCharging record\n"
        #
        # add if it is charging
        output: str = f"{output}\t\tIs charging: {self.isCharging}\n"
        #
        # add if it is charging using usb
        output: str = f"{output}\t\tUsb charging: {self.usbCharging}\n"
        #
        # add if it is charging using ac
        output: str = f"{output}\t\tAc charging: {self.acCharging}\n"
        #
        # add the start timestamp
        output: str = f"{output}\t\tStart timestamp: {self.startTimestamp}\n"
        #
        # if it has also the finished timestamp
        if self.finishTimestamp :
            #
            # add the finish timestamp
            output: str = f"{output}\t\tFinish timestamp: {self.finishTimestamp}\n"
        #
        # return the output
        return output

# class used to manage charging records
class Charging :
    
    # constructor to initialize the object for charging management
    def __init__ ( self ) -> None :
        #
        # create an empty list of charging records
        self.listChargingRecords: list [ ChargingRecord ] = list ( )
    
    # function used to add a new charging record
    def addChargingRecord ( self , isCharging: bool , usbCharging: bool , acCharging: bool , startTimestamp: int ) -> None :
        #
        # if there are other charging records
        if self.listChargingRecords :
            #
            # finish the last old charging record
            self.listChargingRecords [ -1 ].finishRecord ( startTimestamp )
        #
        # create a new record of charging
        chargingRecord: ChargingRecord = ChargingRecord ( isCharging , usbCharging , acCharging , startTimestamp )
        #
        # add the new record in the list
        self.listChargingRecords.append ( chargingRecord )
    
    # function used to get a specific charging record using the timestamp
    def getCharging ( self , timestamp: int ) -> ChargingRecord :
        #
        # get the list of records that the timestamp is included in the range of timestamps
        listChargingRecords: ChargingRecord = [ obj for obj in self.listChargingRecords if obj.startTimestamp <= timestamp ]
        #
        # if the list is not empty
        if listChargingRecords :
            #
            # return the last element
            return listChargingRecords [ -1 ]
        #
        # return none because there are no elements in the list
        return None
    
    # function used to print a charging object
    def __str__ ( self ) -> str :
        #
        # initialize as empty the output string
        output: str = ""
        #
        # print debug row of all charging records
        output: str = f"{output}\nLIST OF ALL CHARGING RECORDS\n"
        #
        # for each charging record
        for chargingRecord in self.listChargingRecords :
            #
            # print the charging record
            output: str = f"{output}{chargingRecord}"
        #
        # return the output
        return output

if __name__ == "__main__" :
    d = Charging ( )
    d.addChargingRecord ( True , False , True , 1 )
    d.addChargingRecord ( False , False, False , 13 )
    print ( d )
