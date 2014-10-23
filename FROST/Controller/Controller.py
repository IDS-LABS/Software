#!/usr/bin/python

from PyQt4 import QtGui, QtCore

class Controller(object):
	def __init__(self):
		super(Controller, self).__init__()
		self.channels = []
	
	def addChannel(self, channel, recvFunct):
		channel.receiveFunction(recvFunct)
		self.channels.append(channel)