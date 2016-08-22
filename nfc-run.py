#!/usr/bin/env/python

from minis.auto.NFCCheck import Status
from minis.auto.NFC import Read

import time

Status()

while 1:
       	uid = Read()
       	uid_list = [None]
	
	if uid in uid_list :
		continue
	else:	
		print uid
		uid_list.append(uid)
		print "uid_list", uid_list
		#break
