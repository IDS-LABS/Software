#!/usr/bin/python
from frost.model import *

class PanTiltModel(baseModel.baseModel):
	def __init__(self):
		super(PanTiltModel, self).__init__("PanTiltModel")
		self.motorPanAngle = 0
		self.motorTiltAngle = 0