#!/usr/bin/env python

import socket
import os
import pymongo

def get_ip_address():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(("8.8.8.8", 80))
	return s.getsockname()[0]


path = os.path.abspath("/home/pi/minis_fw/minis/config/mongoURI.txt")
uri = open(path,'r')

mongouri = uri.readlines()
host = mongouri[0]
port = int(mongouri[1])

client = pymongo.MongoClient(host,port)
db = client.minis       # Everything is dealt with a mongoDB named 'minis'
coll = db.modules	# Collections 'modules' is used for registering all the devices 

def main():
	module = socket.gethostname()
	ip = get_ip_address()
	coll.insert_one({"module":str(module), "ip":str(ip)})

if __name__ == "__main__":
	main()



