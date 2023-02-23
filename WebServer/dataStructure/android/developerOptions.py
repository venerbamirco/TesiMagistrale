"""
LIST OF ALL DEVELOPER OPTIONS RECORDS

	Developer options record
		Developer options: True
		Android debug bridge: False
		Start timestamp: 1
		Finish timestamp: 12

	Developer options record
		Developer options: False
		Android debug bridge: False
		Start timestamp: 13
"""

# class used to manage the single record of development options
class DeveloperOptionsRecord :
    
    # constructor to initialize the single record of development options
    def __init__ ( self , developerOptionsEnabled: bool , androidDebugBridgeEnabled: bool , startTimestamp: int ) -> None :
        #
        # save if developer options are enabled
        self.developerOptionsEnabled: bool = developerOptionsEnabled
        #
        # save if the android debug bridge is enabled
        self.androidDebugBridgeEnabled: bool = androidDebugBridgeEnabled
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
    
    # function used to get the duration of actual developer options record
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
    
    # function used to print a developer option record
    def __str__ ( self ) -> str :
        #
        # variable to store the output
        output: str = "\n\tDeveloper options record\n"
        #
        # add if the developer options are enabled
        output: str = f"{output}\t\tDeveloper options: {self.developerOptionsEnabled}\n"
        #
        # add if the android debug bridge is enabled
        output: str = f"{output}\t\tAndroid debug bridge: {self.androidDebugBridgeEnabled}\n"
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

# class used to manage developer options and adb
class DeveloperOptions :
    
    # constructor to initialize the object for the development options
    def __init__ ( self ) -> None :
        #
        # create an empty list of developer option records
        self.listDeveloperOptions: list [ DeveloperOptionsRecord ] = list ( )
    
    # function used to add a new developer option record
    def addDeveloperOptionRecord ( self , developerOptionsEnabled: bool , androidDebugBridgeEnabled: bool , startTimestamp: int ) -> None :
        #
        # if there are other records of developer options
        if self.listDeveloperOptions :
            #
            # finish the last old developer option record
            self.listDeveloperOptions [ -1 ].finishRecord ( startTimestamp )
        #
        # create a new record of developer options
        developerOptionRecord: DeveloperOptionsRecord = DeveloperOptionsRecord ( developerOptionsEnabled , androidDebugBridgeEnabled , startTimestamp )
        #
        # add the new record in the list
        self.listDeveloperOptions.append ( developerOptionRecord )
    
    # function used to get a specific developer option record using the timestamp
    def getDeveloperOption ( self , timestamp: int ) -> DeveloperOptionsRecord :
        #
        # get the list of records that the timestamp is included in the range of timestamps
        listDeveloperOptionRecord: DeveloperOptionsRecord = [ obj for obj in self.listDeveloperOptions if obj.startTimestamp <= timestamp ]
        #
        # if the list is not empty
        if listDeveloperOptionRecord :
            #
            # return the last element
            return listDeveloperOptionRecord [ -1 ]
        #
        # return none because there are no elements in the list
        return None
    
    # function used to print a developer options object
    def __str__ ( self ) -> str :
        #
        # initialize as empty the output string
        output: str = ""
        #
        # print debug row of all developer options records
        output: str = f"{output}\nLIST OF ALL DEVELOPER OPTIONS RECORDS\n"
        #
        # for each developer options record
        for developerOptionsRecord in self.listDeveloperOptions :
            #
            # print the actual developer options record
            output: str = f"{output}{developerOptionsRecord}"
        #
        # return the output
        return output

if __name__ == "__main__" :
    d = DeveloperOptions ( )
    d.addDeveloperOptionRecord ( True , False , 1 )
    d.addDeveloperOptionRecord ( False , False , 13 )
    print ( d )
