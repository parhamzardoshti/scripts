#!/usr/bin/python2.7

import urllib2

from urllib import urlencode

data = {"username":"askar","password":"123456789"}

data_encoded = urlencode(data)

req = urllib2.Request("http://192.168.1.8/urls/auth.php",data_encoded,headers={"User-Agent":"Scanner"})

final_request = urllib2.urlopen(req)

print final_request.read()
