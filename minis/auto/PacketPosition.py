#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

def Detect(pin):
        GPIO.setup(pin, GPIO.IN)
        if(GPIO.input(pin) == GPIO.HIGH):
                return 1
        else:
                return 0


