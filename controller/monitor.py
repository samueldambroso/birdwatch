import RPi.GPIO as GPIO
from datetime import datetime
from picamera import PiCamera
from time import sleep	

sensorPin = 11 # input for movement sensor
camera = PiCamera()
storageDirectory = '/home/pi/Pictures/'

def setup():
	GPIO.setmode(GPIO.BOARD) # use PHYSICAL GPIO Numbering
	GPIO.setup(sensorPin, GPIO.IN) # set sensorPin to INPUT mode

def loop():
	while True:
		if hasMovementCheck():
			capturePhotoSession()
		else :
			delayMovementCheck()

def hasMovementCheck():
	if GPIO.input(sensorPin)==GPIO.HIGH:
		return True
	return False

def delayMovementCheck():
	sleep(5)

def capturePhotoSession():
	camera.start_preview()
	for index in range(1,5):
		capturePhoto()
		sleep(1)
	camera.stop_preview()

def capturePhoto():
	pictureName = formatPictureName()
	picturePath = storageDirectory + pictureName + '.jpg'
	camera.capture(picturePath)

def formatPictureName():
	now = datetime.now()
	formattedName = now.strftime("%m%d%Y%H%M%S")
	return formattedName

def destroy():
	GPIO.cleanup() # Release GPIO resource
	camera.close() # Release Pi Camera

if __name__ == '__main__':
	print ('Program is starting...')
	setup()
	try:
		loop()
	except KeyboardInterrupt: # Press ctrl-c to end the program.
		destroy()
