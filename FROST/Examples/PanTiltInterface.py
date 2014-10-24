#!/usr/bin/python
from frost.interface import *
from PanTiltModel import *
import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005 #Client

class PanTiltInterface(baseInterface.interface):
	def __init__(self):
		super(PanTiltInterface, self).__init__("PanTiltInterface")
		self.addModel(PanTiltModel())
		# self.addDriver(PanTiltDriver())
		self.pan = 0
		self.tilt = 0
		self.sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
		# self.run()

	def update(self):
		self.PanTiltModel.motorPanAngle = self.pan
		self.PanTiltModel.motorTiltAngle = self.tilt
		# self.PanDriver.setAngle(self.PanTiltModel.motorPanAngle)
		# self.TiltDriver.setAngle(self.PanTiltModel.motorTiltAngle)
		self.sock.sendto("pan:"+str(self.PanTiltModel.motorPanAngle*100)+",tilt:"+str(self.PanTiltModel.motorTiltAngle*100), (UDP_IP, UDP_PORT))
