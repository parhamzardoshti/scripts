import sys

import requests
import socket
from datetime import datetime


# Define our tergat
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) # translate hostname ti ipv4
else:
    print("Imvalid amount of parameters")
    print("syntax: python scanner.py <ip>")

#add a pretty banner
print("-" * 50)
print("scanning target" + target)
print("Time started:"+str(datetime.now()))
print("-" * 50)

try:
    for port in range(1,65535):
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

