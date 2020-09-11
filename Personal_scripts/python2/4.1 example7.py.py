#!/usr/bin/python2.7

import urllib2,sys

host = sys.argv[1]
dfile = sys.argv[2]

data = open(dfile,"r")
fdata = data.readlines()

for line in fdata:
    linewn = line.strip("\n")
    strreq = "{0}/{1}".format(host,linewn)
    try:
        req = urllib2.urlopen(strreq)
        if req.code == 200:
            print "[+] {0}/{1} is Found (200)".format(host,linewn)
    except:
        pass
