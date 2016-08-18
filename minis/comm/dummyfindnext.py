#!/usr/bin/env python

import sys
import difflib
import time
import random
import socket

import pigpio


name = socket.gethostname()
cnt = len(name)

TR = 26
baud = 9600
bits = 8

pigpio.exceptions = False

recv=0
sentack=0

while 1:
        x=random.randint(1,4)
	while x==1:
                if (recv!=1) :
                        pi=pigpio.pi()
                        pigpio.exceptions = False
                        pi.set_mode(TR, pigpio.INPUT)
                        pi.bb_serial_read_open(TR, baud, bits)
                        (count, data) = pi.bb_serial_read(TR)
                        time.sleep(0.1)
                        if (count==cnt) and (data!=name) :
                                neighbour = data
                                recv = 1
                                print "My neighbour is", neighbour
                                pi.stop()
                                break
                        else:
                                pi.stop()
                                break
                        pi.bb_serial_read_close(TR)
                        del count, data
                        break

	while x==2:
                if(sentack!="1"):
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
                        break
                else:
  			break            

#        if(recv==1) and (sentack=="1"):
#                print "neighbour identified and Acknowledged"
#                break


