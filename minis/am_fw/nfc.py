#!/usr/bin/env python

import sys
import time
import binascii

import Adafruit_PN532 as nfc

def init():
		
                CS   = 8
                MOSI = 10
                MISO = 9
                SCLK = 11
                nfc_r = nfc.PN532(cs=CS, sclk=SCLK, mosi=MOSI, miso=MISO)
                nfc_r.begin()

		ic, ver, rev, support = nfc_read.get_firmware_version()
		print('Found PN532 with firmware version: {0}.{1}'.format(ver, rev))

def read():
                CS   = 8
                MOSI = 10
                MISO = 9
                SCLK = 11
                nfc_r = nfc.PN532(cs=CS, sclk=SCLK, mosi=MOSI, miso=MISO)
                nfc_r.begin()

		uid = nfc_r.read_passive_target()
                
		while True:
			if uid is None:
                                continue
                        else :
				uid_res=binascii.hexlify(uid)
                        	return  uid_res
                        	

