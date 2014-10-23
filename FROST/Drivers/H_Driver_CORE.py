 """@package docstring
Complete Driver Collection of supported devices by FROST OS. Support devices datasheets can be found at www.ids-labs.me.

Version 0.1
Revision October 10,2014

Author: Isaac DeSouza
Copyright IDS LABS 2014
"""

from Adafruit_I2C import Adafruit_I2C
import time
import math
import smbus
import i2c_lib

class PCA9865:

	__PCA9685_MODE1 = 0x0
	__PCA9685_PRESCALE = 0xFE

	__PCA9685_SLEEP = 0x10
	__PCA9685_RESTART = 0x80

	__SERVO_L = 0x8
	__SERVO_H = 0x9

	__PCA9685_SUBADR1 =0x2
	__PCA9685_SUBADR2 =0x3
	__PCA9685_SUBADR3 =0x4

	__LED0_ON_L= 0x6
	__LED0_ON_H =0x7
	__LED0_OFF_L =0x8
	__LED0_OFF_H =0x9

	__ALLLED_ON_L =0xFA
	__ALLLED_ON_H =0xFB
	__ALLLED_OFF_L =0xFC
	__ALLLED_OFF_H= 0xFD
	__SERVO_MULTIPLIER = 4
	
	FREQ_MIN=50
	FREQ_MAX=300

	__DEFAULT_FREQ=300
	#Valid PCA9865 I2C port values.
	__PORT_1=0x40
	__PORT_2=0x41
	
	def __init__(self,busnum=-1, debug=False,port):
		"""When creating driver objects the port for the device must be specified. Ports are integers values from 1 - 2. Returns nothing.
		"""
		if port == 0:
			try:
				self.i2c = Adafruit_I2C(PORT_1)
				print "PCA9865 Channel open on 0x40"
				self.setFreq(DEFAULT_FREQ)
			except:
				print "I2C address 0x40 not found. Check for connected port by using $ i2cdetect -y 1 on the command line"
		if port ==1:
			try:
				self.i2c = Adafruit_I2C(PORT_2)
				print "PCA9865 Channel open on 0x40"
				self.setFreq(DEFAULT_FREQ)
				
			except:
				print "I2C address 0x41 not found. Check for connected port by using $ i2cdetect -y 1 on the command line"
    	
		return
		

	def setFreq(self,freq):
		"""Sets the oscillator frequency for the PCA9865 driver. Frequency values from 50 to 300 are allowed.
		"""
		if ((freq >=FREQ_MIN) and (freq<=FREQ_MAX)):
		    prescale = self.calc_prescale(freq)
			self.i2c.write8(self.PCA9685_MODE1,0x0)
			self.i2c.write8(self.PCA9685_PRESCALE, prescale)
			print "PCA9865 frequency set to ", freq
			return
		else:
			print "Invalid input frequency. Please select a value from 50 to 300."
			return

	def __calc_prescale__(self,freq):
			"""Converts the input frequency into the appropriate values for the PCA9865 driver. See PCA9865 datasheet for more information.
			"""
        	prescale = 25000000.0
	        prescale /= 4096
        	prescale /= freq
	        prescale -= 1
		prescale=int(math.floor(prescale))
		print "Prescale set."
	    return prescale


class Adafruit_LSM303(Adafruit_I2C):
"""
Python library for Adafruit Flora Accelerometer/Compass Sensor (LSM303).
This is pretty much a direct port of the current Arduino library and is
similarly incomplete (e.g. no orientation value returned from read()
method).  This does add optional high resolution mode to accelerometer
though.

Copyright 2013 Adafruit Industries

Version 0.1

Revised October 10, 2014

Revision Author: Isaac DeSouza (IDS LABS)

Copyright 2014 IDS LABS
"""

    # Minimal constants carried over from Arduino library
    LSM303_ADDRESS_ACCEL = (0x32 >> 1)  # 0011001x
    LSM303_ADDRESS_MAG   = (0x3C >> 1)  # 0011110x
                                             # Default    Type
    LSM303_REGISTER_ACCEL_CTRL_REG1_A = 0x20 # 00000111   rw
    LSM303_REGISTER_ACCEL_CTRL_REG4_A = 0x23 # 00000000   rw
    LSM303_REGISTER_ACCEL_OUT_X_L_A   = 0x28
    LSM303_REGISTER_MAG_CRB_REG_M     = 0x01
    LSM303_REGISTER_MAG_MR_REG_M      = 0x02
    LSM303_REGISTER_MAG_OUT_X_H_M     = 0x03

    # Gain settings for setMagGain()
    LSM303_MAGGAIN_1_3 = 0x20 # +/- 1.3
    LSM303_MAGGAIN_1_9 = 0x40 # +/- 1.9
    LSM303_MAGGAIN_2_5 = 0x60 # +/- 2.5
    LSM303_MAGGAIN_4_0 = 0x80 # +/- 4.0
    LSM303_MAGGAIN_4_7 = 0xA0 # +/- 4.7
    LSM303_MAGGAIN_5_6 = 0xC0 # +/- 5.6
    LSM303_MAGGAIN_8_1 = 0xE0 # +/- 8.1


    def __init__(self, busnum=-1, debug=False, hires=False):

        # Accelerometer and magnetometer are at different I2C
        # addresses, so invoke a separate I2C instance for each
        self.accel = Adafruit_I2C(self.LSM303_ADDRESS_ACCEL, busnum, debug)
        self.mag   = Adafruit_I2C(self.LSM303_ADDRESS_MAG  , busnum, debug)

        # Enable the accelerometer
        self.accel.write8(self.LSM303_REGISTER_ACCEL_CTRL_REG1_A, 0x27)
        # Select hi-res (12-bit) or low-res (10-bit) output mode.
        # Low-res mode uses less power and sustains a higher update rate,
        # output is padded to compatible 12-bit units.
        if hires:
            self.accel.write8(self.LSM303_REGISTER_ACCEL_CTRL_REG4_A,
              0b00001000)
        else:
            self.accel.write8(self.LSM303_REGISTER_ACCEL_CTRL_REG4_A, 0)
  
        # Enable the magnetometer
        self.mag.write8(self.LSM303_REGISTER_MAG_MR_REG_M, 0x00)


    # Interpret signed 12-bit acceleration component from list
    def accel12(self, list, idx):
        n = list[idx] | (list[idx+1] << 8) # Low, high bytes
        if n > 32767: n -= 65536           # 2's complement signed
        return n >> 4                      # 12-bit resolution


    # Interpret signed 16-bit magnetometer component from list
    def mag16(self, list, idx):
        n = (list[idx] << 8) | list[idx+1]   # High, low bytes
        return n if n < 32768 else n - 65536 # 2's complement signed


    def read(self):
        # Read the accelerometer
        list = self.accel.readList(
          self.LSM303_REGISTER_ACCEL_OUT_X_L_A | 0x80, 6)
        res = [( self.accel12(list, 0),
                 self.accel12(list, 2),
                 self.accel12(list, 4) )]

        # Read the magnetometer
        list = self.mag.readList(self.LSM303_REGISTER_MAG_OUT_X_H_M, 6)
        mag = (self.mag16(list, 0),
                    self.mag16(list, 2),
                    self.mag16(list, 4),
                    0.0)    # ToDo: Calculate orientation
        y = mag[2]  # mind the weird "XZY" order - SL
        z = mag[1]
        mag = (mag[0],y,z)
        res.append(mag)
        return res


    def setMagGain(gain=LSM303_MAGGAIN_1_3):
        self.mag.write8(LSM303_REGISTER_MAG_CRB_REG_M, gain)


class LCD:
"""
Driver for 16 Characters 4 line LCD with an I2C interface.

Version 0.1

Revised October 10, 2014

Revision Author: Isaac DeSouza (IDS LABS)

Copyright 2014 IDS LABS
"""
	# LCD Address
	ADDRESS = 0x27

	# commands
	LCD_CLEARDISPLAY = 0x01
	LCD_RETURNHOME = 0x02
	LCD_ENTRYMODESET = 0x04
	LCD_DISPLAYCONTROL = 0x08
	LCD_CURSORSHIFT = 0x10
	LCD_FUNCTIONSET = 0x20
	LCD_SETCGRAMADDR = 0x40
	LCD_SETDDRAMADDR = 0x80

	# flags for display entry mode
	LCD_ENTRYRIGHT = 0x00
	LCD_ENTRYLEFT = 0x02
	LCD_ENTRYSHIFTINCREMENT = 0x01
	LCD_ENTRYSHIFTDECREMENT = 0x00

	# flags for display on/off control
	LCD_DISPLAYON = 0x04
	LCD_DISPLAYOFF = 0x00
	LCD_CURSORON = 0x02
	LCD_CURSOROFF = 0x00
	LCD_BLINKON = 0x01
	LCD_BLINKOFF = 0x00

	# flags for display/cursor shift
	LCD_DISPLAYMOVE = 0x08
	LCD_CURSORMOVE = 0x00
	LCD_MOVERIGHT = 0x04
	LCD_MOVELEFT = 0x00

	# flags for function set
	LCD_8BITMODE = 0x10
	LCD_4BITMODE = 0x00
	LCD_2LINE = 0x08
	LCD_1LINE = 0x00
	LCD_5x10DOTS = 0x04
	LCD_5x8DOTS = 0x00

	# flags for backlight control
	LCD_BACKLIGHT = 0x08
	LCD_NOBACKLIGHT = 0x00

	En = 0b00000100 # Enable bit
	Rw = 0b00000010 # Read/Write bit
	Rs = 0b00000001 # Register select bit
	backlight=LCD_BACKLIGHT
	print backlight

	#initializes objects and lcd
	def __init__(self):
	  self.lcd_device = i2c_lib.i2c_device(ADDRESS)

	  self.lcd_write(0x03)
	  self.lcd_write(0x03)
	  self.lcd_write(0x03)
	  self.lcd_write(0x02)
	  self.backlight=LCD_BACKLIGHT
	  print self.backlight
	  self.lcd_write(LCD_FUNCTIONSET | LCD_2LINE | LCD_5x8DOTS | LCD_4BITMODE)
	  self.lcd_write(LCD_DISPLAYCONTROL | LCD_DISPLAYON)
	  self.lcd_write(LCD_CLEARDISPLAY)
	  self.lcd_write(LCD_ENTRYMODESET | LCD_ENTRYLEFT)
	  sleep(0.2)

	# clocks EN to latch command
	def lcd_strobe(self, data):
	  self.lcd_device.write_cmd(data | En | self.backlight)
	  sleep(.0005)
	  self.lcd_device.write_cmd(((data & ~En) | self.backlight))
	  sleep(.0001)

	def lcd_backlight(self,on):
	  if on==1:
		     self.backlight=LCD_BACKLIGHT
		 print self.backlight
	  if on==0:
		     self.backlight=LCD_NOBACKLIGHT
	  self.lcd_strobe(self.backlight)

	def lcd_write_four_bits(self, data):
	  self.lcd_device.write_cmd(data | LCD_BACKLIGHT)
	  self.lcd_strobe(data)

	# write a command to lcd
	def lcd_write(self, cmd, mode=0):
	  self.lcd_write_four_bits(mode | (cmd & 0xF0))
	  self.lcd_write_four_bits(mode | ((cmd << 4) & 0xF0))

	# put string function
	def lcd_display_string(self, string, line):
	  if line == 1:
		 self.lcd_write(0x80)
	  if line == 2:
		 self.lcd_write(0xC0)
	  if line == 3:
		 self.lcd_write(0x94)
	  if line == 4:
		 self.lcd_write(0xD4)

	  for char in string:
		 self.lcd_write(ord(char), Rs)

	# clear lcd and set to home
	def lcd_clear(self):
	  self.lcd_write(LCD_CLEARDISPLAY)
	  self.lcd_write(LCD_RETURNHOME)
