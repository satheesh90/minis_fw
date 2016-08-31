#!/usr/bin/env/python

from minis.auto.NFCCheck import Status
from minis.auto.NFC import Read

import time
uid_list = [None]

while 1:
       	uid = Read()
       
       	if not uid in uid_list :
       		uid_list.append(uid)
       		print uid
	else:	
		continue
