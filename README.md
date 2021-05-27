# Smart Birdwatch
AI Birdwatch Pi cam for Raspberry Pi Zero

# Purpose:

Provide a simple code for connecting with a Pi Cam and capturing a sequence of pictures after a signal is detected on a motion sensor. Pictures will be uploaded to AWS S3, where a lambda function will analyse and vote for the best picture using CNNs (https://en.wikipedia.org/wiki/Convolutional_neural_network). Best picture will be uploaded to a social network.

# Hardware:

- Solar power source (6V 3.4A Adafruit/500)
- LiIon battery pack (ICR18650-4400A x2 - 3.7v)
- Solar LiPoly Charger (Adafruit/390, will be upgraded to an UPS with circuit cut off to protect the battery / MPPT)
- IR Motion Sensor (HW-416-B ThePiHut/100283)
- Pi Cam V2
- Raspberry Pi Zero W
- Flood Lamp Case (IP65, 2 Chambers)

Hardware prototype is being built and setup diagram will be made available.

# Further goals:
- Identify bird species / age and sex
- Post facts about the species
- Smart post production done by AI
