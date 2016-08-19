#!usr/bin/env python

import RPi.GPIO as GPIO
import os

shut = 39

GPIO.setmode(GPIO.BCM)

GPIO.setup(shut, GPIO.IN, pull_up_down=GPIO.PUD_UP) 

try:
    GPIO.wait_for_edge(shut, GPIO.FALLING)
    os.system("sudo shutdown -h now")

except:
    pass

GPIO.cleanup()
