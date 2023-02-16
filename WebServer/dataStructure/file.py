# class to manage a specific file
class File :
    
    # constructor for the file class
    def __init__ ( self , filename: str , properties: str ) :
        #
        # save the filename
        self.filename = filename
        #
        # save the property for the file
        self.properties = properties
        #
        # open the file
        self.file = open ( self.filename , self.properties )
    
    # function used to close the file
    def closeFile ( self ) :
        #
        # close the file
        self.file.close ( )
    
    # function used to write into the file
    def writeIntoFile ( self , data: str ) :
        #
        # write data into file
        self.file.write ( data + "\n" )
