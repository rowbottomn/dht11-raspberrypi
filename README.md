# dht11-raspberrypi
A library to drive the DHT11 using a one wire approach

In your terminal of your rasp pi:
sudo git clone https://github.com/rowbottomn/dht11-raspberrypi.git

Use this picture to see how to wire the DHT11 with a 10K resistor.  
https://tutorials-raspberrypi.de/wp-content/uploads/luftfeuchtigkeit_DHT11_Steckplatine-600x476.png
****Note that we are using the 3.3Volt pin on the Pi!****


We will do code together.


Then follow this tutorial on how to get the Pi up and running with MQTT.
https://www.arrow.com/en/research-and-events/articles/mqtt-tutorial

When it comes to setting up our own broker, follow this article on how to specifically set up a password on the pi and also what software to use as a Broker on your PC.
https://desertbot.io/blog/headless-raspberry-pi-4-mqtt-setup

To be able to do this in code
in code 
import os

then add to code with your_topic and your_data
os.system("mosquitto_pub -h [BROKER_IPADDRESS] -t \"your_topic\" -m \"your_data\"")

****Note that you must download the Windows portable version of MQTT Explorer****
https://github.com/thomasnordquist/MQTT-Explorer/releases/download/0.0.0-0.4.0-beta1/MQTT-Explorer-0.4.0-beta1.exe
