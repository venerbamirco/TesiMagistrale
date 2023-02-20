# class to create the dictionary
class Dictionary :
    
    # constructor for the management of the dictionary
    def __init__ ( self ) -> None :
        #
        # create an empty dictionary
        self.__dictionarySyscall: dict = dict ( )
    
    # function used to insert a new key in the dictionary
    def insertNewKey ( self , key: str ) -> None :
        #
        # if key not in dictionary
        if key not in self.__dictionarySyscall.keys ( ) :
            #
            # insert new key with an empty list
            self.__dictionarySyscall [ key ]: list = [ ]
    
    # function used to insert a new element in a certain key
    def insertNewValueInKey ( self , key: str , value: str ) -> None :
        #
        # if key not in dictionary
        if key not in self.__dictionarySyscall.keys ( ) :
            #
            # call the insert key function
            self.insertNewKey ( key )
            #
            # call the insert new value in a key function
            self.insertNewValueInKey ( key , value )
        #
        # if key in dictionary
        else :
            #
            # append the new element in the right key
            self.__dictionarySyscall.get ( key ).append ( value )
    
    # function used to get the list of elements of a key
    def getElementsOfKey ( self , key: str ) -> list :
        #
        # return the list of element for the actual key
        return self.__dictionarySyscall.get ( key )
    
    # function used to delete a particular value from a key
    def deleteValueInKey ( self , key: str , value: str ) -> None :
        #
        # if key in dictionary
        if key in self.__dictionarySyscall.keys ( ) :
            #
            # if the value is in the elements of key
            if value in self.__dictionarySyscall.get ( key ) :
                #
                # remove the element in the right key
                self.__dictionarySyscall.get ( key ).remove ( value )
    
    # function used to delete all values from a key
    def deleteAllValuesInKey ( self , key: str ) -> None :
        #
        # if key in dictionary
        if key in self.__dictionarySyscall.keys ( ) :
            #
            # remove all elements in the right key
            self.__dictionarySyscall.get ( key ).clear ( )
    
    # function used to delete a key from the dictionary
    def deleteKey ( self , key: str ) -> None :
        #
        # delete the key with its values
        self.__dictionarySyscall.pop ( key )
    
    # function used to update value in key
    def updateValueInKey ( self , key: str , oldValue: str , newValue: str ) -> None :
        #
        # if key in dictionary
        if key in self.__dictionarySyscall.keys ( ) :
            #
            # if old value is in list
            if oldValue in self.__dictionarySyscall.get ( key ) :
                #
                # change the actual old element with the actual newest one
                self.__dictionarySyscall.get ( key ) [ self.__dictionarySyscall.get ( key ).index ( oldValue ) ]: str = newValue
    
    # function used to update a key
    def updateKey ( self , oldKey: str , newKey: str ) -> None :
        #
        # if old key in dictionary
        if oldKey in self.__dictionarySyscall.keys ( ) :
            #
            # save the list of elements of old key
            list_elements_old_key = self.__dictionarySyscall.get ( oldKey )
            #
            # delete the key from the dictionary
            self.deleteKey ( oldKey )
            #
            # insert the new key
            self.insertNewKey ( newKey )
            #
            # for each elements of old key
            for value in list_elements_old_key :
                #
                # add the element in the new key
                self.insertNewValueInKey ( newKey , value )
    
    # function used to get the dictionary
    def getDictionary ( self ) -> dict :
        #
        # return the dictionary
        return self.__dictionarySyscall
    
    # function used to print the dictionary and its key values
    def __str__ ( self ) -> str :
        #
        # variable to store the output
        output: str = ""
        #
        # for each key
        for key in self.__dictionarySyscall.keys ( ) :
            #
            # print the actual key
            output += f"{key}\n"
            #
            # for each element of the list of actual key
            for element in self.__dictionarySyscall [ key ] :
                #
                # print actual element of the list
                output += f"\t\t{element}\n"
        #
        # return the output
        return output

if __name__ == "__main__" :
    d = Dictionary ( )
    d.insertNewKey ( "ptracer" )
    d.insertNewValueInKey ( "ptracer" , "nuovovalore" )
    d.insertNewValueInKey ( "ptracer" , "nuovovalore2" )
    d.updateValueInKey ( "ptracer" , "nuovovalore" , "nuovovalore1" )
    d.insertNewKey ( "syscall1" )
    d.insertNewValueInKey ( "syscall1" , "nuovovalore11" )
    print ( d )
