# Smart Birdwatch
AI Birdwatch Pi cam for Raspberry Pi Zero

# Purpose:

Provide a simple code for connecting with a Pi Cam and capturing a sequence of pictures after a signal is detected on a motion sensor. Pictures will be uploaded to AWS S3, where a lambda function will analyse and vote for the best picture using CNNs (https://en.wikipedia.org/wiki/Convolutional_neural_network). Best picture will be uploaded to a social network.

# Hardware:

- Solar power source (6V 3.4A Adafruit/500)
- LiIon battery pack (ICR18650-4400A x2 - 3.7v)
- Polulu voltage regulator (S7V8F5 - IN 2.7v~11v / OUT 5.2v)
- Solar LiPoly Charger (Adafruit/390, will be upgraded to an UPS with circuit cut off to protect the battery / MPPT)
- IR Motion Sensor (HW-416-B ThePiHut/100283)
- Pi Cam V2
- Raspberry Pi Zero W
- Flood Lamp Case (IP65, 2 Chambers)

# Progress:

> Flood light case
<img src="https://github.com/samueldambroso/birdwatch/blob/main/hardware/1-floodlight.jpg" width=50% height=50%>

> Power components
<img src="https://github.com/samueldambroso/birdwatch/blob/main/hardware/2-powercomponents.jpg" width=50% height=50%>

> Assembled power chamber
<img src="https://github.com/samueldambroso/birdwatch/blob/main/hardware/3-powerchamber.jpg" width=50% height=50%>

> Step up/Step down (Polulu 5.2v)
<img src="https://github.com/samueldambroso/birdwatch/blob/main/hardware/4-polulu5v.jpg" width=50% height=50%>

> Attaching polulu
<img src="https://github.com/samueldambroso/birdwatch/blob/main/hardware/5-poluluattached.jpg" width=50% height=50%>

> Output test
<img src="https://github.com/samueldambroso/birdwatch/blob/main/hardware/6-outtest.jpg" width=50% height=50%>

> Input test
<img src="https://github.com/samueldambroso/birdwatch/blob/main/hardware/7-intest.jpg" width=50% height=50%>

> Power chamber done
<img src="https://github.com/samueldambroso/birdwatch/blob/main/hardware/8-powerchamberdone.jpg" width=50% height=50%>

Hardware prototype is being built and setup diagram will be made available.

# Further goals:
- Identify bird species / age and sex
- Post facts about the species
- Smart post production done by AI
