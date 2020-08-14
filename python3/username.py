import requests
from bs4 import BeautifulSoup
for i in range(1,12):
    res = requests.get('https://babynames.net/all/persian?page=%i' % i  , proxies={'https':'socks5://127.0.0.1:9050'})
    soup = BeautifulSoup(res.text , 'html.parser')
    all_names = soup.find_all('span' , attrs={'class':'result-name'})
    for name in all_names:
        name_list = (name.text).strip()
        #print(name_list)
        f = open("username.txt" , "a+")
        f.write(name_list + "\n")
        print("Done!!")
        f.close()

