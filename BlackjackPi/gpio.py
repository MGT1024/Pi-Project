import RPi.GPIO as GP
from time import sleep
#
GP.setmode(GP.BCM)
redLED = 6
blueLED = 13
yellowLED = 19
greenLED = 21
# def setGPIO():
#     gpio = [6, 13,  19, 21]
#     GP.setup(gpio, GP.OUT)
#     return gpio

leds = [redLED,blueLED,yellowLED,greenLED]
GP.setup(leds, GP.OUT)
GP.output(leds, GP.LOW)

def allOff():
    GP.setmode(GP.BCM)
    GP.setup(leds, GP.OUT)
    
    
   
def allOn():
    GP.setmode(GP.BCM)
    GP.setup(leds, GP.OUT)
    GP.output(leds, GP.HIGH)
    sleep(5)
    GP.output(leds, GP.LOW)


def standing():
   GP.setmode(GP.BCM)
   GP.setup(leds, GP.OUT)
   GP.output (leds[0], GP.HIGH),
   GP.output(leds[1], GP.LOW),
   GP.output(leds[2], GP.LOW),
   GP.output(leds[3], GP.LOW)
   sleep(2)
   GP.output(leds, GP.LOW)
   
def dublin():
    GP.setmode(GP.BCM)
    GP.setup(leds, GP.OUT)
    GP.output (leds[0], GP.LOW),
    GP.output(leds[1], GP.HIGH),
    GP.output(leds[2], GP.LOW),
    GP.output(leds[3], GP.LOW)
    sleep(2)
    GP.output(leds, GP.LOW)
def splitting():
    GP.setmode(GP.BCM)
    GP.setup(leds, GP.OUT)
    GP.output (leds[0], GP.LOW),
    GP.output(leds[1], GP.LOW),
    GP.output(leds[2], GP.HIGH),
    GP.output(leds[3], GP.LOW)
    sleep(2)
    GP.output(leds, GP.LOW)
def hitting():
    GP.setmode(GP.BCM)
    GP.setup(leds, GP.OUT)
    GP.output(leds[0], GP.LOW),
    GP.output(leds[1], GP.LOW),
    GP.output(leds[2], GP.LOW),
    GP.output(leds[3], GP.HIGH)
    sleep(2)
    GP.output(leds, GP.LOW)
def splitAndDouble():
    GP.setmode(GP.BCM)
    GP.setup(leds, GP.OUT)
    GP.ouput(leds[0],GP.LOW)
    GP.output(leds[1],GP.HIGH)
    GP.output(leds[2], GP.HIGH)
    GP.output(leds[3], GP.LOW)
    sleep(2)
    GP.output(leds, GP.LOW)

def busting():
    GP.setmode(GP.BCM)
    GP.setup(leds, GP.OUT)
    GP.output(redLED, GP.HIGH)
    sleep(0.5)
    GP.output(redLED, GP.LOW)
    sleep(0.5)
    GP.output(leds, GP.LOW)

def blackjack():
    GP.setmode(GP.BCM)
    GP.setup(leds, GP.OUT)
    GP.output(leds[0], GP.HIGH)
    sleep(.2)
    GP.output(leds[0], GP.LOW),
    GP.output(leds[1], GP.HIGH),
    GP.output(leds[2], GP.LOW),
    GP.output(leds[3], GP.LOW)
    sleep(.2)
    GP.output(leds[0], GP.LOW),
    GP.output(leds[1], GP.LOW),
    GP.output(leds[2], GP.HIGH),
    GP.output(leds[3], GP.LOW)
    sleep(.2)
    GP.output(leds[0], GP.LOW),
    GP.output(leds[1], GP.LOW),
    GP.output(leds[2], GP.LOW),
    GP.output(leds[3], GP.HIGH)
    sleep(.2)
    GP.output(leds[0], GP.LOW),
    GP.output(leds[1], GP.LOW),
    GP.output(leds[2], GP.LOW),
    GP.output(leds[3], GP.LOW)



# gpio = setGPIO()


GP.cleanup()