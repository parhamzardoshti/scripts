#!/usr/bin/python2.7

import socket,sys

target = sys.argv[1]

ports = range(1,10001)

for port in ports:
    try:
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	sock.settimeout(0.1)
        if sock.connect_ex((target,port)) == 0:
            print "[+]The port {0} is Opened".format(port)
        #else:
        #    print "[!]The port {0} is Closed".format(port)
    except socket.error:
        print "[!] Error with socket !"
