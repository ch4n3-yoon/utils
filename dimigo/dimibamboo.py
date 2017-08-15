#!/usr/bin/python
# coding: utf-8

import requests
from bs4 import BeautifulSoup

url = 'http://dimibamboo.com/index.php/write'

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

print soup.find_all('img')[0].get('src')

for i in soup.find_all('img'):
    print i.get('src')
