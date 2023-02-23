"""
LIST OF ALL DEBUGGABLE APPLICATIONS

	Application
		Name: application1

	Application
		Name: application2
"""

# class used to manage the single application
class Application :
    
    # constructor to initialize the single application
    def __init__ ( self , name: str ) -> None :
        #
        # save the name
        self.name: str = name
    
    # function used to print the application details
    def __str__ ( self ) :
        #
        # variable to store the output
        output: str = "\n\tApplication\n"
        #
        # add name of the application
        output: str = f"{output}\t\tName: {self.name}\n"
        #
        # return the output
        return output

# class used to manage the list of debuggable applications
class DebuggableApplications :
    
    # constructor to initialize the object to manage the list of debuggable applications
    def __init__ ( self ) -> None :
        #
        # create the list for all debuggable applications
        self.listDebuggableApplications: list [ Application ] = list ( )
    
    # function used to insert a new debuggable application in the list
    def addDebuggableApplication ( self , name: str ) -> None :
        #
        # create the application with the right name
        application: Application = Application ( name )
        #
        # insert the new debuggable application in the list
        self.listDebuggableApplications.append ( application )
        #
        # order the list of debuggable applications
        self.listDebuggableApplications.sort ( key = lambda x : x.name )
    
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
            output: str = f"{output}{application}"
        #
        # return the output
        return output

if __name__ == "__main__" :
    i = DebuggableApplications ( )
    i.addDebuggableApplication ( "application1" )
    i.addDebuggableApplication ( "application2" )
    i.addDebuggableApplication ( "application3" )
    print ( i )
