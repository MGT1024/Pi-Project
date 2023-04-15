import RPi.GPIO as GP
from time import sleep
from Blackjack_BasicStrat import *
from basicStrategyDict import *

HIT = False
SPLIT = False
DOUBLE = False
STAND= False
BUST = False
DEBUG = False

GP.setmode(GP.BCM)
GP.setup(6, GP.OUT, initial=GP.LOW)
GP.setup(13, GP.OUT, initial=GP.LOW)
GP.setup(19, GP.OUT, initial=GP.LOW)
GP.setup(21, GP.OUT, initial=GP.LOW)



#lights = next move (GREEN = HIT/YELLOW = DOUBLE/ RED = STAND)
lights = {
    'red': {'led':6},
    'blue': {'led': 13},
    'yellow': {'led': 19},
    'green': {'led': 21},
}
leds = [6,13,19,21]

# for key in lights.keys():
#     GP.setup(leds[key]["led"], GP.OUT)

def allOn():
        for i in leds:
            GP.output(leds[i], GP.HIGH)

def allOff():
        for i in leds:
            GP.output(leds[i], GP.LOW)


if STAND:
        GP.output(leds[3], GP.HIGH)
elif DOUBLE:
    GP.output(leds[1], GP.HIGH)

elif SPLIT:
    GP.output(leds[2], GP.HIGH)

elif HIT:
   GP.output(leds[3], GP.HIGH)
    
elif BUST:
    GP.output(6, GP.HIGH)
    sleep(0.5)
    GP.output(6, GP.LOW)
    sleep(0.5)
    




GP.cleanup()
