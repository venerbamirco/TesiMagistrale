"""
LIST OF ALL DEVICES

	Device
		Ip address: 192.168.1.1
		Security level: 1
		Good things:
			Debuggable applications
			Developer options
			Charging type
			Ptracer Started
			Stationary device
		Bad things:
			Sensor alerts
			Debugger found
			Instructions much time
			Subsequences found
			Sequence not secure
"""
from datetime import datetime

from algorithm.settings.settings import Settings

# Security levels
#
# Android:
#   debuggable application
#   developer options
#   charging
#   ptracer
#   stationary
#   sensor alerts
#   debugger found -> max level
#
# Ptracer:
#   instruction much time
#   sequences not secure
#   subsequences

# Numbers:
#   0 safe
#   > 0 component that are not safe
#   10 max level -> blocked

# 0 safe
# 1-4 normal
# 5-8 warning
# 9-10 blocked

# class used for security level of the device
class SecurityLevel :
    
    # constructor to initialize the security level
    def __init__ ( self ) -> None :
        #
        # security level
        self.securityLevel: int = 0
        #
        # good things
        self.goodThings: list [ str ] = Settings.possibleSecurityLevel
        #
        # bad things
        self.badThings: list [ str ] = list ( )
        #
        # timestamp for each flag
        self.timestampFlags: list [ str ] = list ( )
        #
        # initialize structure of timestamp of each flag
        for i in range ( 0 , 10 ) :
            self.timestampFlags.append ( "" )
    
    # function used to increment the security level
    def incrementSecurityLevel ( self , type: str ) -> int :
        #
        # if not training mode
        if not Settings.training :
            #
            # if the debugger is found
            if type == "Debugger found" or type == "Ptracer Started" :
                #
                # if we can show the security level
                if Settings.securityLevel :
                    #
                    # debug row
                    print ( "Security level of device = 10, device blocked" )
                #
                # if actual type is in good things
                if type in self.goodThings :
                    #
                    # block the device immediately
                    self.securityLevel: int = 10
                    #
                    # add in bad thing current type
                    self.badThings.append ( type )
                    #
                    # remove from good current type
                    self.goodThings.remove ( type )
                    #
            #
            # else if debugger is not found and ptracer is started
            else :
                #
                # if actual type is in good things
                if type in self.goodThings :
                    #
                    # if security level is less than 10
                    if self.securityLevel < 10 :
                        #
                        # increment actual security level
                        self.securityLevel: int = self.securityLevel + 1
                    #
                    # add in bad thing current type
                    self.badThings.append ( type )
                    #
                    # remove from good current type
                    self.goodThings.remove ( type )
                    #
                    # if we can show the security level
                    if Settings.securityLevel :
                        #
                        # debug row
                        print ( "Security level of device = " + str ( self.securityLevel ) )
        #
        # return security level
        return self.securityLevel
    
    # function used for the representation of security level
    def __str__ ( self ) -> str :
        #
        # print debug row of security level
        output: str = f"\n\t\tSecurity level: {self.securityLevel}\n"
        #
        # add the good things of the device
        output: str = f"{output}\t\tGood things:"
        #
        # for each good thing
        for goodThing in self.goodThings :
            #
            # add actual good thing to the output
            output: str = f"{output}\n\t\t\t{goodThing}"
        #
        # add the bad things of the device
        output: str = f"{output}\n\t\tBad things:"
        #
        # for each bad thing
        for badThing in self.badThings :
            #
            # add actual bad thing to the output
            output: str = f"{output}\n\t\t\t{badThing}"
        #
        # return the output
        return output

class Device :
    
    # constructor to initialize the device object
    def __init__ ( self , ipAddress: str ) -> None :
        #
        # only the ip address
        self.ipAddress: str = ipAddress
        #
        # number of debuggable applications
        self.numberDebuggableApplications: int = 0
        #
        # number of times that the device is stationary
        self.numberStationary: int = 0
        #
        # number of times that the device is in bad position
        self.numberBadPosition: int = 0
        #
        # number of times that an instruction has a long duration
        self.numberInstructionLongerDuration: int = 0
        #
        # number of times that is found a insecure subsequence
        self.numberFoundInsecureSubsequence: int = 0
        #
        # number of times that is found a insecure sequence
        self.numberInsecureSequence: int = 0
        #
        # security level
        self.securityLevel: SecurityLevel = SecurityLevel ( )
    
    # function used for the representation of the single device
    def __str__ ( self ) -> str :
        #
        # debug variable to store the output
        output: str = ""
        #
        # add the description of the device
        output: str = f"{output}\t\tIp address: {self.ipAddress}"
        #
        # add the security level of the device
        output: str = f"{output}{self.securityLevel}"
        #
        # return the output
        return output
    
    # function used to increment security level
    def incrementSecurityLevelWithoutPrint ( self , type: str ) -> int :
        #
        # increment security level and return the count of bad things
        return self.securityLevel.incrementSecurityLevel ( type )
    
    # function used to increment security level
    def incrementSecurityLevel ( self , type: str, timestamp:int ) -> int :
        #
        # if not training mode
        if not Settings.training :
            #
            # switch for type of security level
            match type :
                #
                # debugger
                case "Debugger found" :
                    self.securityLevel.timestampFlags [ 6 ] = str ( timestamp)
                    #
                    # increment security level and return the count of bad things
                    return self.securityLevel.incrementSecurityLevel ( type )
                #
                # ptracer not started
                case "Ptracer Started" :
                    self.securityLevel.timestampFlags [ 3 ] = str ( timestamp)
                    #
                    # increment security level and return the count of bad things
                    return self.securityLevel.incrementSecurityLevel ( type )
                #
                # charging type
                case "Charging type" :
                    self.securityLevel.timestampFlags [ 2 ] = str ( timestamp)
                    #
                    # if we can show that a new things is found
                    if Settings.foundNewThingSecurityLevel :
                        #
                        # debug row
                        print ( "\nFound USB charging type." )
                    #
                    # increment security level and return the count of bad things
                    return self.securityLevel.incrementSecurityLevel ( type )
                #
                # developer options
                case "Developer options" :
                    self.securityLevel.timestampFlags [ 1 ] = str ( timestamp)
                    #
                    # if we can show that a new things is found
                    if Settings.foundNewThingSecurityLevel :
                        #
                        # debug row
                        print ( "\nFound developer options enabled" )
                    #
                    # increment security level and return the count of bad things
                    return self.securityLevel.incrementSecurityLevel ( type )
                #
                # debuggable application
                case "Debuggable applications" :
                    self.securityLevel.timestampFlags [ 0 ] = str ( timestamp)
                    #
                    # increment number of debuggable applications
                    self.numberDebuggableApplications: int = self.numberDebuggableApplications + 1
                    #
                    # if we can show that a new things is found
                    if Settings.foundNewThingSecurityLevel :
                        #
                        # debug row
                        print ( "\nFound debuggable application." )
                    #
                    # increment security level and return the count of bad things
                    return self.securityLevel.incrementSecurityLevel ( type )
                #
                # device is stationary
                case "Stationary device" :
                    #
                    # increment number of stationary position
                    self.numberStationary: int = self.numberStationary + 1
                    #
                    #
                    print ( "\nDevice stationary" )
                    #
                    # if we found tot insecure sequences
                    if self.numberStationary == Settings.numberStationaryDevice :
                        self.securityLevel.timestampFlags [ 4 ] = str ( timestamp)
                        #
                        # if we can show that a new things is found
                        if Settings.foundNewThingSecurityLevel :
                            #
                            # debug row
                            print ( "\nDevice stationary many times" )
                        #
                        # increment security level and return the count of bad things
                        return self.securityLevel.incrementSecurityLevel ( type )
                #
                # device in bad position
                case "Sensor alerts" :
                    #
                    # increment number of bad position
                    self.numberBadPosition: int = self.numberBadPosition + 1
                    #
                    #
                    print ( "\nBad position" )
                    #
                    # if we found tot bad positions
                    if self.numberBadPosition == Settings.numberSensorAlerts :
                        self.securityLevel.timestampFlags [ 5 ] = str ( timestamp)
                        #
                        # if we can show that a new things is found
                        if Settings.foundNewThingSecurityLevel :
                            #
                            # debug row
                            print ( "\nBad position many times" )
                        #
                        # increment security level and return the count of bad things
                        return self.securityLevel.incrementSecurityLevel ( type )
                #
                # instruction with longer duration
                case "Instructions much time" :
                    #
                    # increment number of longer duration instruction
                    self.numberInstructionLongerDuration: int = self.numberInstructionLongerDuration + 1
                    #
                    # if we found tot longer instructions
                    if self.numberInstructionLongerDuration == Settings.numberInstructionLongerDuration :
                        self.securityLevel.timestampFlags [ 7 ] = str ( timestamp)
                        #
                        # if we can show that a new things is found
                        if Settings.foundNewThingSecurityLevel :
                            #
                            # debug row
                            print ( "\nLonger duration many times" )
                        #
                        # increment security level and return the count of bad things
                        return self.securityLevel.incrementSecurityLevel ( type )
                #
                # found subsequence
                case "Subsequences found" :
                    #
                    # increment number of subsequences
                    self.numberFoundInsecureSubsequence: int = self.numberFoundInsecureSubsequence + 1  #
                    #
                    print ( "\nFound subsequence" )
                    #
                    # if we found tot insecure subsequences
                    if self.numberFoundInsecureSubsequence == Settings.numberInsecureSubsequences :
                        self.securityLevel.timestampFlags [ 8 ] = str ( timestamp)
                        #
                        # if we can show that a new things is found
                        if Settings.foundNewThingSecurityLevel :
                            #
                            # debug row
                            print ( "\nSubsequences many times" )
                        #
                        # increment security level and return the count of bad things
                        return self.securityLevel.incrementSecurityLevel ( type )
                #
                # insecure sequence
                case "Sequence not secure" :
                    #
                    # increment number of insecure sequence
                    self.numberInsecureSequence: int = self.numberInsecureSequence + 1
                    #
                    # if we found tot insecure sequences
                    if self.numberInsecureSequence == Settings.numberInsecureSequence :
                        self.securityLevel.timestampFlags [ 9 ] = str ( timestamp)
                        #
                        # if we can show that a new things is found
                        if Settings.foundNewThingSecurityLevel :
                            #
                            # debug row
                            print ( "\nInsecure sequence many times." )
                        #
                        # increment security level and return the count of bad things
                        return self.securityLevel.incrementSecurityLevel ( type )
        #
        # return count of bad things
        return self.securityLevel.securityLevel

# class used to manage the list of devices
class Devices :
    
    # constructor to initialize the list of devices
    def __init__ ( self ) -> None :
        #
        # list of devices initially empty
        self.listDevices: list [ Device ] = list ( )
        #
        # list of safe devices initially empty
        self.listSafeDevices: list [ Device ] = list ( )
        #
        # list of normal devices initially empty
        self.listNormalDevices: list [ Device ] = list ( )
        #
        # list of warning devices initially empty
        self.listWarningDevices: list [ Device ] = list ( )
        #
        # list of blocked devices initially empty
        self.listBlockedDevices: list [ Device ] = list ( )
    
    # function used to add a device
    def addDevice ( self , ipAddress: str ) -> None :
        #
        # if there are not device with same ip address
        if not any ( device.ipAddress == ipAddress for device in self.listDevices ) :
            #
            # create a new device
            device: Device = Device ( ipAddress )
            #
            # append the new device in the list of all devices
            self.listDevices.append ( device )
            #
            # append the new device in the list of good things
            self.listSafeDevices.append ( device )
    
    # function used to increment level of security
    def incrementLevelSecurity ( self , ipAdress: str , type: str , timestamp: int ) -> None :
        #
        # for each device
        for device in self.listDevices :
            #
            # if it is the right device
            if device.ipAddress == ipAdress :
                #
                # increment security level
                device.incrementSecurityLevel ( type, timestamp )
                #
                # if normal level
                if device.securityLevel.securityLevel == 1 :
                    #
                    # if device in safe list
                    if device in self.listSafeDevices :
                        #
                        # remove from safe list
                        self.listSafeDevices.remove ( device )
                    #
                    # if there are not device with same ip address
                    if not any ( d.ipAddress == ipAdress for d in self.listNormalDevices ) :
                        #
                        # add in normal device list
                        self.listNormalDevices.append ( device )
                #
                # if warning level
                elif device.securityLevel.securityLevel == 5 :
                    #
                    # if device in normal list
                    if device in self.listNormalDevices :
                        #
                        # remove from normal list
                        self.listNormalDevices.remove ( device )
                    #
                    # if there are not device with same ip address
                    if not any ( d.ipAddress == ipAdress for d in self.listWarningDevices ) :
                        #
                        # add in warning device list
                        self.listWarningDevices.append ( device )
                #
                # if blocked level
                elif 9 <= device.securityLevel.securityLevel <= 10 :
                    #
                    # if device in safe list
                    if device in self.listSafeDevices :
                        #
                        # remove from safe list
                        self.listSafeDevices.remove ( device )
                    #
                    # if device in normal list
                    elif device in self.listNormalDevices :
                        #
                        # remove from normal list
                        self.listNormalDevices.remove ( device )
                    #
                    # if device in warning list
                    elif device in self.listWarningDevices :
                        #
                        # remove from warning list
                        self.listWarningDevices.remove ( device )
                    #
                    # if there are not device with same ip address
                    if not any ( d.ipAddress == ipAdress for d in self.listBlockedDevices ) :
                        #
                        # add in blocked device list
                        self.listBlockedDevices.append ( device )
    
    # function used to increment level of security
    def incrementSecurityLevelWithoutPrint ( self , ipAdress: str , type: str ) -> None :
        #
        # for each device
        for device in self.listDevices :
            #
            # if it is the right device
            if device.ipAddress == ipAdress :
                #
                # increment security level
                device.incrementSecurityLevelWithoutPrint ( type )
                #
                # if normal level
                if device.securityLevel.securityLevel == 1 :
                    #
                    # if device in safe list
                    if device in self.listSafeDevices :
                        #
                        # remove from safe list
                        self.listSafeDevices.remove ( device )
                    #
                    # if there are not device with same ip address
                    if not any ( d.ipAddress == ipAdress for d in self.listNormalDevices ) :
                        #
                        # add in normal device list
                        self.listNormalDevices.append ( device )
                #
                # if warning level
                elif device.securityLevel.securityLevel == 5 :
                    #
                    # if device in normal list
                    if device in self.listNormalDevices :
                        #
                        # remove from normal list
                        self.listNormalDevices.remove ( device )
                    #
                    # if there are not device with same ip address
                    if not any ( d.ipAddress == ipAdress for d in self.listWarningDevices ) :
                        #
                        # add in warning device list
                        self.listWarningDevices.append ( device )
                #
                # if blocked level
                elif 9 <= device.securityLevel.securityLevel <= 10 :
                    #
                    # if device in safe list
                    if device in self.listSafeDevices :
                        #
                        # remove from safe list
                        self.listSafeDevices.remove ( device )
                    #
                    # if device in normal list
                    elif device in self.listNormalDevices :
                        #
                        # remove from normal list
                        self.listNormalDevices.remove ( device )
                    #
                    # if device in warning list
                    elif device in self.listWarningDevices :
                        #
                        # remove from warning list
                        self.listWarningDevices.remove ( device )
                    #
                    # if there are not device with same ip address
                    if not any ( d.ipAddress == ipAdress for d in self.listBlockedDevices ) :
                        #
                        # add in blocked device list
                        self.listBlockedDevices.append ( device )
    
    # function used to check a presence of a device
    def checkPresenceDevice ( self , ipAddress: str ) -> bool :
        #
        # for each device
        for device in self.listDevices :
            #
            # if actual ip address is the right address
            if device.ipAddress == ipAddress :
                #
                # device found
                return True
        #
        # device not found
        return False
    
    # function used for the representation of list of devices
    def __str__ ( self ) -> str :
        #
        # print debug row of safe security level
        output: str = f"\nLIST OF ALL DEVICES SAFE DEVICES, LEVEL=0\n"
        #
        # for each safe device
        for device in self.listSafeDevices :
            #
            # print actual device
            output: str = f"{output}\n\tDevice\n{device}\n"
        #
        # print debug row of normal security level
        output: str = f"{output}\nLIST OF ALL DEVICES NORMAL DEVICES, LEVEL=1-4\n"
        #
        # for each normal device
        for device in self.listNormalDevices :
            #
            # print actual device
            output: str = f"{output}\n\tDevice\n{device}\n"
        #
        # print debug row of warning security level
        output: str = f"{output}\nLIST OF ALL DEVICES WARNING DEVICES, LEVEL=5-8\n"
        #
        # for each warning device
        for device in self.listWarningDevices :
            #
            # print actual device
            output: str = f"{output}\n\tDevice\n{device}\n"
        #
        # print debug row of blocked security level
        output: str = f"{output}\nLIST OF ALL DEVICES BLOCKED DEVICES, LEVEL=9-10\n"
        #
        # for each blocked device
        for device in self.listBlockedDevices :
            #
            # print actual device
            output: str = f"{output}\n\tDevice\n{device}\n"
        #
        # return the output
        return output

if __name__ == "__main__" :
    deviceList = Devices ( )
    deviceList.addDevice ( "192.168.1.1" )
    deviceList.incrementLevelSecurity ( "192.168.1.1" , "Debugger found" )
    print ( str ( deviceList ) )
