#!/usr/bin/env python

import socket


def get_ip_address():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(("8.8.8.8", 80))
	return s.getsockname()[0]



import pymongo
client = pymongo.MongoClient('mongodb://129.217.193.182:38128/')
db = client.minis
coll = db.iplists

def main():
	module = socket.gethostname()
	ip = get_ip_address()
	#print name, ip
	coll.insert_one({"module":str(module), "ip":str(ip)})

if __name__ == "__main__":
	main()



