#!/usr/bin/env python

import socket
import os
import pymongo

def get_ip_address():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(("8.8.8.8", 80))
	return s.getsockname()[0]


def Register():
	path = os.path.abspath("../config/mongoURI.txt")
	uri = open(path,'r')

	mongouri = uri.readlines()
	host = mongouri[0]
	port = int(mongouri[1])

	client = pymongo.MongoClient(host,port)  # Connect to the MongoDB
	db = client.minis       # Everything is dealt with a mongoDB named 'minis'
	coll = db.ilmodules	# IntraLogistics modules Collection 
	coll2 = db.nonilmodules # Non-Intralogistics modules collection

	module = socket.gethostname()
	ip = get_ip_address()
	
	###Check whether the module is configured and ready###
        try:
                f = open('../config/ModuleStatus.txt','r')
                con = f.readline()[0:-1] #**READ WITHOUT '\n' CHARACTER AT THE END
        except :
                con = "Not Ready"
        ###################################################### 
	
	
	###Check whether it is an IntraLogistics module###
	i=0
	while (i<2) :
		if(i==0):
			chk = module[i]
		else:
			chk = chk + module[i]
		i = i +1
	
	if chk=="IL" :
		coll.insert_one({"module":str(module), "ip":str(ip), "status":con})
	else :
		coll2.insert_one({"module":str(module), "ip":str(ip), "status":con})
	###################################################
	
	




