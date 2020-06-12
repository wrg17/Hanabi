import sys
import socket
import select
import errno

# Used to build basic GUI application
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets  import (QApplication, QLabel, 
	QLineEdit, QTextEdit, QVBoxLayout, QHBoxLayout, QWidget)
from threading import Thread
from time import sleep

HEADER_SIZE = 10
IP = '192.168.1.234'
PORT = 8888

class ClientWindow(QWidget):
	def __init__(self):
		super(ClientWindow, self).__init__()
		self.my_username = input("Username: ")
		self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.client_socket.connect((IP, PORT))
		self.client_socket.setblocking(False)

		username = self.my_username.encode('utf-8')
		username_header = f"{len(username):<{HEADER_SIZE}}".encode('utf-8')
		self.client_socket.send(username_header + username)

		self.initUI()

	def initUI(self):
		self.message_area = QTextEdit()
		layout = QVBoxLayout()
		layout.addWidget(self.message_area)
		input_row = QHBoxLayout()
		input_row.addWidget(QLabel("Input: "))
		self.line_input = QLineEdit()
		input_row.addWidget(self.line_input)
		layout.addLayout(input_row)
		self.setLayout(layout)
		self.resize(500,500)
		self.setWindowTitle("Basic IO")
		self.show()

		self.new_messages = []

		self.line_input.returnPressed.connect(self.send_message)
		self.timer1 = QTimer()
		self.timer1.timeout.connect(self.receive_messages)
		self.timer1.start(200)

		self.timer2 = QTimer()
		self.timer2.timeout.connect(self.update_messages)
		self.timer2.start(200)
		

	def receive_messages(self):
		try:
			username_header = self.client_socket.recv(HEADER_SIZE)
			if not len(username_header):
				print("Connection closed by the server")
				sys.exit()
			username_length = int(username_header.decode('utf-8').strip())
			username = self.client_socket.recv(username_length).decode('utf-8')
			message_header = self.client_socket.recv(HEADER_SIZE)
			message_length = int(message_header.decode('utf-8').strip())
			message = self.client_socket.recv(message_length).decode('utf-8')
			self.new_messages.append(f"{username}: {message}")
		except IOError as e:
			if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
				print('Reading error', str(e))
				sys.exit() 
			pass

		except Exception as e:
			print('General error', str(e))
			sys.exit()


	def send_message(self):
		message = self.line_input.text()
		message = message.encode('utf-8')
		message_header = f"{len(message):<{HEADER_SIZE}}".encode('utf-8')
		self.client_socket.send(message_header + message)
		self.line_input.clear()

	def update_messages(self):
		while self.new_messages:
			self.message_area.append(self.new_messages.pop(0))


def main():
	app = QApplication(sys.argv)
	main = ClientWindow()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()

