#!/usr/bin/python
from frost.controller import *
from frost.driver import *
from frost.interface import *
from frost.model import *
from frost.network import *
from PanTiltInterface import *
from GamepadInterface import *

# Rover.motorCortex.motorFL.power = 10
# Rover['motorCortex']['motorFL']['power'] = 10
# Rover Model
# Drone Model
# Arm model
# walker model

# model.objects.parameter
# getters and setters

if __name__ == '__main__':
	pantilt = PanTiltInterface()
	gamepad = GamepadInterface()
	gamepad.start()
	pantilt.start()
	while True:
		pantilt.pan = gamepad.axisLX
		pantilt.tilt = gamepad.axisLY


	# udp = UDPChannel(0, "127.0.0.1", 5005)
	# protocol = RoverProtocol("roverProtocol")
	# RoverController("controller", rover, udp, protocol)
	# udp.startRecv()
	# print rover.motorCortex.motorFL.power
	# print rover.motorCortex.motorFL.direction