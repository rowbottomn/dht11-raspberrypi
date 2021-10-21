#dht11_pseudo
#Nathan Rowbottom
#Oct 18 2021
#Pseudo code to allow students to create their own program to drive the dht11 using the rasppi 
# and the dht11 library

#Import the RPi.GPIO library as GPIO <== a nice short cut
#Import the dht11 library
#Import the time library

# initialize GPIO

#call the GPIO.setmode() function and use that to set the mode to either 
#GPIO.BCM <== use GPIO pins as references
#or 
#GPIO.BOARD <== use the physical pin numbers as a reference

#GPIO.cleanup()

# read data using Pin GPIO21 
#create a variable to hold the instance of the DHT11 class we make from the 
#dht11 library.


#create our sensor loop so that we keep getting data from the sensor

    #make a variable to hold the result from the dht11 object reading the sensor
    
    #if it the result does not have an error code
    
        #display it to the screen  
        
    #since the sensor can only read so fast delay the loop for a second
    
