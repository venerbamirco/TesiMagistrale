# class to manage a specific file
class File :
    
    # constructor for the file class
    def __init__ ( self , filename: str , properties: str ) -> None :
        #
        # save the filename
        self.filename: str = filename
        #
        # save the property for the file
        self.properties: str = properties
        #
        # open the file
        self.file: File = open ( self.filename , self.properties )
    
    # function used to close the file
    def closeFile ( self ) -> None :
        #
        # close the file
        self.file.close ( )
    
    # function used to write into the file
    def writeIntoFile ( self , data: str ) -> None :
        #
        # write data into file
        self.file.write ( f"{data}\n" )
