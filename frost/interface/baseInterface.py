#!/usr/bin/python
import threading
import time

class interface(threading.Thread):
	def __init__(self, name):
		# super(interface, self).__init__()
		threading.Thread.__init__(self)
		self.interfaces = []
		self.models = []
		self.drivers = []
		
	def addModel(self, model):
		setattr(self, model.name, model)
		self.models.append(getattr(self, model.name))

	def addInterface(self, interface):
		setattr(self, interface.name, interface)
		self.interfaces.append(getattr(self, interface.name))

	def addDriver(self, driver):
		setattr(self, driver.name, driver)
		self.drivers.append(getattr(self, driver.name))

	def update(self):
		pass

	def run(self):
		while True:
			self.update()
			time.sleep(0.001)