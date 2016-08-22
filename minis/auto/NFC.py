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
nfc_r.begin()
nfc_r.SAM_configuration()

def Read():
		uid = nfc_r.read_passive_target()
		if uid is None:
                        return None
                else:
			uid_res=binascii.hexlify(uid)
               	        return uid_res
					
