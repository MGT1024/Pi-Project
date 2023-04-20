from tkinter.ttk import LabeledScale
from turtle import hideturtle
from xmlrpc.server import SimpleXMLRPCDispatcher
import RPi.GPIO as GP
from time import sleep

HIT = False
SPLIT = False
DOUBLE = False
STAND = False
BUST = False

GP.setmode(GP.BCM)
six = 6
tTeen = 13
nTeen = 19
tOne = 21
def setGPIO():
    gpio = [6, 13,  19, 21]
    GP.setup(gpio, GP.OUT)
    return gpio
# lights = {
#     'red': 6,
#     'blue': 13,
#     'yellow': 19,
#     'green': 21,

# }
leds = [six,tTeen,nTeen,tOne]
GP.setup(leds, GP.OUT)
GP.output(leds, GP.LOW)

def allOff():
    GP.output(leds, GP.LOW)
    
   
def allOn():
    GP.output(leds, GP.HIGH)
    sleep(5)


def standing():
   GP.output (leds[0], GP.HIGH),
   GP.output(leds[1], GP.LOW),
   GP.output(leds[2], GP.LOW),
   GP.output(leds[3], GP.LOW)
   sleep(8)
   
def dublin():
    GP.output (leds[0], GP.LOW),
    GP.output(leds[1], GP.HIGH),
    GP.output(leds[2], GP.LOW),
    GP.output(leds[3], GP.LOW)
    sleep(8)
def splitting():
    GP.output (leds[0], GP.LOW),
    GP.output(leds[1], GP.LOW),
    GP.output(leds[2], GP.HIGH),
    GP.output(leds[3], GP.LOW)
    sleep(8)
def hitting():
    GP.output (leds[0], GP.LOW),
    GP.output(leds[1], GP.LOW),
    GP.output(leds[2], GP.LOW),
    GP.output(leds[3], GP.HIGH)
    sleep(8)
def busting():
    GP.output(six, GP.HIGH)
    sleep(0.5)
    GP.output(six, GP.LOW)
    sleep(0.5)

if STAND :
    standing()
elif DOUBLE:
    dublin()
elif SPLIT:
    splitting()
elif HIT:
    hitting()
elif BUST:
    busting()
    busting()
    busting()
    busting()
    busting()
    busting()
    busting()
    busting()
else: allOff()

gpio = setGPIO()


GP.cleanup()