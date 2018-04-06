# -*- coding: utf-8 -*-
# __Author__: Sdite
# __Email__ : a122691411@gmail.com

# 将国家代号ISO-2 和ISO-3做映射

import requests
import pickle
from bs4 import BeautifulSoup

url = 'http://doc.chacuo.net/iso-3166-1'
res = requests.get(url=url)
soup = BeautifulSoup(res.text, 'lxml')

countryTwoLettersToThree = dict()
tr_list = soup.find('tbody').find_all('tr')
for tr in tr_list:
    td = tr.find_all('td')
    countryTwoLettersToThree[td[0].get_text()] = td[1].get_text()

countryTwoLettersToThree['CW'] = 'CUW'
with open('countryTwoLettersToThree.pickle', 'wb') as f:
    pickle.dump(countryTwoLettersToThree, f)