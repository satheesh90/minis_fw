#!/usr/bin/env python
import socket
import time, sys

name=socket.gethostname()

from minis.auto.NFC import Status

print "*****This program for is Testing the configuration of the MINIS module "+name+" *****"

print "(1) Checking for Adafruit PN532 NFC Reader....."
val = Status()
if(val==1):
	nfc=1
	print "NFC is configured. Proceeding to check for Packet Position Sensors..."
else :
  while 1:	
	nfc_chk = raw_input("Do you want to configure/connect the NFC Reader(y/n)?")
	if (nfc_chk == "y") or (nfc_chk == "Y"):
		print "Connect the NFC Reader and again run the 'minis-config'.."
		sys.exit()
	elif (nfc_chk == "n") or (nfc_chk == "N"):
		print "As NFC Reader is not available, it is set to NONE for this module "+name+"."
	 	nfc=0
		time.sleep(1)
		break
	else :
		print "Enter 'y' or 'n'"
		continue

print "(2) Checking for Paket Position Sensors..."
while 1:
	pps1_chk = raw_input("Is Packet Position Sensor at Position PPS1 of MINIS Board connected(y/n)? ")
	if(pps1_chk == "y") or (pps1_chk == "Y"):
		pps1 = 1
		print "Sensor at position PPS1 is 'SET' for "+name+" module"
		break
	elif(pps1_chk == "n") or (pps1_chk == "N"):
		pps1 = 0
		print "Sensor at position PPS1 is set to 'NONE' for "+name+" module"
		break
	else :
                print "Enter 'y' or 'n'"
                continue

while 1:
        pps2_chk = raw_input("Is Packet Position Sensor at Position PPS2 of MINIS Board connected(y/n)? ")
        if(pps2_chk == "y") or (pps2_chk == "Y"):
                pps2 = 1
                print "Sensor at position PPS2 is 'SET' for "+name+" module"
                break
        elif(pps2_chk == "n") or (pps2_chk == "N"):
                pps2 = 0
                print "Sensor at position PPS2 is set to 'NONE' for "+name+" module"
                break
        else :
                print "Enter 'y' or 'n'"
                continue
while 1:
        pps3_chk = raw_input("Is Packet Position Sensor at Position PPS3 of MINIS Board connected(y/n)? ")
        if(pps3_chk == "y") or (pps3_chk == "Y"):
                pps3 = 1
                print "Sensor at position PPS3 is 'SET' for "+name+" module"
                break
        elif(pps3_chk == "n") or (pps3_chk == "N"):
                pps3 = 0
                print "Sensor at position PPS3 is set to 'NONE' for "+name+" module"
                break
        else :
                print "Enter 'y' or 'n'"
                continue



print "(3) Checking for Motors Connected to the module"

i=2
while (i<6) :
        if (i==2):
                chk = name[i]
        else:
                chk = chk + name[i]
        i=i+1

if chk == "SORT" :
  while 1:
	m1_chk = raw_input("Is a Motor at position M1 of MINIS Board connected(y/n)?")
	if (m1_chk=="y") or (m1_chk=="Y"):
		m1=1
		print "Motor at position M1 is 'SET' for "+name+" module" 
		break
	elif (m1_chk=="n") or (m1_chk=="N"):
		m1=0
		print "Motor at position M1 is set to 'NONE' for "+name+" module" 
		break
	else:
		print "Enter 'y' or 'n'"
		continue

  while 1:
        m2_chk = raw_input("Is a Sorter Motor at position M2 of MINIS Board connected(y/n)?")
        if (m2_chk=="y") or (m2_chk=="Y"):
                m2=1
                print "Motor at position M2 is 'SET' for "+name+" module"
                break
        elif (m2_chk=="n") or (m2_chk=="N"):
                m2=0
                print "Motor at position M1 is set to 'NONE' for "+name+" module"
                break
        else:
                print "Enter 'y' or 'n'"
                continue

  while 1:
        m3_chk = raw_input("Is a Sorter Motor at position M3 of MINIS Board connected(y/n)?")
        if (m3_chk=="y") or (m3_chk=="Y"):
                m3=1
                print "Motor at position M3 is 'SET' for "+name+" module"
                break
        elif (m3_chk=="n") or (m3_chk=="N"):
                m3=0
                print "Motor at position M1 is set to 'NONE' for "+name+" module"
                break
        else:
                print "Enter 'y' or 'n'"
                continue

else:
  print "Since "+name+" is not a SORTER module, connect the conveyor driving motor at the position 'M1'."
  while 1:
        m1_chk = raw_input("Is a Motor at position M1 of MINIS Board connected(y/n)?")
        if (m1_chk=="y") or (m1_chk=="Y"):
                m1=1
                print "Motor at position M1 is 'SET' for "+name+" module"
                break
        elif (m1_chk=="n") or (m1_chk=="N"):
                m1=0
                print "Motor at position M1 is set to 'NONE' for "+name+" module"
                break
        else:
                print "Enter 'y' or 'n'"
                continue
			
print "nfc: ", nfc
print "pps1:", pps1
print "pps2:", pps2
print "pps3:", pps3
print "m1:", m1
print "m2:", m2
print "m3:", m3



#if __name__ == "__main__":
#	main()

