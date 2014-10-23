#!/usr/bin/python

from PyQt4 import QtGui, QtCore

class Model(object):
	def __init__(self, name, arg=None):
		super(Model, self).__init__()
		self.name = name
		self.arg = arg
		self.parents = []
		self.child = []
		self.value = arg

	def addParent(self, parent):
		self.parent.append(parent)

	def addChild(self, child):
		self.child.append(child)

if __name__ == '__main__':
	rover = Model("Rover")