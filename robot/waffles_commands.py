import serial
from rx import Observable, Observer

#Opens up serial communication between the Rpi and Arduino
ser = serial.Serial('/dev/ttyAMA0', 9600)


class WafflesCMD(Observer):
	#The past mood of the robot
	state = 'neutral'

	#Picks the next behavior based on current and immediate past state
	def on_next(self, x):
		state = self.state
		print(state)
		if(state == 'neutral'):
			if(x == 'happy'):
				self.purr()
			if(x == 'sad'):
				self.whine()
		elif (state == 'happy'):
			if(x == 'sleep'):
				self.sleepy_purr()
		elif (state == 'sleep'):
			if(x == 'happy'):
				self.wakeup_purr()
			if(x == 'neutral'):
				self.wakeup_purr()
		elif (state  == 'sad'):
			if(x == 'happy'):
				self.purr()

		self.state = x

	def on_error(self, e):
		print("Got error: %s" % e)

	def on_completed(self):
		print("Sequence completed")
	
	#Encodes the values for a movement or sound command for serial communication
	def make_command(self, throttle, direction, beep_freq, duration):
		start = 'CMD'
		end = 'q'
		return (start +  str(throttle) + 'z' + str(direction) + 'z' + str(beep_freq) + 'z' + str(duration) + end + '\r')

	#A special command that will clear the arduino's move queue when the robot is being petted
	def stop(self):
		return 'CMDSTOPq'	


	#TODO: Collection of predetermined "animations" for robot. Needs to be moved from arduino.
	def purr(self):
		ser.write((self.make_command(0, 0, 1000, 1000)).encode('ascii'))

	def whine(self):
		ser.write(b(self.make_command(0, 0, 1000, 1000)).encode('ascii'))

	def sleepy_purr(self):
		ser.write((self.make_command(0, 0, 1000, 1000)).encode('ascii'))
		print("sleepy_purr...")

	def wakeup_purr(self):
		ser.write((self.make_command(0, 0, 1000, 1000)).encode('ascii'))
		print("wakeup_purr!")
