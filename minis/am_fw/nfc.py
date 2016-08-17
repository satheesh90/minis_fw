#!/usr/bin/env python

import sys
import time
import binascii

import Adafruit_PN532 as nfc

CS   = 8
MOSI = 10
MISO = 9
SCLK = 11
nfc_r = nfc.PN532(cs=CS, sclk=SCLK, mosi=MOSI, miso=MISO)
nfc_r.begin()

def status():
		
                ic, ver, rev, support = nfc_r.get_firmware_version()
		print('Found PN532 with firmware version: {0}.{1}'.format(ver, rev))

def read():

		uid = nfc_r.read_passive_target()
                
		
		if uid is None:
                                return None
                else:
			uid_res=binascii.hexlify(uid)
               	        return uid_res        	


