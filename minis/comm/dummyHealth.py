
#!/usr/bin/env python

import os
import time, socket

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
			res1 = os.system(addrin +" -c 1 -w2 >/dev/null 2>&1")
			if res1 == 0:
				print inhost,"is alive"
				x=x+1
				time.sleep(1)
			else:
				print inhost,"is Dead"
				x=x+1
				time.sleep(1)

		elif (outhost != "None") and (x==2):
                        addrout = outhost + ".local"
                        res2 = os.system(addrout + " -c 1 -w2 >/dev/null 2>&1")
                        if res2 == 0:
                                print outhost,"is alive"
                                x=x+1
				time.sleep(1)
                        else:
                                print outhost,"is Dead"
                                x=x+1
				time.sleep(1)

                elif (lefthost != "None") and (x==3):
                        addrleft = lefthost + ".local"
                        res3 = os.system(addrleft + " -c 1 -w2 >/dev/null 2>&1")
                        if res3 == 0:
                                print lefthost,"is alive"
                                x=x+1
				time.sleep(1)
                        else:
                                print lefthost,"is Dead"
                                x=x+1
				time.sleep(1)

                elif (righthost != "None") and (x==4):
                        addrright = righthost + ".local"
                        res4 = os.system(addrright + " -c 1 -w2 >/dev/null 2>&1")
                        if res4 == 0:
                                print righthost,"is alive"
                                x=1
				time.sleep(1)
                        else:
                                print righthost,"is Dead"
                                x=1
				time.sleep(1)


Check()
