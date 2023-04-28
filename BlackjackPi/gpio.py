import RPi.GPIO as GP
from time import sleep
#setup pins
GP.setmode(GP.BCM)
redLED = 6
blueLED = 13
yellowLED = 19
greenLED = 21
leds = [redLED,blueLED,yellowLED,greenLED]
GP.setup(leds, GP.OUT)
GP.output(leds, GP.LOW)

#LEDS FUNCTIONS
def allOff():
    GP.setmode(GP.BCM)
    GP.setup(leds, GP.OUT)
    GP.output(leds, GP.LOW)
    
   
def allOn():
    GP.setmode(GP.BCM)
    GP.setup(leds, GP.OUT)
    GP.output(leds, GP.HIGH)
    sleep(5)
    GP.output(leds, GP.LOW)

def redOn():    
    GP.setmode(GP.BCM)
    GP.setup(leds, GP.OUT)
    GP.output (leds[0], GP.HIGH),
    GP.output(leds[1], GP.LOW),
    GP.output(leds[2], GP.LOW),
    GP.output(leds[3], GP.LOW)

def blueOn():
    GP.setmode(GP.BCM)
    GP.setup(leds, GP.OUT)
    GP.output (leds[0], GP.LOW),
    GP.output(leds[1], GP.HIGH),
    GP.output(leds[2], GP.LOW),
    GP.output(leds[3], GP.LOW)

def yellowOn():
    GP.setmode(GP.BCM)
    GP.setup(leds, GP.OUT)
    GP.output (leds[0], GP.LOW),
    GP.output(leds[1], GP.LOW),
    GP.output(leds[2], GP.HIGH),
    GP.output(leds[3], GP.LOW)

def greenOn():
    GP.setmode(GP.BCM)
    GP.setup(leds, GP.OUT)
    GP.output(leds[0], GP.LOW),
    GP.output(leds[1], GP.LOW),
    GP.output(leds[2], GP.LOW),
    GP.output(leds[3], GP.HIGH)

def YellAndBlu():
    GP.setmode(GP.BCM)
    GP.setup(leds, GP.OUT)
    GP.output(leds[0], GP.LOW)
    GP.output(leds[1], GP.HIGH)
    GP.output(leds[2], GP.HIGH)
    GP.output(leds[3], GP.LOW)

def Bust():
    GP.setmode(GP.BCM)
    GP.setup(leds, GP.OUT)
    GP.output(redLED, GP.HIGH)
    sleep(0.5)
    GP.output(redLED, GP.LOW)
    sleep(0.5)
    GP.output(leds, GP.LOW)

def Blackjack():
    redOn()
    sleep(.2)
    blueOn()
    sleep(.2)
    yellowOn()
    sleep(.2)
    greenOn()
    sleep(.2)
    


#controlling lights and times
def standing():
   redOn()
   sleep(2)
   allOff()
   
def dublin():
    blueOn()
    sleep(2)
    allOff()

def splitting():
    yellowOn()
    sleep(2)
    allOff()

def hitting():
    greenOn()
    sleep(2)
    allOff()

def splitAndDouble():
    YellAndBlu()
    sleep(2)
    allOff()

def busting():
    Bust()

def blackjack():
    redOn()
    sleep(.2)
    blueOn()
    sleep(.2)
    yellowOn()
    sleep(.2)
    greenOn()
    sleep(.2)


GP.setwarnings(False)
GP.cleanup()