#!/usr/bin/env python

import sys
import difflib
import time
import random
import socket
import threading
import os
import pymongo

import pigpio

pigpio.exceptions = False

def Neighbour(TR):
   name = socket.gethostname()
   length = len(name)
   recv=0 
   sentack=0
   cnt=0
   Infind=0
   baud = 9600
   bits = 8
   timeout = 10
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
                        if (count==length) and (data!=name) :
                                find = data
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
                if(cnt <= timeout):
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


if __name__ == "__main__":

	path = os.path.abspath("../config/mongoURI.txt")
	uri = open(path,'r')

	mongouri = uri.readlines()
	host = mongouri[0]
	port = int(mongouri[1])

	client = pymongo.MongoClient(host,port)
	db = client.minis       # Everything is dealt with a mongoDB named 'minis'
	coll = db.config        # collection 'config' says when to start the configuration  

	while 1 :

	        status = coll.find_one({"aspect":"status"})
	        value = status.get("value")
        	if value == "start":
#                	print "Starting..."
                	break
        	else:
                	continue


	LEFT = Neighbour(26)
	targetLEFT = open('../config/LEFT.txt','w')
	targetLEFT.write(str(LEFT))
	targetLEFT.write("\n")
	targetLEFT.close()
