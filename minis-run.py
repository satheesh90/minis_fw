#!usr/bin/env python

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
coll = db.config	# collection 'config' says when to start the configuration  

while 1 :

        status = coll.find_one({"aspect":"status"})
	value = status.get("value")
	if value == "start":
		print "Starting..."
		break
	else:
		continue


#### Check whether it is a Sorter module - As it checks for 4 directional neighbours ###
name = socket.gethostname()
i=2

while (i<6) :
		if (i==2):
			chk = name[i]
		else:
			chk = chk + name[i]
		i = i +1
#########################################################################################

if (chk == "SORT") :

	val1 = Neighbour(19)
	val2 = Neighbour(26)
	print "In Neighbour is", val1
	print "Out Neighbour is", val2

else :
	val1 = Neighbour(26)
        val2 = Neighbour(19)
        val3 = Neighbour(5)
	val4 = Neighbour(6)
	print "In Neighbour is", val1
        print "Out Neighbour is", val2
	print "Left Neighbour is", val3
	print "Right Neighbour is", val4



#import minis.am_fw.nfc

#while 1:
#	x = minis.am_fw.nfc.read()
#	print x
#	time.sleep(.3)

#########

#import minis.auto.pps
#import minis.auto.motor

#try :
#  while 1:	
#	x = minis.auto.pps.detect(18)
#	if x == 0:
#		minis.auto.motor.InOut(24,23)
#	elif x == 1:	
#		minis.auto.motor.OutIn(24,23) 

#except KeyboardInterrupt :
#	minis.am_fw.motor.cleanup()

#finally :
#	minis.auto.motor.cleanup()
