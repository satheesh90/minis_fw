#!usr/bin/env python

import sys
import os, time

#import minis.am_fw.nfc

#while 1:
#	x = minis.am_fw.nfc.read()
#	print x
#	time.sleep(.3)

#########

import minis.auto.pps
import minis.auto.motor

try :
  while 1:	
	x = minis.auto.pps.detect(18)
	if x == 0:
		minis.auto.motor.InOut(24,23)
	elif x == 1:	
		minis.auto.motor.OutIn(24,23) 

#except KeyboardInterrupt :
#	minis.am_fw.motor.cleanup()

finally :
	minis.auto.motor.cleanup()
