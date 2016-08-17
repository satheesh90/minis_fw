#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

def InOut(ph, en):
	GPIO.setup(ph, GPIO.OUT)
        GPIO.setup(en, GPIO.OUT)
	GPIO.output(ph, True)
	GPIO.output(en, True)

def OutIn(ph, en):
	GPIO.setup(ph, GPIO.OUT)
        GPIO.setup(en, GPIO.OUT)
        GPIO.output(ph, False)
        GPIO.output(en, True)

def SortLeft(ph, en):
	GPIO.setup(ph, GPIO.OUT)
        GPIO.setup(en, GPIO.OUT)
        GPIO.output(en, True)
        GPIO.output(ph, True)

def SortRight(ph, en):
	GPIO.setup(ph, GPIO.OUT)
        GPIO.setup(en, GPIO.OUT)
        GPIO.output(en, False)
        GPIO.output(ph, True)

def stop(ph, en):
	GPIO.setup(ph, GPIO.OUT)
        GPIO.setup(en, GPIO.OUT)
        GPIO.output(en, False)
        
def cleanup():
	GPIO.cleanup()
	

