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


# class used for security level of the device
class SecurityLevel :
    
    # constructor to initialize the security level
    def __init__ ( self ) -> None :
        #
        # security level
        self.securityLevel: int = 0
    
    # function used to increment the security level
    def incrementSecurityLevel ( self ) -> None :
        #
        # increment actual security level
        self.securityLevel = self.securityLevel + 1
    
    # function used for the representation of security level
    def __str__ ( self ) -> str :
        #
        # print debug row of security level
        output: str = f"\n\t\tSecurity level: {self.securityLevel}\n"
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
        # good things
        self.goodThings: list [ str ] = [
            "Debuggable applications" ,
            "Developer options" ,
            "Charging type" ,
            "Ptracer Started" ,
            "Stationary device"
        ]
        #
        # bad things
        self.badThings: list [ str ] = [
            "Sensor alerts" ,
            "Debugger found" ,
            "Instructions much time" ,
            "Subsequences found" ,
            "Sequence not secure"
        ]
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
    
    # function used to increment security level
    def incrementSecurityLevel ( self ) :
        #
        # increment security level
        self.securityLevel.incrementSecurityLevel ( )

# class used to manage the list of devices
class Devices :
    
    # constructor to initialize the list of devices
    def __init__ ( self ) -> None :
        #
        # list of devices initially empty
        self.listDevices: list [ Device ] = list ( )
        #
        # list of good devices initially empty
        self.listGoodDevices: list [ Device ] = list ( )
        #
        # list of bad devices initially empty
        self.listBadDevices: list [ Device ] = list ( )
    
    # function used to add a device
    def addDevice ( self , ipAddress: str ) -> None :
        #
        # create a new device
        device: Device = Device ( ipAddress )
        #
        # append the new device
        self.listDevices.append ( device )
    
    # function used to increment level of security
    def incrementLevelSecurity ( self , ipAdress: str ) -> None :
        #
        # for each device
        for device in self.listDevices :
            #
            # if it is the right device
            if device.ipAddress == ipAdress :
                #
                # increment security level
                device.incrementSecurityLevel ( )
    
    # function used for the representation of list of devices
    def __str__ ( self ) -> str :
        #
        # print debug row of security level
        output: str = f"\nLIST OF ALL DEVICES\n"
        #
        # for each devices
        for device in self.listDevices :
            #
            # print actual device
            output: str = f"{output}\n\tDevice\n{device}"
        #
        # return the output
        return output

if __name__ == "__main__" :
    deviceList = Devices ( )
    deviceList.addDevice ( "192.168.1.1" )
    deviceList.incrementLevelSecurity ( "192.168.1.1" )
    print ( str ( deviceList ) )
