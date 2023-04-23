"""
LIST OF ALL LIFECYCLE RECORDS

	Lifecycle record
		On resume: True
		On pause: False
		Start timestamp: 1
		Finish timestamp: 12

	Lifecycle record
		On resume: False
		On pause: True
		Start timestamp: 13
"""

# class used to manage the single record of lifecycle
class LifecycleRecord :
    
    # constructor to initialize the single record of lifecycle
    def __init__ ( self , onResume: bool , onPause: bool , startTimestamp: int ) -> None :
        #
        # save if it is on resume
        self.onResume: bool = onResume
        #
        # save if it is on pause
        self.onPause: bool = onPause
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
    
    # function used to get the duration of lifecycle record
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
    
    # function used to print a lifecycle record
    def __str__ ( self ) -> str :
        #
        # variable to store the output
        output: str = "\n\tLifecycle record\n"
        #
        # add if it is on resume
        output: str = f"{output}\t\tOn resume: {self.onResume}\n"
        #
        # add if it is on pause
        output: str = f"{output}\t\tOn pause: {self.onPause}\n"
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

# class used to manage lifecycle records
class Lifecycle :
    
    # constructor to initialize the object for lifecycle management
    def __init__ ( self ) -> None :
        #
        # create an empty list of lifecycle records
        self.listLifecycleRecords: list [ LifecycleRecord ] = list ( )
    
    # function used to add a new lifecycle record
    def addLifecycleRecord ( self , onResume: bool , onPause: bool , startTimestamp: int ) -> None :
        #
        # if there are other lifecycle records
        if self.listLifecycleRecords :
            #
            # finish the last old lifecycle record
            self.listLifecycleRecords [ -1 ].finishRecord ( startTimestamp )
        #
        # create a new record of lifecycle
        lifecycleRecord: LifecycleRecord = LifecycleRecord ( onResume , onPause , startTimestamp )
        #
        # add the new record in the list
        self.listLifecycleRecords.append ( lifecycleRecord )
    
    # function used to get a specific lifecycle record using the timestamp
    def getLifecycle ( self , timestamp: int ) -> LifecycleRecord :
        #
        # get the list of records that the timestamp is included in the range of timestamps
        listLifecycleRecords: list [ LifecycleRecord ] = list ( obj for obj in self.listLifecycleRecords if obj.startTimestamp <= timestamp )
        #
        # if the list is not empty
        if listLifecycleRecords :
            #
            # return the last element
            return listLifecycleRecords [ -1 ]
        #
        # return none because there are no elements in the list
        return None
    
    # function used to print a lifecycle object
    def __str__ ( self ) -> str :
        #
        # initialize as empty the output string
        output: str = ""
        #
        # print debug row of all charging records
        output: str = f"{output}\nLIST OF ALL LIFECYCLE RECORDS\n"
        #
        # for each lifecycle record
        for lifecycleRecord in self.listLifecycleRecords :
            #
            # print the lifecycle record
            output: str = f"{output}{lifecycleRecord}"
        #
        # return the output
        return output

if __name__ == "__main__" :
    d = Lifecycle ( )
    d.addLifecycleRecord ( True , False , 1 )
    d.addLifecycleRecord ( False , True , 13 )
    print ( d )
