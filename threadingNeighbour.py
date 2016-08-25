#!/usr/bin/env python 

import os
import time
import socket
import pymongo
from minis.comm.FindNeighbour import Neighbour

path = os.path.abspath("./minis/config/mongoURI.txt")
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
                print "Starting..."
                break
        else:
                continue


name = socket.gethostname()
i=2

while (i<6) :
                if (i==2):
                        chk = name[i]
                else:
                        chk = chk + name[i]
                i = i +1
#########################################################################################
import thread

def IN():
	inhost = Neighbour(29)
	print inhost
	thread.exit()
	
def OUT():
	outhost = Neighbour(19)
	print outhost
	thread.exit()
	
def LEFT():
	lefthost = Neighbour(5)
	print lefthost
	thread.exit()

def RIGHT():
	righthost = Neighbour(6)
	print righthost
	thread.exit()


if (chk != "SORT") :
				
		thread.start_new_thread(IN())
		thread.start_new_thread(OUT())

else :
		thread.start_new_thread(IN())
                thread.start_new_thread(OUT())
		thread.start_new_thread(LEFT())
                thread.start_new_thread(RIGHT())
