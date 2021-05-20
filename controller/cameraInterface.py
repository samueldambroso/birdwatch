from datetime import datetime
from picamera import PiCamera
from time import sleep

camera = PiCamera()
storageDirectory = '/home/pi/Pictures/'

def burstPhoto():
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
	camera.close() # Release Pi Camera

def execute():
    try:
        burstPhoto()
    finally:
        destroy()

if __name__ == '__main__':
    try:
        burstPhoto()
    finally:
        destroy()