import socket
import select

HEADER_SIZE = 10
# choose IP based on what launches the program --> communicate with Client.py after.
IP = '192.168.1.234'
PORT = 8888

serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Easier usage when running server repeatedly during debugging
serv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serv_socket.bind((IP, PORT))

# At most 5 people in queue at a time. We shouldn't even expect more than 5 to be concurrently using it
serv_socket.listen()

sockets_list = [serv_socket]
clients = {}

print(f"Listening for connections on {IP}:{PORT}...")

def receive_message(clientsocket):
	try:
		message_header = clientsocket.recv(HEADER_SIZE)
		if not len(message_header): 
			return False
		message_length = int(message_header.decode('utf-8').strip())
		return {'header': message_header, 'data': clientsocket.recv(message_length)}
	except:
		return False

while True:
	# Helps handle socket interfaces on different OS
	read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)
	for notified_socket in read_sockets:
		if notified_socket == serv_socket:
			client_socket, client_address = serv_socket.accept()
			user = receive_message(client_socket) 
			if user is False:
				continue
			sockets_list.append(client_socket)
			clients[client_socket] = user
			print(f"Accepted new connection from {client_address[0]}:{client_address[1]}. Username: {user['data'].decode('utf-8')}")
			# TODO Implement IP security protocols for trusted and not trusted connections
		else:
			message = receive_message(notified_socket)
			if message is False:
				print(f"Closed connection from {clients[notified_socket]['data'].decode('utf-8')}")
				sockets_list.remove(notified_socket)
				del clients[notified_socket]
			else:
				user = clients[notified_socket]
				print(f"Received message from {user['data'].decode('utf-8')}: {message['data'].decode('utf-8')}")

				for cs in clients:
					cs.send(user['header'] + user['data'] + message['header'] + message['data'])

	for notified_socket in exception_sockets:
		print(f"Closed connection from {clients[notified_socket]['data'].decode('utf-8')}")
		sockets_list.remove(notified_socket)
		del clients[notified_socket]
