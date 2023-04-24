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


# class used for security level of the device
class SecurityLevel :
    
    # constructor to initialize the security level
    def __init__ ( self ) -> None :
        #
        # security level
        self.securityLevel: int = 1
