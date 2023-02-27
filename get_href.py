from bs4 import BeautifulSoup
import requests
req = requests.get('https://google.com/')
bs = BeautifulSoup(req.text,'html.parser')
for link in bs.findAll('a'):
    print(link.get('href'))
