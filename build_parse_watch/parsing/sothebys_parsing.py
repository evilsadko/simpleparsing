from stem import Signal
from stem.control import Controller
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
from pynput.mouse import Button, Controller

from bs4 import BeautifulSoup
import numpy as np
import cv2
import requests as R
import time
import random
import json
import os
import ast
import io
from data_base_work import DataBase
from bson.objectid import ObjectId
import scipy.interpolate as si


# get a new selenium webdriver with tor as the proxy
def my_proxy(PROXY_HOST,PROXY_PORT):
    fp = webdriver.FirefoxProfile()
    #fp.set_preference("network.proxy.type", 1)
    #fp.set_preference("network.proxy.socks",PROXY_HOST)
    #fp.set_preference("network.proxy.socks_port",int(PROXY_PORT))

    fp.update_preferences()
    options = Options()
    #options.add_argument('headless')
    #options.add_argument("--headless")
    #options.headless = True
    return webdriver.Firefox(options=options, firefox_profile=fp)

def scroll():
    w = last_height//100
    igg = 100
    for i in range(w):
        proxy.execute_script("window.scrollTo(0, {})".format(igg))
        time.sleep(0.3)
        igg += 100
"""
{"name": lot.Brand,
 "name": lot.Model,
 "created_at": lot.Date_action, +
 "estimate_price": lot.Price, +
 "cost ": lot.Lot_sold +
 "extra_data": { "auctioneer": lot.Auctioner, +
               "info": lot.Info,
               "lot": { "id": lot.Lot_id, +
                          "sold": lot.Lot_sold, +
                      }
               },
  "name": lot.Title, +
  "text": lot.Title, +
  "slug": lot.Link, +
  
  "image": lot.Img_link +
}
"""

if __name__ == "__main__":
        #classdb = DataBase()
        #proxy = my_proxy("127.0.0.1", 9050)
        outfile = open('data.txt', 'w')
        proxy = my_proxy("127.0.0.1", 9050)
        #proxy = my_proxy("198.46.160.38", 8080)
        #proxy = my_proxy('111.111.111.111', 1111)
        #Sess = RequestLib()
        proxy.get("https://www.sothebys.com/en/results?locale=en")#search?keyword=rolex&upcoming=false
        last_height = proxy.execute_script("return document.body.scrollHeight")
        scroll()
        html = proxy.page_source
        soup = BeautifulSoup(html, features="lxml")
        J = soup.find_all('a', {"class": "Card-info-container"})
        #print (J)
        #temp_list = []
        data = {}
        for IX, i in enumerate(J[:]):
            auctioneer = i.find('div', {'class':'Card-title'}).text
            print (auctioneer)
            created_at = i.find('div', {'class':'Card-details'}).text
            print (created_at)
            proxy.get(i["href"])
            try:
            #css-1b67vvn css-1l934fo - select
            #css-1x64id9 
               _button = WebDriverWait(proxy, 10).until(EC.element_to_be_clickable((By.CLASS_NAME ,"css-1l934fo")))
               _button.click()
            except:
               print ("ERROR")
            scroll()
            html = proxy.page_source
            soup = BeautifulSoup(html, features="lxml")
            time.sleep(random.choice([1,2,0.5]))
            K = soup.find_all('a', {"class": "css-ytumd6"})
            lots = {}
            for IIX, ii in enumerate(K[:-1]):
                slug = ii["href"]
                try:
                        image = ii.find('img', {'class':'css-1qefrf4'})["src"]
                        #print (image)
                except:
                        image = ""        
                name = ii.find('p', {'class':'css-noralg-p-small-regular'}).text
                id_lot = ii.find('h4', {'class':'css-18iadgp-h4-regular'}).text
                estimate_price = ii.find_all('h4', {'class':'css-xnoh5a'})[-1].text
                try:
                   #cost = ii.find('span', {'class':'css-8fe5tn-label-bold'}).text
                   sold = ii.find('span', {'class':'css-8fe5tn-label-bold'}).text
                   print (sold)
                except:
                   sold = 0
                temp_data = { "brand": "", "model": "",
                               "created_at": created_at,
                               "estimate_price": estimate_price,
                               "cost ": sold,
                               "extra_data": { "auctioneer": auctioneer, "info": "", "lot": {"id": id_lot, "sold": sold}},
                               "name": name,
                               "text": name, 
                               "slug": slug,
                               "image": image                        
                            }
                print (temp_data)  
                lots[IIX] = temp_data          
            data[IX] = lots
        json.dump(data, outfile)
                                 
            #temp_list.append(i["href"])
            #a class="css-ytumd6"
            #div Card-title
            
#        
#        for i in J:
#             proxy.get(i["href"])
#             scroll()
#             html = proxy.page_source
#             soup = BeautifulSoup(html, features="lxml")
#             time.sleep(random.choice([1,2,0.5]))
#         json.dump(data, outfile)
#https://www.drove.com/campaign/5f33d93d6345a20001f960d3?utm_medium=whatsapp&skey=.2ald
