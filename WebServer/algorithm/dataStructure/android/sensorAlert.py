"""
LIST OF ALL CORRECTLY USED ALERTS

	Alert record
		Alert: True
		Start timestamp: 10
		Finish timestamp: 12

	Alert record
		Alert: False
		Start timestamp: 13

LIST OF ALL AZIMUTH ALERTS

	Alert record
		Alert: False
		Start timestamp: 10
		Finish timestamp: 12

	Alert record
		Alert: True
		Start timestamp: 13

LIST OF ALL PITCH ALERTS

	Alert record
		Alert: False
		Start timestamp: 10
		Finish timestamp: 14

	Alert record
		Alert: True
		Start timestamp: 15

LIST OF ALL ROLL ALERTS

	Alert record
		Alert: False
		Start timestamp: 10
"""

# class used to manage the single alert
class AlertRecord :
    
    # constructor to initialize the alert object
    def __init__ ( self , alert: bool , startTimestamp: int ) -> None :
        #
        # save the alert
        self.alert: bool = alert
        #
        # save the start timestamp
        self.startTimestamp: int = startTimestamp
        #
        # finish timestamp not defined at the moment
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
    
    # function used to represent the object with only the alert
    def __repr__ ( self ) -> str :
        #
        # return only the alert
        return f"{self.alert}"
    
    # function used to print a sensor record
    def __str__ ( self ) -> str :
        #
        # variable to store the output
        output: str = "\n\tAlert record\n"
        #
        # add if correctly used
        output: str = f"{output}\t\tAlert: {self.alert}\n"
        #
        # add start timestamp
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

# class used to manage the list of alert records
class SensorAlert :
    
    # constructor to initialize the list of alerts
    def __init__ ( self ) -> None :
        #
        # create  an empty list of azimuth alerts
        self.listAzimuthAlerts: list [ AlertRecord ] = list ( )
        #
        # create  an empty list of pitch alerts
        self.listPitchAlerts: list [ AlertRecord ] = list ( )
        #
        # create  an empty list of roll alerts
        self.listRollAlerts: list [ AlertRecord ] = list ( )
        #
        # create  an empty list of correctly used
        self.listCorrectlyUsed: list [ AlertRecord ] = list ( )
    
    # function used to add azimuth alert
    def addAlert ( self , listAlerts: list [ AlertRecord ] , actualAlert: bool , startTimeStamp: int , correctlyUsed: bool ) -> None :
        #
        # if the list is empty
        if not listAlerts :
            #
            # if it is a correctly used alert
            if correctlyUsed :
                #
                # create an initial element that is ok for correctly used list
                initialElement: AlertRecord = AlertRecord ( True , startTimeStamp )
                #
                # append in the list the initial element
                listAlerts.append ( initialElement )
                #
                # create an initial element for azimuth pitch and roll from the initial timestamp
                initialElementAzimuth: AlertRecord = AlertRecord ( False , startTimeStamp )
                initialElementPitch: AlertRecord = AlertRecord ( False , startTimeStamp )
                initialElementRoll: AlertRecord = AlertRecord ( False , startTimeStamp )
                #
                # append in azimuth pitch and roll list the initial element that is ok
                self.listAzimuthAlerts.append ( initialElementAzimuth )
                self.listPitchAlerts.append ( initialElementPitch )
                self.listRollAlerts.append ( initialElementRoll )
        #
        # if the list is not empty
        else :
            #
            # obtain the last element in the list
            lastAlert: AlertRecord = listAlerts [ -1 ]
            #
            # if the last element is the same of actual
            if lastAlert.alert == actualAlert :
                #
                # delete the finish timestamp of last element
                lastAlert.finishTimestamp: int = None
            #
            # if the last element is different from actual
            else :
                #
                # finish the last element
                lastAlert.finishRecord ( startTimeStamp )
                #
                # if the finish timestamp is smaller than start timestamp
                if lastAlert.finishTimestamp < lastAlert.startTimestamp :
                    #
                    # remove from the list the actual element
                    listAlerts.remove ( lastAlert )
                    #
                    # recall this function to add the new element
                    self.addAlert ( listAlerts , actualAlert , startTimeStamp , correctlyUsed )
                #
                # if the start timestamp is smaller than finish timestamp is ok
                else :
                    #
                    # create an actual alert with right startTimestamp
                    actualAlertRecord: AlertRecord = AlertRecord ( actualAlert , startTimeStamp )
                    #
                    # append in the list the new element
                    listAlerts.append ( actualAlertRecord )
    
    # function used to manage the addition of alert
    def manageAddAlert ( self , listAlerts: list [ AlertRecord ] , actualAlert: bool , startTimeStamp: int , correctlyUsed: bool ) -> None :
        #
        # add the actual alert in the relative list
        self.addAlert ( listAlerts , actualAlert , startTimeStamp , correctlyUsed )
        #
        # if azimuth pitch or roll alert
        if not correctlyUsed :
            #
            # if the actual alert is true
            if actualAlert :
                #
                # device not correctly used
                self.addAlert ( self.listCorrectlyUsed , False , startTimeStamp , True )
            #
            # if actual alert is false
            else :
                #
                # get list of actual start timestamp alerts
                listActualAlerts: list [ AlertRecord ] = self.getSensorRecord ( startTimeStamp )
                #
                # if in the actual moment there are no alerts
                if not listActualAlerts [ 1 ].alert and not listActualAlerts [ 2 ].alert and not listActualAlerts [ 3 ].alert :
                    #
                    # device correctly used
                    self.addAlert ( self.listCorrectlyUsed , True , startTimeStamp , True )
    
    # function used to add azimuth alert
    def addAzimuthAlert ( self , azimuthAlert: bool , startTimeStamp: int ) -> None :
        #
        # add the actual azimuth alert in the relative list
        self.manageAddAlert ( self.listAzimuthAlerts , azimuthAlert , startTimeStamp , False )
    
    # function used to add pitch alert
    def addPitchAlert ( self , pitchAlert: bool , startTimeStamp: int ) -> None :
        #
        # add the actual pitch alert in the relative list
        self.manageAddAlert ( self.listPitchAlerts , pitchAlert , startTimeStamp , False )
    
    # function used to add roll alert
    def addRollAlert ( self , rollAlert: bool , startTimeStamp: int ) -> None :
        #
        # add the actual roll alert in the relative list
        self.manageAddAlert ( self.listRollAlerts , rollAlert , startTimeStamp , False )
    
    # function used to add roll alert
    def addCorrectlyUsed ( self , correctlyUsed: bool , startTimeStamp: int ) -> None :
        #
        # add the actual correctly used alert in the relative list
        self.manageAddAlert ( self.listCorrectlyUsed , correctlyUsed , startTimeStamp , True )
        #
        # add that there are not azimuth pitch and roll alert
        self.addAzimuthAlert ( False , startTimeStamp )
        self.addPitchAlert ( False , startTimeStamp )
        self.addRollAlert ( False , startTimeStamp )
    
    # function used to get a specific sensor record using the timestamp
    def getSensorRecord ( self , timestamp: int ) -> list [ AlertRecord ] :
        #
        # create an empty list to contain 4 alerts [correctlyUsed, azimuthAlert, pitchAlert, rollAlert] of specific timestamp
        listSensorAlerts: list [ AlertRecord ] = list ( )
        #
        # get the list of azimuth alerts that the timestamp is included in the range of timestamps
        listAzimuthRecords: list [ AlertRecord ] = list ( obj for obj in self.listAzimuthAlerts if obj.startTimestamp <= timestamp )
        #
        # get the list of pitch alerts that the timestamp is included in the range of timestamps
        listPitchRecords: list [ AlertRecord ] = list ( obj for obj in self.listPitchAlerts if obj.startTimestamp <= timestamp )
        #
        # get the list of roll alerts that the timestamp is included in the range of timestamps
        listRollRecords: list [ AlertRecord ] = list ( obj for obj in self.listRollAlerts if obj.startTimestamp <= timestamp )
        #
        # get the list of correctly used alerts that the timestamp is included in the range of timestamps
        listCorrectlyUsedRecords: list [ AlertRecord ] = list ( obj for obj in self.listCorrectlyUsed if obj.startTimestamp <= timestamp )
        #
        # if all lists are not empty
        if listAzimuthRecords and listPitchRecords and listRollRecords and listCorrectlyUsedRecords :
            #
            # append in the returned list all elements [correctlyUsed, azimuthAlert, pitchAlert, rollAlert]
            listSensorAlerts.append ( listCorrectlyUsedRecords [ -1 ] )
            listSensorAlerts.append ( listAzimuthRecords [ -1 ] )
            listSensorAlerts.append ( listPitchRecords [ -1 ] )
            listSensorAlerts.append ( listRollRecords [ -1 ] )
            #
            # return the final list
            return listSensorAlerts
        #
        # return none because there are no elements in the list
        return None
    
    # function used to print the lists of alerts
    def __str__ ( self ) -> str :
        #
        # initialize as empty the output string
        output: str = ""
        #
        # print debug row of correctly used alerts
        output: str = f"{output}\nLIST OF ALL CORRECTLY USED ALERTS\n"
        #
        # for each correctly used alert
        for correctlyUsedAlert in self.listCorrectlyUsed :
            #
            # print the actual correctly used alert
            output: str = f"{output}{correctlyUsedAlert}"
        #
        # print debug row of azimuth alerts
        output: str = f"{output}\nLIST OF ALL AZIMUTH ALERTS\n"
        #
        # for each azimuth alert
        for azimuthAlert in self.listAzimuthAlerts :
            #
            # print the azimuth alert
            output: str = f"{output}{azimuthAlert}"
        #
        # print debug row of pitch alerts
        output: str = f"{output}\nLIST OF ALL PITCH ALERTS\n"
        #
        # for each pitch alert
        for pitchAlert in self.listPitchAlerts :
            #
            # print the pitch alert
            output: str = f"{output}{pitchAlert}"
        #
        # print debug row of roll alerts
        output: str = f"{output}\nLIST OF ALL ROLL ALERTS\n"
        #
        # for each roll alert
        for rollAlert in self.listRollAlerts :
            #
            # print the roll alert
            output: str = f"{output}{rollAlert}"
        #
        # return the output
        return output

if __name__ == "__main__" :
    d = SensorAlert ( )
    d.addCorrectlyUsed ( True , 10 )
    d.addAzimuthAlert ( True , 13 )
    d.addPitchAlert ( True , 15 )
    print ( d )
