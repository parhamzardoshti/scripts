'''
hacker news scraping
'''
import requests
from bs4 import BeautifulSoup


req = requests.get('https://thehackernews.com')

soup = BeautifulSoup(req.text, 'html.parser')

response = soup.find_all('a', attrs={'story-link'})

for index in response:
    print((index.text).strip())

