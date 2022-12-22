# name for the file to store all incoming messages
filename = "savedlog/incomingdata.log"

# property to define how to open the file
properties = "w"

# class to manage the incoming messages
class IncomingData :
	
	# constructor to initialize the whole incomingdata object
	def __init__ ( self , filename , properties ) :
		# save the filename
		self.__filename = filename
		# save the property for the file
		self.__properties = properties
	
	# function used to open the file to store all incoming messages
	def openFile ( self ) :
		# open the file
		self.__file = open ( self.__filename , self.__properties )
	
	# function used to close the file to store all incoming messages
	def closeFile ( self ) :
		# close the file
		self.__file.close ( )
	
	# function used to write into the file
	def writeIntoFile ( self , data ) :
		# write data into file
		self.__file.write ( data + "\n" )
