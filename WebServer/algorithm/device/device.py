# class used to target the single device
class Device :
    
    # constructor to initialize the device object
    def __init__ ( self , ipAddress: str ) -> None :
        #
        # only the ip address
        self.ipAddress: str = ipAddress
