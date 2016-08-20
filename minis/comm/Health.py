#!/usr/bin/env python

import sh, time
import socket

def Check():

	name = socket.gethostname()
	i=2
	while (i<6) :
                if (i==2):
                        chk = name[i]
                else:
                        chk = chk + name[i]
                i=i+1
	#s = open('../config/Neighbours.txt','r')

	#if chk == "SORT":
	inhost = "ILCURV01"
	outhost = "ILLONG01"
	lefthost = "ILMANY01"
	righthost = "ILDUMM03"
	x=1
	while 1:
	 	if (inhost != "None") and (x==1):
			addrin = inhost + ".local"
			try :
				sh.ping(addrin) # "-c 1", _out="/dev/null")
				print inhost, "is healthy"
				x=x+1
			except sh.ErrorReturnCode_1:
					print inhost, "is dead"
					x=x+1

		elif (outhost != "None") and (x==2):
                                addrout = outhost + ".local"
                                try :
                                        sh.ping(addrin, "-c 1", _out="/dev/null")
                                        print outhost, "is healthy"
					x=x+1
				except sh.ErrorReturnCode_1:
                                        print outhost, "is dead"
					x=x+1

		elif (lefthost != "None") and (x==3):
                                addrleft = lefthost + ".local"
                                try :
                                        sh.ping(addrleft, "-c 1", _out="/dev/null")
                                        print lefthost, "is healthy"
					x=x+1
				except sh.ErrorReturnCode_1:
                                        print lefthost, "is dead"
					x=x+1
		elif (righthost != "None") and (x==4):
                                addrright = righthost + ".local"
                                try :
                                        sh.ping(addrright, "-c 1", _out="/dev/null")
                                        print righthost, "is healthy"
					x=1
				except sh.ErrorReturnCode_1:
                                        print righthost, "is dead"
					x=1

#def AlertEmail()

Check()
