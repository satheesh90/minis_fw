#!usr/bin/env python

import os
import time
import pymongo
from minis.comm.findNeigh import Neighbour

path = os.path.abspath("/home/pi/minis_fw/minis/config/mongoURI.txt")
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

val1 = Neighbour(26)
val2 = Neighbour(19)
print "In Neighbour is", val1
print "Out Neighbour is", val2






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
