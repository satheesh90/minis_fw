
#!/usr/bin/env python

import os, sys
import time, socket

def Check():
  name = socket.gethostname()
  print name
  i=2
  while (i<6) :
        if (i==2):
                chk = name[i]
        else:
                chk = chk + name[i]
        i=i+1
  
  print chk	
  if chk == "SORT":
	neigh = open('../config/Neighbours.txt').read().splitlines()
	inhost = neigh[0]
        outhost = neigh[1]
        lefthost = neigh[2]
       	righthost = neigh[3]

  	while 1:
		if (inhost != "None"): 
                        addrin = inhost + ".local"
			res1 = os.system("sudo ping "+addrin +" -c 1 -w2 >/dev/null 2>&1")
			if res1 == 0:
				print inhost,"is alive"
				time.sleep(.5)
			else:
				print inhost,"is Dead"
				AlertMail(inhost)
                                # mongodb update for failure
				time.sleep(.5)

		if (outhost != "None"): 
                        addrout = outhost + ".local"
                        res2 = os.system("sudo ping "+addrout + " -c 1 -w2 >/dev/null 2>&1")
                        if res2 == 0:
                                print outhost,"is alive"
                                time.sleep(.5)
                        else:
                                print outhost,"is Dead"
                                AlertMail(outhost)
                                # mongodb update for failure
				time.sleep(.5)

                if (lefthost != "None"): 
                        addrleft = lefthost + ".local"
                        res3 = os.system("sudo ping "+addrleft + " -c 1 -w2 >/dev/null 2>&1")
                        if res3 == 0:
                                print lefthost,"is alive"
                                time.sleep(.5)
                        else:
                                print lefthost,"is Dead"
                                AlertMail(lefthost)
                                # mongodb update for failure
				time.sleep(.5)

                if (righthost != "None"):
                        addrright = righthost + ".local"
                        res4 = os.system("sudo ping "+addrright + " -c 1 -w2 >/dev/null 2>&1")
                        if res4 == 0:
                                print righthost,"is alive"
                                time.sleep(.5)
                        else:
                                print righthost,"is Dead"
                                AlertMail(righthost)
                                # mongodb update for failure
				time.sleep(.5)




  else: 
        neigh = open('../config/Neighbours.txt').read().splitlines()
        inhost = neigh[0]
        outhost = neigh[1]
        
        while 1:
                if (inhost != "None"):
                        addrin = inhost + ".local"
                        res1 = os.system("sudo ping "+addrin +" -c 1 -w2 >/dev/null 2>&1")
                        if res1 == 0:
                                print inhost,"is alive"
                                time.sleep(.5)
                        else:
                                print inhost,"is Dead"
  	                        AlertMail(inhost)
                                # mongodb update for failure
				time.sleep(.5)

                if (outhost != "None"):
                        addrout = outhost + ".local"
                        res2 = os.system("sudo ping "+addrout + " -c 1 -w2 >/dev/null 2>&1")
                        if res2 == 0:
                                print outhost,"is alive"
                                time.sleep(.5)
                        else:
                                print outhost,"is Dead"
                                AlertMail(outhost)
                                # mongodb update for failure
				time.sleep(.5)



def AlertMail(host):
	import smtplib
	sender = 'satheesh.selvanathan@tu-dortmund.de'
	receivers = ['satheesh.selvanathan@web.de']	

	message = """From: MINIS Alert Mail <alert@minis.mb.tu-dortmund.de>
To: Administrator <admin@minis.mb.tu-dortmund.de>
Subject : Module Failure Alert

This is an automatic e-mail to Alert the failure of one or more MINIS modules. A module named """+ host +""" has failed. Check the MINIS webdesk for more details
"""

	smtpObj = smtplib.SMTP('unimail.tu-dortmund.de')
	smtpObj.sendmail(sender, receivers, message)           
	print "Successfully sent email"
	
