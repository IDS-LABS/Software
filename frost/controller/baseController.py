#!/usr/bin/python
from PyQt4 import QtGui, QtCore

# class controller(QtCore.QObject):
# 	def __init__(self, name):
# 		super(controller, self).__init__()
# 		self.name = name
# 		self.channels = []
# 		self.models = []
# 		self.protocols = []
	
# 	def addChannel(self, channelName, channel, recvFunct):
# 		# getattr(self, channelName).receiveFunction(recvFunct)
# 		self.channels.append(channel)
# 		setattr(self, channelName, self.channels[len(self.channels)-1])

# 	def addModel(self, modelName, model):
# 		self.models.append(model)
# 		setattr(self, modelName, self.models[len(self.models)-1])

# 	def addProtocol(self, protocolName, protocol):
# 		self.protocols.append(protocol)
# 		setattr(self, protocolName, self.protocols[len(self.protocols)-1])

# class protocol(object):
# 	def __init__(self, name):
# 		super(protocol, self).__init__()
# 		self.name = name

# 	def isFormat(self, msg):
# 		pass
	
# 	def parse(self, msg):
# 		pass