from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import requests as R
import time
import random
import json
import os
import ast
import numpy as np
from data_base1 import DataBase
from bson.objectid import ObjectId
import time

class RequestLib():
    def __init__(self):
        self.session = R.session()
        self.session.proxies = {}
        self.session.proxies['http'] = 'socks5://127.0.0.1:9050'
        self.session.proxies['https'] = 'socks5://127.0.0.1:9050'
        self.headers = {}
        self.headers['User-agent'] = UserAgent().random
        self.headers['Accept-Language'] = "en,en-US;q=0,5"
        self.headers['Content-Type'] = "application/x-www-form-urlencoded"
        self.headers['Connection'] = "keep-alive"
        self.headers['Accept'] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
    def get(self, http):
        print (http)
        get_page = self.session.get(http, headers=self.headers)#, timeout=(10, 10)) 
        return get_page.text 
    def get_img(self, http): 
        get_page = self.session.get(http, headers=self.headers)#, timeout=(20, 20)) 
        return get_page   
         
Sess = RequestLib()
http = "https://www.liveauctioneers.com/search/?keyword=rolex&sort=-relevance&status=online"
#https://www.liveauctioneers.com/search/?keyword=rolex&pageSize=48&sort=-relevance&status=online
Sess = Sess.get(http)
soup = BeautifulSoup(Sess)
J = soup.find_all('div', {"class": "card___1ZynM cards___2C_7Z"})
#Pag = soup.find('ul', {"class": "paginator___35V-U paginator___3_KwX"})
#Pag = Pag.find_all('li')
for iop in J:
   H = iop.find('img', {"class": "image___2rMaZ img-primary___vK3xm"})
   #soup = BeautifulSoup(H)
   time.sleep(1)
   print (type(H), H)#["src"])# H["src"]
#   data = H["src"].split(",")[-1]
#   data = data.encode()
#   with open("imageToSave4.png", "wb") as fh:
#       fh.write(data)
