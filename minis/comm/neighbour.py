#!/usr/bin/env python

import sys
import difflib
import time
import random

import pigpio

nm = "sqpa42"
#TR = 26
baud = 9600
bits = 8

pigpio.exceptions = False

def recv(TR):
		pi=pigpio.pi()
                pigpio.exceptions = False
            	pi.set_mode(TR, pigpio.INPUT)
                pi.bb_serial_read_open(TR, baud, bits)
                (count, data) = pi.bb_serial_read(TR)
                time.sleep(0.1)
                if (count==6) and (data!=name) :
                	return data
                        pi.stop()
		else :
			pi.stop()
		pi.bb_serial_read_close(TR)
		del data
		time.sleep(0.5)

def send(TR, name):
		pi=pigpio.pi()
                pigpio.exceptions = False
                pi.set_mode(TR, pigpio.OUTPUT)
                pi.wave_clear()
                pi.wave_add_serial(TR, baud,name, bits)
                wid = pi.wave_create()
                pi.wave_send_once(wid)
                pi.wave_delete(wid)
                time.sleep(0.5)
                pi.stop()
                

while True:
	x = random.randint(1,2)
	while x == 1:
		send(26, nm)
	while x == 2:
		y = recv(26)	
