#!/usr/bin/python
from frost.interface import *
from frost.driver import *

class GamepadInterface(baseInterface.interface):
	def __init__(self):
		super(GamepadInterface, self).__init__("GamepadInterface")
		# self.addModel(GamepadModel())
		self.addDriver(LogitechGamepadDriver.LogitechGamepadDriver())
		self.axisLX = 0
		self.axisLY = 0
		self.axisRX = 0
		self.axisRY = 0
		self.buttonA = 0
		self.buttonB = 0
		self.buttonX = 0
		self.buttonY = 0
		self.buttonLB = 0
		self.buttonRB = 0
		self.buttonLT = 0
		self.buttonRT = 0
		self.buttonBack = 0
		self.buttonStart = 0
		self.dPadLeft = 0
		self.dPadRight = 0
		self.dPadUp = 0
		self.dPadDown = 0
		self.LogitechGamepadDriver.startThreads()
		print 'created GamepadInterface'

	def update(self):
		self.axisLX = self.LogitechGamepadDriver.axisLX
		self.axisLY = self.LogitechGamepadDriver.axisLY
		self.axisRX = self.LogitechGamepadDriver.axisRX
		self.axisRY = self.LogitechGamepadDriver.axisRY
		self.buttonA = self.LogitechGamepadDriver.buttonA
		self.buttonB = self.LogitechGamepadDriver.buttonB
		self.buttonX = self.LogitechGamepadDriver.buttonX
		self.buttonY = self.LogitechGamepadDriver.buttonY
		self.buttonLB = self.LogitechGamepadDriver.buttonLB
		self.buttonRB = self.LogitechGamepadDriver.buttonRB
		self.buttonLT = self.LogitechGamepadDriver.buttonLT
		self.buttonRT = self.LogitechGamepadDriver.buttonRT
		self.buttonBack = self.LogitechGamepadDriver.buttonBack
		self.buttonStart = self.LogitechGamepadDriver.buttonStart
		self.dPadLeft = self.LogitechGamepadDriver.dPadLeft
		self.dPadRight = self.LogitechGamepadDriver.dPadRight
		self.dPadUp = self.LogitechGamepadDriver.dPadUp
		self.dPadDown = self.LogitechGamepadDriver.dPadDown
