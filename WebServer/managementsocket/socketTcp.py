import socket

from managementlog.incomingData import IncomingData

# hostname for the tcp managementsocket
host = socket.gethostname ( )
# port for the tcp managementsocket
port = 1234
# maximum number of connected clients
clients = 1

# class to manage the tcp socker
class SocketTcp :
	
	# constructor to initialize the whole managementsocket object
	def __init__ ( self , host: str , port: int , clients: int , file: IncomingData ) :
		# initialize the host field
		self.__host = host
		# initialize the port field
		self.__port = port
		# initialize the maximum number of client
		self.__clients = clients
		# save the file where to save all incoming messages
		self.__fileIncomingData = file
	
	# function used to update host field
	def setHost ( self , host: str ) :
		# update host field
		self.__host = host
	
	# function used to update port field
	def setPort ( self , port: int ) :
		# update port field
		self.__port = port
	
	# function used to update clients number
	def setClients ( self , clients: int ) :
		# update clients field
		self.__clients = clients
	
	# function used to get the host field
	def getHost ( self ) :
		# get the host field
		return self.__host
	
	# function used to get the port field
	def getPort ( self ) :
		# get the port field
		return self.__port
	
	# function used to get the clients field
	def getPort ( self ) :
		# get the clients field
		return self.__clients
	
	# function used to create the tcp managementsocket
	def createAndConfigureSocketTcp ( self ) :
		# create the managementsocket object
		self.__server_socket = socket.socket ( )
		# bing parameter to the managementsocket object
		self.__server_socket.bind ( (self.__host , self.__port) )
		# one client maximum for the connection
		self.__server_socket.listen ( self.__clients )
	
	# function used to listen new requests
	def waitNewRequests ( self ) :
		# wait new incoming request
		self.__conn , self.__address = self.__server_socket.accept ( )
		print ( "Connection from: " + str ( self.__address ) )
	
	# function to receive data from the managementsocket
	def listenMessageIntoSocket ( self ) :
		# while all messages are not received
		while True :
			# receive data stream, it won't accept data packet greater than 10240 bytes
			self.__receivedMessageBytes = self.__conn.recv ( 10240 )
			# if there aren't received data
			if not self.__receivedMessageBytes :
				# exit from listening mode
				break
			# transform the bytes array into a string
			self.__receivedMessageString = self.__receivedMessageBytes.decode ( )
			# delete from the incoming message the final new line
			self.__receivedMessageString = self.__receivedMessageString.rstrip ( )
			# if the received string is the terminal string
			if self.__receivedMessageString == "exit" :
				# exit from listening mode
				break
			# if the received string is not an empty string
			if self.__receivedMessageString != "\n" :
				# write the incoming message into the file
				self.__fileIncomingData.writeIntoFile ( self.__receivedMessageString )
	
	# function used to close the tcp managementsocket
	def closeTcpSocket ( self ) :
		# close the connection
		self.__conn.close ( )
		# close the managementsocket
		self.__server_socket.close ( )


"""def server_program ( ) :
	server_socket = managementsocket.managementsocket ( )  # get instance
	# look closely. The bind() function takes tuple as argument
	server_socket.bind ( (host , port) )  # bind host address and port together
	
	# configure how many client the server can listen simultaneously
	server_socket.listen ( 2 )
	conn , address = server_socket.accept ( )  # accept new connection
	print ( "Connection from: " + str ( address ) )
	
	file = open ( "myfile.txt" , "w" )
	
	while True :
		# receive data stream. it won't accept data packet greater than 10240 bytes
		data = conn.recv ( 10240 ).decode ( )
		if not data :
			# if data is not received break
			break
		print ( data )
		file.write ( data + "\n" )
	
	conn.close ( )  # close the connection
	file.close ( )"""
