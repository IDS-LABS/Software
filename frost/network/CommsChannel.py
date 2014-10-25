#!/usr/bin/python

import threading
import time
import socket
import sys
from PyQt4 import QtGui, QtCore

class UDPChannel(QtCore.QObject):
	recvEvent = QtCore.pyqtSignal(int, str,tuple)

	def __init__(self, num, ip, port, timeout=1):
		QtCore.QObject.__init__(self)
		self.num = num
		self.ip = ip
		self.port = port
		self.sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
		self.sock.bind((self.ip, self.port))
		self.sock.settimeout(timeout)
		self.thread = CommsThread(self.num, self.recv)

	def send(self, msg):
		self.send(msg, self.ip, self.port)

	def send(self, msg, ip, port):
		self.sock.sendto(msg, (ip, port))

	def recv(self, num, buf=1024):
		data, addr = self.sock.recvfrom(buf) # buffer size is 1024 bytes
		self.recvEvent.emit(num, data, addr)

	def receiveFunction(self, funct):
		self.recvEvent.connect(funct)

	def startRecv(self):
		self.thread.run()

	def stopRecv(self):
		self.thread.isRunning = False

class CommsThread(threading.Thread):
	def __init__(self, num, funct, arg=None):
		threading.Thread.__init__(self)
		self.isRunning = True
		self.num = num
		self.funct = funct
		self.arg = arg

	def run(self):
		while self.isRunning:
			try:
				if self.arg is not None:
					self.funct(self.num, self.arg)
				else:
					self.funct(self.num)
			except Exception, e:
				pass