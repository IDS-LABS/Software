##@package H_Motor_CORE
#Complete Motor type collection of supported devices by FROST OS. Support devices datasheets can be found at www.ids-labs.me.
#
#Version 0.1
#Revision October 10,2014
#
#\author Isaac DeSouza
#\copyright IDS LABS 2014


import time
import math
import serial
import H_Driver_CORE
from Adafruit_I2C import Adafruit_I2C

##This class defines types of supported motor drivers and methods to use them. It must be initialized with a valid i2c port.
class DC:
	 	
	__MOTOR_TYPE="DC"
	__MOTOR_CLASS=""
	__SET_UP=False
	

	def __init__(self,i2c):
		self.i2c=i2c
		print "Motor type set to DC"
		return

	#These methods define the class of controller being used. This will map out the pins to the appropriate output required. 
	##This motor driver requires 3 pins for control. pin_INA, pin_INB, pin_PWM correspond to the INA, INB, PWM pins respectively and which pins on the PCA9865 driver it is connected to. Refer to datasheets for more information.
	def setPololuVNH5019(self,pin_INA,pin_INB,pin_PWM):
		

		#Assign pins for motor use
		self.__pin_INA=pin_INA
		self.__pin_INB=pin_INB
		self.__pin_PWM=pin_PWM	
		self.__MOTOR_CLASS="VNH5019"
		self.__SET_UP=True
		return
	##This motor driver requires 3 pins for control. pin_PWMH, pin_PWML, pin_DIR correspond to the PWMH, PWML, DIR pins on the respectively and which pins on the PCA9865 driver it is connected to. Refer to datasheets for more information.
	def setPololuHPD(self,pin_dir,pin_PWMH,pin_PWML,i2c_num):
				
		#Set up motor for use
		self.__pin_PWMH=pin_PWMH
		self.__pin_PWML=pin_pin_PWML
		self.__pin_DIR=pin_DIR
		self.__MOTOR_CLASS="24v23"
		self.__SET_UP=True		

   		return
	##This connects to the servo directly to the PCA9865 driver. The pin_PWM is the pin on the PCA9865 driver it is connected to. Refer to datasheets for more information.
	def setUpServo(self,pin_PWM):
		
		
		self.pin_PWM=pin_PWM						
       	return
	##Sets the power from 0 to 100 % for motor defined. Direction is -1 or 1
	def setMotorPower(self,duty,direction):
		
		
		try:
			if  self.SET_UP==False:
				raise Exception("Motor not set up. Set up motor controller type.")
			if not abs(int(input))==1:
				raise ValueError()
		except ValueError:
				print "Invalid Direction value. Number must be -1 or 1"
		except Exception as inst:
			print inst 
		if abs(direction)==1:
			if self.MOTOR_CLASS=="VNH5019":	
				self.__sendCommand__(pin_PWM,duty)
				if direction==1:
					self.__sendCommand__(pin_INA,100)
					self.__sendCommand__(pin_INB,0)
				if direction ==(-1):
					self.__sendCommand__(pin_INA,0)
					self.__sendCommand__(pin_INB,100)
			if self.motorType=="24v23":
				self.__sendCommand__(pin_PWMH,duty)
				self.__sendCommand__(pin_PWML,duty)
				if direction==1:
					self.__sendCommand__(pin_DIR,100)
				if direction ==(-1):
					self.__sendCommand__(pin_DIR,0)
		return

	##Set the pulse width for the servo.
	def setServoPower(self,duty):
		 
        self.__sendCommand__(pin_PWM,duty)
		return

	def __sendCommand__(self,pin,pinDuty):
		#This function determines the commands required for the PCA9865 driver and sends them. 
			off=math.floor(pinDuty*4095)-1
			high,low=self.bytes(int(off))
			high=int(high)
			low=int(low)
			on_low=0x00
			on_high=0x00
			off_low=low
			off_high=high

			#Register for PWM HIGH
			LEDn_ON_L = 4*self.pin+6
			LEDn_ON_H = 4*self.pin+7
			LEDn_OFF_L= 4*self.pin+8
			LEDn_OFF_H= 4*self.pin+9

		
			#Send Commands
			self.i2c.write8(LEDn_ON_L,on_low)
			self.i2c.write8(LEDn_ON_H,on_high)
			self.i2c.write8(LEDn_OFF_L,off_low)
			self.i2c.write8(LEDn_OFF_H,off_high)
			return


