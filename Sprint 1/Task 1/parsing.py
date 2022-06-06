# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests

words = []
url = 'http://sherwoodschool.ru/vocabulary/upperintermediate/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('a', target='_blank')

for quote in quotes:
    if 'Foxinet' not in quote.text:
        words.append(quote.text.lower())
    else:
        pass
with open('words.txt', 'w+') as f1:
    if f1.read() == '':
        for i in words:
            if i != '':
                try:
                    f1.write(i + '\n')
                except UnicodeEncodeError:
                    pass
