# AI Birdwatch
AI Birdwatch Pi cam for Raspberry Pi Zero

Purpose:
Provide a simple code for connecting with a Pi Cam and capturing a sequence of pictures after a signal is detected on a motion sensor. Pictures will be uploaded to AWS S3, where a lambda function will analyse and vote for the best picture using CNNs (https://en.wikipedia.org/wiki/Convolutional_neural_network). Best picture will be uploaded to a social network.

Hardware prototype is being built and setup diagram will be made available.

Hardware:
- Solar power source (6V 3.4A Adafruit/500)
- LiIon battery pack (INR18650-2200A x2 - 7.4v)
- Solar LiPoly Charger (Adafruit/390, will be upgrade to a APU with circuit cut to protect the battery)
- IR Motion Sensor (HW-416-B ThePiHut/100283)
- Pi Cam V2
- Raspberry Pi Zero W
- Flood Lamp Case (IP65, 2 Chambers)
