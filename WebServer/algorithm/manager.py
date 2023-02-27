from dataStructure.android.charging import Charging
from utils.functions import strToBool

# class used to manage all the parts of the algorithm
class Manager :
    
    # constructor to initialize the manager
    def __init__ ( self ) -> None :
        #
        # initialize the charging manager
        self.chargingManager = Charging ( )
    
    # function used to add a record in charging
    def addChargingRecord ( self , record: str ) -> None :
        #
        # input: 1677155940999 UsbChecker: ischarg: false usbcharg: false accharg: false
        #
        # split the input string using the space character
        listInputWords: list [ str ] = record.split ( )
        #
        # get timestamp
        timestamp: int = int ( listInputWords [ 0 ] )
        #
        # get if it is charging
        isCharging: bool = strToBool ( listInputWords [ 3 ] )
        #
        # get if it is charging using usb
        usbCharging: bool = strToBool ( listInputWords [ 5 ] )
        #
        # get if it is charging using ac
        acCharging: bool = strToBool ( listInputWords [ 7 ] )
        #
        # add the charging record in the relative manager
        self.chargingManager.addChargingRecord ( isCharging , usbCharging , acCharging , timestamp )

if __name__ == "__main__" :
    #
    m = Manager ( )
    m.addChargingRecord ( "1677155940999 UsbChecker: ischarg: true usbcharg: false accharg: true" )
