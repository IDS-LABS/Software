import time
import motorCortex
import serial
import pwm_Driver
import threading
import math

class device(threading.Thread):
		
	def __init__(self,m1,m2,model):
		threading.Thread.__init__(self)
		self.num=1
		self.parent=None
		self.Model=model
		self.i2c=1
		self.pan_id=m1
		self.tilt_id=m2
		self.pan=motorCortex.Motor()
		self.tilt=motorCortex.Motor()
		self.pan.setUpServo(self.pan_id,self.i2c)
		self.tilt.setUpServo(self.tilt_id,self.i2c)
		self.status=True
		self.pan_min=0
		self.pan_max=1.0
		self.tilt_min=0
		self.tilt_max=1
		self.range_tilt=1.0
		self.tilt_mid=0.5
		self.range_pan=1.0
		self.pan_mid=0.5
		self.pan_unit=self.range_pan/360.0
		self.tilt_unit=self.range_tilt/180.0

		self.Driver1=pwm_Driver.DRIVER()
		self.Driver1.setFreq(50,1)
		self.tilt_V=self.tilt_mid

		self.isRunning=True
		#Set Scan boundary for pan or tilt
		#pan_min=0.2
		#pan_max=0.3
		self.pan_V=self.pan_mid

	def run(self):
		while self.isRunning:
			try:
				if self.status==True:
					#print "PAN TILT ONLINE"
					#do some stuff like pan and tilt
					#Apply Modeling
					self.logitech()
					self.tilt.setServoPower(self.tilt_V)
					self.pan.setServoPower(self.pan_V)
					time.sleep(0.01)
					#print "PAN TILT ON"
				if self.status==False:
					#print "PAN TILT OFFLINE"
					self.status=True
					
			except KeyboardInterrupt:
				print "PAN TILT OFF"
				self.status=False
				self.end()
				self.Model.isRunning=False
						
	def end(self):
		self.isRunning=False
		pass

	def logitech(self):
		
		updatecmd=False
		self.status=False
		if (self.Model.tilt_V > -0.1) and ( self.Model.tilt_V < 0.1):
			self.Model.tilt_V=0
			#print "DEADZONE"
                if (self.Model.tilt_V < -0.1) or ( self.Model.tilt_V > 0.1):
                        #self.Model.tilt_V*=0.9/1.0
			updatecmd=True
			print "TILT ACTIVE", self.Model.tilt_V

		if (self.Model.pan_V > -0.1) and (self.Model.pan_V < 0.1):
			self.Model.pan_V=0
			#print "DEADZONE"	
                if (self.Model.pan_V < -0.1) or (self.Model.pan_V > 0.1):
                        #self.Model.pan_V*=0.9
			updatecmd=True
                        print "PAN ACTIVE",self.Model.pan_V

		

		if self.Model.tilt_V < 0:
			self.Model.tilt_V*=-1
			#self.Model.tilt_V=math.sqrt(self.Model.tilt_V)
			self.Model.tilt_V*=-1

		if self.Model.pan_V <0:
			self.Model.pan_V*=-1
			#self.Model.pan_V=math.sqrt(self.Model.pan_V)
			self.Model.pan_V*=-1
		#updatecmd=True
		if updatecmd==True:
			self.tilt_V=self.tilt_mid+self.Model.tilt_V*90.0*self.tilt_unit
			self.pan_V=self.pan_mid+self.Model.pan_V*180.0*self.pan_unit
			self.status=True
		
