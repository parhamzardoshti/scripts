#!/usr/bin/python2.7

import socket,sys

host = sys.argv[1]
port = int(sys.argv[2])

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
    sock.connect((host,port))
    print "[+] Connection Done !"
except socket.error:
    print "[+] Error !!! :("

sock.send("Hi\n")
