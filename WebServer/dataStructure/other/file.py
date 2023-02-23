# class to manage a specific other
class File :
    
    # constructor for the other class
    def __init__ ( self , filename: str , properties: str ) -> None :
        #
        # save the filename
        self.filename: str = filename
        #
        # save the property for the other
        self.properties: str = properties
        #
        # open the other
        self.file: File = open ( self.filename , self.properties )
    
    # function used to close the other
    def closeFile ( self ) -> None :
        #
        # close the other
        self.file.close ( )
    
    # function used to write into the other
    def writeIntoFile ( self , data: str ) -> None :
        #
        # write data into other
        self.file.write ( f"{data}\n" )
