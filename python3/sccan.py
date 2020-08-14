import sys

import socket
import requests
from datetime import datetime
import netifaces
# ip foundation
netifaces.ifaddresses('wlp3s0')
ipp = netifaces.ifaddresses('wlp3s0')[netifaces.AF_INET][0]['addr']



#ip = requests.get('https://api.ipify.org').text
target=ipp

# Define our tergat manually if we want ....

#if len(sys.argv) == 2:
#    target = socket.gethostbyname(sys.argv[1]) # translate hostname ti ipv4
#else:
#    print("INvalid amount of parameters")
#    print("syntax: python scanner.py <ip>")

#add a pretty banner
print("-" * 50)
print('My public IP address is: {}'.format(ipp))
print("scanning target\t" + target )
print("Time started:"+str(datetime.now()))
print("-" * 50)

try:
    for port in range(1,65000):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port)) # returns an error indicator
        #print(f'Checking port {port}')
        if result == 0:
            print(f'Port {port} is open')
        s.close()
except KeyboardInterrupt:
    print("\nExiting  program.")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved.")
    sys.exit()

except socket.error:
    print("couldn't connect to server")
    sys.exit()

