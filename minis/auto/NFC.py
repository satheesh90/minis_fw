#!/usr/bin/env python

import sys
import time
import binascii

import Adafruit_PN532 as nfc

CS   = 8
MOSI = 10
MISO = 9
SCLK = 11
PN532_COMMAND_GETFIRMWAREVERSION = 0x02

nfc_r = nfc.PN532(cs=CS, sclk=SCLK, mosi=MOSI, miso=MISO)


def Status():
		response = nfc_r.call_function(PN532_COMMAND_GETFIRMWAREVERSION, 4)
		if response is None :
			print "NFC Reader Module is not Connected"
			return 0
		else :
                	ic, ver, rev, support = nfc_r.get_firmware_version()
			print('Found PN532 with firmware version: {0}.{1}'.format(ver, rev))
			return 1

def Read():
		nfc_r.begin()
		uid = nfc_r.read_passive_target()

		if uid is None:
                        return None
                else:
			uid_res=binascii.hexlify(uid)
               	        return uid_res



