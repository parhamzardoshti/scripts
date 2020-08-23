import socket
import os

host = '127.0.0.1'
port =  4444

if not os.path.exists('./logs'):
    os.mkdir('./logs')
    os.mknod("./logs/log.txt")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    print("Server is listening at port ", port)
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            dedata = data.decode()
            if not data:
                break
            with open('./logs/log.txt', 'a') as file:
                file.write(dedata)
