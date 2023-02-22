"""
LIST OF ALL DEBUGGABLE APPLICATIONS
	application1
	application2
	application3
"""

# class used to manage the list of debuggable applications
class DebuggableApplications :
    
    # constructor to initialize the object to manage the list of debuggable applications
    def __init__ ( self ) -> None :
        #
        # create the list for all debuggable applications
        self.listDebuggableApplications: list [ str ] = list ( )
    
    # function used to insert a new debuggable application in the list
    def addNewDebuggableApplication ( self , application: str ) -> None :
        #
        # if the application is not in the list
        if application not in self.listDebuggableApplications :
            #
            # insert the new debuggable application in the list
            self.listDebuggableApplications.append ( application )
    
    # function used to print the list of all debuggable applications
    def __str__ ( self ) -> str :
        #
        # initialize as empty the output string
        output: str = ""
        #
        # print debug row of all debuggable applications
        output: str = f"{output}\nLIST OF ALL DEBUGGABLE APPLICATIONS\n"
        #
        # for each debuggable application in the list
        for application in self.listDebuggableApplications :
            #
            # print the name of actual application
            output: str = f"{output}\t{application}\n"
        #
        # return the output
        return output

if __name__ == "__main__" :
    i = DebuggableApplications ( )
    i.addNewDebuggableApplication("application1")
    i.addNewDebuggableApplication("application2")
    i.addNewDebuggableApplication("application3")
    print ( i )
