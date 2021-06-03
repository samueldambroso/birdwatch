1 - Select your image and burn it to the SD card
https://www.raspberrypi.org/documentation/installation/installing-images/README.md

2 - Configure your raspberrypi for remote access (headless version / 2.4ghz for Pi Zero)
https://www.raspberrypi.org/documentation/configuration/wireless/headless.md

3 - Enable remote access (your choice)
https://www.raspberrypi.org/documentation/remote-access/

Simplest way for a headless PI is adding a SSH file into the boot folder before ejecting the SD card. 
Connect to the PI once it's online using Putty and the raspberrypi IP address.

Default user / pass will be:
pi
raspberry

Once connected change your host and pass.

4 - Update your raspberry OS
https://www.raspberrypi.org/documentation/raspbian/updating.md