# class to manage a specific file
class ManageFile:
    
    # constructor to initialize the object to manage the file access
    def __init__(self, filename: str, properties: str):
        # save the filename
        self.__filename = filename
        # save the property for the file
        self.__properties = properties
    
    # function used to open the file
    def openFile(self):
        # open the file
        self.__file = open(self.__filename, self.__properties)
    
    # function used to close the file
    def closeFile(self):
        # close the file
        self.__file.close()
    
    # function used to write into the file
    def writeIntoFile(self, data: str):
        # write data into file
        self.__file.write(data + "\n")
