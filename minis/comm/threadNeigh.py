#!/usr/bin/env python

import sys
import difflib
import time
import random
import socket
import threading


import pigpio

pigpio.exceptions = False

def IN(inTR):
   name = socket.gethostname()
   length = len(name)
   recv=0 
   sentack=0
   cnt=0
   Infind=0
   baud = 9600
   bits = 8
   timeout = 30
   while 1:
        x=random.randint(1,2)
	while x==1:
                if (recv!=1) :
                        pi=pigpio.pi()
                        pigpio.exceptions = False
                        pi.set_mode(inTR, pigpio.INPUT)
                        pi.bb_serial_read_open(inTR, baud, bits)
                        (count, data) = pi.bb_serial_read(inTR)
                        time.sleep(0.1)
                        if (count==length) and (data!=name) :
                                find = data
                                recv = 1
                               	pi.stop()
                                break
                        else:
                                pi.stop()
                                break
                        pi.bb_serial_read_close(inTR)
                        del count, data
                        break
		else :
			break
	

	while x==2:
                if(cnt <= timeout):
                        pi=pigpio.pi()
                        pigpio.exceptions = False
                        pi.set_mode(inTR, pigpio.OUTPUT)
                        pi.wave_clear()
                        pi.wave_add_serial(inTR, baud,name, bits)
                        wid = pi.wave_create()
                        pi.wave_send_once(wid)
                        pi.wave_delete(wid)
                        time.sleep(0.5)
                        pi.stop()
                        cnt = cnt+1
			break
                else:
  			break            
	
	if (recv == 1) and (cnt > timeout):
		return find
		break
                          
        if (recv !=1) and (cnt > timeout):
		return None
		break

