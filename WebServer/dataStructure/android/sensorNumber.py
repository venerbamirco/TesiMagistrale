"""
LIST OF ALL SENSOR RECORDS

	Sensor record
		Azimuth value: 1
		Pitch value: 2
		Roll value: 3
		Start timestamp: 1
		Finish timestamp: 12

	Sensor record
		Azimuth value: 4
		Pitch value: 5
		Roll value: 6
		Start timestamp: 13
"""

# class used to manage the single record of sensor
class SensorRecord :
    
    # constructor to initialize the single record of sensor
    def __init__ ( self , azimuth: int , pitch: int , roll: int , startTimestamp: int ) -> None :
        #
        # save azimuth value
        self.azimuth: int = azimuth
        #
        # save pitch value
        self.pitch: int = pitch
        #
        # save roll value
        self.roll: int = roll
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
    
    # function used to get the duration of actual sensor record
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
    
    # function used to print a sensor record
    def __str__ ( self ) -> str :
        #
        # variable to store the output
        output: str = "\n\tSensor record\n"
        #
        # add azimuth value
        output: str = f"{output}\t\tAzimuth value: {self.azimuth}\n"
        #
        # add pitch value
        output: str = f"{output}\t\tPitch value: {self.pitch}\n"
        #
        # add roll value
        output: str = f"{output}\t\tRoll value: {self.roll}\n"
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

# class used to manage sensor records
class SensorNumber :
    
    # constructor to initialize the object for the sensor
    def __init__ ( self ) -> None :
        #
        # create an empty list of sensor records
        self.listSensorRecord: list [ SensorRecord ] = list ( )
    
    # function used to add a new sensor record
    def addSensorRecord ( self , azimuth: int , pitch: int , roll: int , startTimestamp: int ) -> None :
        #
        # if there are other records of sensor
        if self.listSensorRecord :
            #
            # finish the last old sensor record
            self.listSensorRecord [ -1 ].finishRecord ( startTimestamp )
        #
        # create a new record of sensor
        sensorRecord: SensorRecord = SensorRecord ( azimuth , pitch , roll , startTimestamp )
        #
        # add the new record in the list
        self.listSensorRecord.append ( sensorRecord )
    
    # function used to get a specific sensor record using the timestamp
    def getSensorRecord ( self , timestamp: int ) -> SensorRecord :
        #
        # get the list of records that the timestamp is included in the range of timestamps
        listSensorRecords: list ( SensorRecord ) = list ( obj for obj in self.listSensorRecord if obj.startTimestamp <= timestamp )
        #
        # if the list is not empty
        if listSensorRecords :
            #
            # return the last element
            return listSensorRecords [ -1 ]
        #
        # return none because there are no elements in the list
        return None
    
    # function used to print a sensor object
    def __str__ ( self ) -> str :
        #
        # initialize as empty the output string
        output: str = ""
        #
        # print debug row of all sensor records
        output: str = f"{output}\nLIST OF ALL SENSOR NUMBER RECORDS\n"
        #
        # for each sensor record
        for sensorRecord in self.listSensorRecord :
            #
            # print the actual sensor record
            output: str = f"{output}{sensorRecord}"
        #
        # return the output
        return output

if __name__ == "__main__" :
    d = SensorNumber ( )
    d.addSensorRecord ( 1,2,3 , 1 )
    d.addSensorRecord ( 4,5,6 , 13 )
    print ( d )
