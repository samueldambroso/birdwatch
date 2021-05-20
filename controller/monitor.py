import RPi.GPIO as GPIO
import cameraInterface
from time import sleep

sensorPin = 11 # input for movement sensor

def setup():
	GPIO.setmode(GPIO.BOARD) # use PHYSICAL GPIO Numbering
	GPIO.setup(sensorPin, GPIO.IN) # set sensorPin to INPUT mode

def loop():
	while True:
		if hasMovementCheck():
       		cameraInterface.execute()
		else:
			delayMovementCheck()

def hasMovementCheck():
	if GPIO.input(sensorPin)==GPIO.HIGH:
		return True
	return False

def delayMovementCheck():
	sleep(0.5) # Configure a delay between checks to save energy

def destroy():
	GPIO.cleanup() # Release GPIO resource

if __name__ == '__main__':
	print ('Program is starting...')
	setup()
	try:
		loop()
	except KeyboardInterrupt: # Press ctrl-c to end the program.
		destroy()
