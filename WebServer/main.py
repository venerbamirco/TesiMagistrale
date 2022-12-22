from managementlog.incomingData import filename , IncomingData , properties
from managementsocket.socketTcp import SocketTcp , host , port , clients

if __name__ == "__main__" :
	
	# create the file to store all incoming messages
	incomingData = IncomingData ( filename , properties )
	
	# open the file
	incomingData.openFile ( )
	
	# create the management socket object
	socketTcp = SocketTcp ( host , port , clients, incomingData )
	
	# create and configure the tcp socket object
	socketTcp.createAndConfigureSocketTcp ( )
	
	# wait a request in the tcp socket
	socketTcp.waitNewRequests ( )
	
	# activate listening mode in the socket tcp
	socketTcp.listenMessageIntoSocket ( )
	
	# close the tcp socket
	socketTcp.closeTcpSocket ( )
	
	# close the file
	incomingData.closeFile()
