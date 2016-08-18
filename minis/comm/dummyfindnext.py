#!/usr/bin/env python

import sys
import difflib
import time
import random
import socket
import threading
from threading import Thread

import pymongo
client = pymongo.MongoClient('mongodb://129.217.193.182:38128/')
db = client.minis
coll = db.neighbour

import pigpio
name = socket.gethostname()
cnt = len(name)

TR = 26
RT = 19
baud = 9600
bits = 8

pigpio.exceptions = False
#recv=0
#sentack=0
#recv1=0
#sentack1=0

def find_in():
   recv=0 
   sentack=0
   while 1:
        x=random.randint(1,2)
	while x==1:
                if (recv!=1) :
                        pi=pigpio.pi()
                        pigpio.exceptions = False
                        pi.set_mode(TR, pigpio.INPUT)
                        pi.bb_serial_read_open(TR, baud, bits)
                        (count, data) = pi.bb_serial_read(TR)
                        time.sleep(0.1)
                        if (count==cnt) and (data!=name) :
                                In = data
                                print "My IN neighbour is",In
				recv = 1
                               	pi.stop()
                                break
                        else:
                                pi.stop()
                                break
                        pi.bb_serial_read_close(TR)
                        del count, data
                        break
		else :
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

	

def find_out():
  recv1=0
  sentack1=0	
  while 1:
        x=random.randint(1,2)
        while x==1:
                if (recv1!=1) :
                        pi1=pigpio.pi()
                        pigpio.exceptions = False
                        pi1.set_mode(RT, pigpio.INPUT)
                        pi1.bb_serial_read_open(RT, baud, bits)
                        (count1, data1) = pi1.bb_serial_read(RT)
                        time.sleep(0.1)
                        if (count1==cnt) and (data1!=name) :
                                Out = data1
                                print "My OUT neighbour is", Out
                                recv1 = 1
                                pi1.stop()
                                break
                        else:
                                pi1.stop()
                                break
                        pi1.bb_serial_read_close(RT)
                        del count1, data1
                        break
                else :
                        break

        while x==2:
                if(sentack1!="1"):
                        pi1=pigpio.pi()
                        pigpio.exceptions = False
                        pi1.set_mode(RT, pigpio.OUTPUT)
                        pi1.wave_clear()
                        pi1.wave_add_serial(RT, baud,name, bits)
                        wid1 = pi1.wave_create()
                        pi1.wave_send_once(wid1)
                        pi1.wave_delete(wid1)
                        time.sleep(0.5)
                        pi1.stop()
                        break
                else:
                        break




if __name__ == '__main__':
    Thread(target = find_in).start()
    Thread(target = find_out).start()


#db.neighbour.insert_one({"module":str(name), "In":str(In), "out":str(Out)})
