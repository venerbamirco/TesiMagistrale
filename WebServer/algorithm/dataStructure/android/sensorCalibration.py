"""
LIST OF ALL CALIBRATION RECORDS

	Calibration record
		Calibrated: True
		Timestamp: 1

	Calibration record
		Calibrated: True
		Timestamp: 13
"""

# class used to manage the single record of calibration
class CalibrationRecord :
    
    # constructor to initialize the single record of calibration
    def __init__ ( self , calibration: bool , timestamp: int ) -> None :
        #
        # save if calibrated
        self.calibration: bool = calibration
        #
        # save the timestamp
        self.timestamp: int = timestamp
    
    # function used to print a calibration record
    def __str__ ( self ) -> str :
        #
        # variable to store the output
        output: str = "\n\tCalibration record\n"
        #
        # add if it is charging
        output: str = f"{output}\t\tCalibrated: {self.calibration}\n"
        #
        # add the timestamp
        output: str = f"{output}\t\tTimestamp: {self.timestamp}\n"
        #
        # return the output
        return output

# class used to manage calibration records
class SensorCalibration :
    
    # constructor to initialize the object for calibration management
    def __init__ ( self ) -> None :
        #
        # create an empty list of calibration records
        self.listCalibrationRecords: list [ CalibrationRecord ] = list ( )
    
    # function used to add a new calibration record
    def addCalibrationRecord ( self , calibration: bool , timestamp: int ) -> None :
        #
        # create a new record of calibration
        calibrationRecord: CalibrationRecord = CalibrationRecord ( calibration , timestamp )
        #
        # add the new record in the list
        self.listCalibrationRecords.append ( calibrationRecord )
    
    # function used to get a specific calibration record using the timestamp
    def getCalibration ( self , timestamp: int ) -> CalibrationRecord :
        #
        # get the list of records that the timestamp is included in the range of timestamps
        listCalibrationRecords: list [ CalibrationRecord ] = list ( obj for obj in self.listCalibrationRecords if obj.startTimestamp <= timestamp )
        #
        # if the list is not empty
        if listCalibrationRecords :
            #
            # return the last element
            return listCalibrationRecords [ -1 ]
        #
        # return none because there are no elements in the list
        return None
    
    # function used to print a calibration object
    def __str__ ( self ) -> str :
        #
        # initialize as empty the output string
        output: str = ""
        #
        # print debug row of all calibration records
        output: str = f"{output}\nLIST OF ALL CALIBRATION RECORDS\n"
        #
        # for each calibration record
        for calibrationRecord in self.listCalibrationRecords :
            #
            # print the calibration record
            output: str = f"{output}{calibrationRecord}"
        #
        # return the output
        return output

if __name__ == "__main__" :
    d = SensorCalibration ( )
    d.addCalibrationRecord ( True , 1 )
    d.addCalibrationRecord ( True, 13 )
    print ( d )
