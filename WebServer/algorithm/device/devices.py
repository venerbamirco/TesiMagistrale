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
    def __init__ ( self , settings: Settings ) -> None :
        #
        # save settings reference
        self.settings: Settings = settings
        #
        # security level
        self.securityLevel: int = 0
        #
        # good things
        self.goodThings: list [ str ] = self.settings.possibleSecurityLevel
        #
        # bad things
        self.badThings: list [ str ] = list ( )
    
    # function used to increment the security level
    def incrementSecurityLevel ( self , type: str ) -> int :
        #
        # if the debugger is found
        if type == "Debugger found" :
            #
            # block the device immediately
            self.securityLevel = 10
        #
        # else if debugger is not found
        else :
            #
            # increment actual security level
            self.securityLevel = self.securityLevel + 1
        #
        # add in bad thing current type
        self.badThings.append ( type )
        #
        # remove from good current type
        self.goodThings.remove ( type )
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
    def __init__ ( self , ipAddress: str , settings: Settings ) -> None :
        #
        # only the ip address
        self.ipAddress: str = ipAddress
        #
        # security level
        self.securityLevel: SecurityLevel = SecurityLevel ( settings )
    
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
    def incrementSecurityLevel ( self , type: str ) -> int :
        #
        # increment security level and return the count of bad things
        return self.securityLevel.incrementSecurityLevel ( type )

# class used to manage the list of devices
class Devices :
    
    # constructor to initialize the list of devices
    def __init__ ( self , settings: Settings ) -> None :
        #
        # save reference of settings
        self.settings: Settings = settings
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
        # create a new device
        device: Device = Device ( ipAddress , self.settings )
        #
        # append the new device in the list of all devices
        self.listDevices.append ( device )
        #
        # append the new device in the list of good things
        self.listSafeDevices.append ( device )
    
    # function used to increment level of security
    def incrementLevelSecurity ( self , ipAdress: str , type: str ) -> None :
        #
        # if type is correct
        if type in self.settings.possibleSecurityLevel :
            #
            # for each device
            for device in self.listDevices :
                #
                # if it is the right device
                if device.ipAddress == ipAdress :
                    #
                    # increment security level
                    device.incrementSecurityLevel ( type )
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
    settings = Settings ( )
    deviceList = Devices ( settings )
    deviceList.addDevice ( "192.168.1.1" )
    deviceList.incrementLevelSecurity ( "192.168.1.1" , "Debugger found" )
    print ( str ( deviceList ) )
