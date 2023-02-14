# class to create the dictionary of all syscall and the following instructions
class DictionarySyscall :
    
    # constructor for the management of syscall sequences
    def __init__ ( self ) -> None :
        #
        # create an empty dictionary
        self.__dictionarySyscall = dict ( )
    
    # function used to insert a new key in the dictionary
    def insertNewKeys ( self , keys: [ str ] ) -> None :
        #
        # for each key
        for key in keys :
            # if key not in dictionary
            if key not in self.__dictionarySyscall.keys ( ) :
                #
                # insert new key with an empty list
                self.__dictionarySyscall [ key ] = [ ]
    
    #TODO stesso piu chiavi per deleteValuesInKey e array di elementi
    
    # function used to insert a new element in a certain key
    def insertNewValuesInKey ( self , key: str , values: [ str ] ) -> None :
        #
        # if key not in dictionary
        if key not in self.__dictionarySyscall.keys ( ) :
            #
            # call the insert key function
            self.insertNewKeys ( [ key ] )
            #
            # call the insert new value in a key function
            self.insertNewValuesInKey ( key , values )
        #
        # if key in dictionary
        else :
            #
            # for each value
            for element in values :
                #
                # append the new element in the right key
                self.__dictionarySyscall.get ( key ).append ( element )
    
    # function used to get the list of elements of a key
    def getElementsOfKey ( self , key: str ) -> list ( str ) :
        #
        # return the list of element for the actual key
        return self.__dictionarySyscall.get ( key )
    
    #TODO stesso piu chiavi per deleteValuesInKey e array di elementi
    
    # function used to delete a particular value from a key
    def deleteValuesInKey ( self , key: str , values: [ str ] ) -> None :
        #
        # if key in dictionary
        if key in self.__dictionarySyscall.keys ( ) :
            #
            # for each value
            for element in values :
                #
                # if actual element is in the elements of key
                if element in self.__dictionarySyscall [ key ] :
                    #
                    # remove the element in the right key
                    self.__dictionarySyscall.get ( key ).remove ( element )
                    


    # TODO da fare mettere su deleteAllValuesInKey piu chiavi
    
    # function used to delete all values from a key
    def deleteAllValuesInKey ( self , key: str ) -> None :
        #
        # if key in dictionary
        if key in self.__dictionarySyscall.keys ( ) :
            #
            # remove all elements in the right key
            self.__dictionarySyscall.get ( key ).clear ( )

    # TODO da fare mettere su deleteKey piu chiavi
    
    # function used to delete a key from the dictionary
    def deleteKey ( self , key: str ) -> None :
        #
        # delete the key with its values
        self.__dictionarySyscall.pop ( key )
        
    # da TODO fare mettere su updateValuesInKey piu chiavi con i relativi array su vecchi e nuovi elementi
    
    # function used to update values in key
    def updateValuesInKey ( self , key: str , oldValues: [ str ] , newValues: [ str ] ) -> None :
        #
        # if key in dictionary
        if key in self.__dictionarySyscall.keys ( ) :
            #
            # if the input array have same length
            if len ( oldValues ) == len ( newValues ) :
                #
                # for each combination
                for oldValue , newValue in zip ( oldValues , newValues ) :
                    #
                    # if old value is in list
                    if oldValue in self.__dictionarySyscall.get ( key ) :
                        #
                        # change the actual old element with the actual newest one
                        self.__dictionarySyscall.get ( key ) [ self.__dictionarySyscall.get ( key ).index ( oldValue ) ] = newValue
    
    # function used to update a key
    def updateKey ( self ) :
        pass
    
    # function used to get the dictionary
    def getDictionary ( self ) -> dict :
        #
        # return the dictionary
        return self.__dictionarySyscall
    
    # function used to print the dictionary and its key values
    def printDictionary ( self ) -> None :
        #
        # for each key
        for key in self.__dictionarySyscall.keys ( ) :
            #
            # print the actual key
            print ( key )
            #
            # for each element of the list of actual key
            for element in self.__dictionarySyscall [ key ] :
                #
                # print actual element of the list
                print ( "\t\t" + element )

if __name__ == "__main__" :
    d = DictionarySyscall ( )
    d.insertNewKey ( "syscall" )
    d.insertNewValuesInKey ( "syscall" , [ "nuovovalore0" , "nuovovalore1" , "nuovovalore2" ] )
    d.printDictionary ( )
    d.updateValuesInKey ( "syscall" , [ "nuovovalore0" , "nuovovalore2" ] , [ "nuovovalore00" , "nuovovalore22" ] )
    d.printDictionary ( )
