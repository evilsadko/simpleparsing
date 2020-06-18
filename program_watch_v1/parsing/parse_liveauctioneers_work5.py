from stem import Signal
from stem.control import Controller
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import numpy as np
import requests as R
import time
import random
import json
import os
import ast
from data_base2 import DataBase
from bson.objectid import ObjectId

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
        #print (http)
        get_page = self.session.get(http, headers=self.headers)#, timeout=(10, 10)) 
        return get_page#.text 

# signal TOR for a new connection
def switchIP():
    with Controller.from_port(port = 9051) as controller:
        controller.authenticate()
        controller.signal(Signal.NEWNYM)

# get a new selenium webdriver with tor as the proxy
def my_proxy(PROXY_HOST,PROXY_PORT):
    fp = webdriver.FirefoxProfile()
    fp.set_preference("network.proxy.type", 1)
    fp.set_preference("network.proxy.socks",PROXY_HOST)
    fp.set_preference("network.proxy.socks_port",int(PROXY_PORT))

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
    
classdb = DataBase()
proxy = my_proxy("127.0.0.1", 9050)
Sess = RequestLib()
#https://www.liveauctioneers.com/search/?keyword=rolex&sort=-relevance&status=archive
#proxy.get("https://www.liveauctioneers.com/search/?keyword=rolex&sort=-relevance&status=online")
#proxy.get("https://www.liveauctioneers.com/search/?keyword=rolex&sort=-saleStart&status=archive")

#
#proxy.get("https://www.liveauctioneers.com/search/?keyword=rolex&page={}&sort=-saleStart&status=archive".format(iD))  
proxy.get("https://www.liveauctioneers.com")
proxy.find_element_by_css_selector('.link___.link-primary-weak___.link-default___3gIWR').click()
inputLog = WebDriverWait(proxy, 10).until(EC.presence_of_element_located((By.ID, "uname")))
inputLog.send_keys('vdmitriev89@gmail.com')
#
inputPass = WebDriverWait(proxy, 10).until(EC.presence_of_element_located((By.ID, "pw")))
inputPass.send_keys('robo151989')
proxy.find_element_by_css_selector('.submit___1XYKo').click()
#
try:
    last_height = proxy.execute_script("return document.body.scrollHeight")
    element = WebDriverWait(proxy, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "loggedIn___2QTzb"))
    )
finally:
    pass
#try:
#    proxy.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#    element = WebDriverWait(proxy, 10).until(
#        EC.presence_of_element_located((By.CLASS_NAME, "close-button___3kR_Z"))
#    )
#finally:
#    pass
scroll()
#"Ulysse Nardin", "Rolex"
brand = ["Ulysse Nardin", "Rolex", "Patek Philippe", "Vacheron Constantin", "Audemars Piguet", "Omega", "Chopard",
         "TAG Heuer", "Jaeger-LeCoultre", "Cartier", "Longines", "Breguet", "Breitling", "Blancpain", "Tissot",
         "Swatch", "Hublot", "Piaget", "A. Lange & Söhne", "Seiko"]
for i_b, b_d in enumerate(brand):
        for i in range(20):
                proxy.get("https://www.liveauctioneers.com/search/?keyword={}&page={}&sort=-saleStart&status=archive".format(b_d,i))  
                last_height = proxy.execute_script("return document.body.scrollHeight")
                print(last_height)
                scroll()
                html = proxy.page_source
                soup = BeautifulSoup(html, features = "html.parser")
                J = soup.find_all('div', {"class": "card___1ZynM cards___2C_7Z"})
                for iop in J:
                   img = iop.find('img', {"class": "image___2rMaZ img-primary___vK3xm"})
                   H1 = iop.find('div', {"class": "item-title-container___3j0W1"})#
                   title = H1.find('span')
                   solid = iop.find('div', {"class": "item-bids-container___3bOnR"})
                   auctioner = iop.find('div', {"class": "auctioneer-link-container___GB_Bj"})
                   auc = auctioner.find("a", {"class":"link___ link-primary-weak___ auctioneer-link___Ds7lm"}).text
                   auc1 = auctioner.find("a", {"class":"link___ link-primary-weak___ auctioneer-link___Ds7lm"})["href"]
                   href = iop.find('a', {"class": "link___ link-primary___ item-title___24bKg"})
                   date = iop.find('div', {"class": "catalog-countdown-container___2hyiX"})
                   try:
                       #print (img["src"], href["href"], title.text, solid, auctioner, date) 
                       
                       dump = {"date_action":str(date.text), "auctioner":{"href": auc1, "name":auc},
                               "link":"https://www.liveauctioneers.com" + href["href"], 
                               "title":str(title.text), "lot_sold":str(solid.text), "img_link":img["src"]}
                       classdb.create_collection("Watch")
                       idx = classdb.create_post(dump) 
                       print (dump, idx) 
                   except:
                      print ("ERROR")
                #proxy.get("https://www.liveauctioneers.com/search/?keyword=rolex&page={}&sort=-saleStart&status=archive".format(iD))  
 
#------------------------------------->  

"""
 1 Patek Philippe 4.9 2 Vacheron Constantin 4.8 3 Breguet 4.8 4 Lange & Sohne 4.8 5 Audemars Piguet 4.7 6 Jaeger-LeCoultre 4.7 7 Girard-Perregaux 4.7 8 Blancpain Watches 4.6 9 Ulysse Nardin 4.5 10 Rolex 4.5 11 Tag Heuer 4.5 12 Hublot 4.5 13 Chopard

Источник: https://expertology.ru/13-samykh-dorogikh-brendov-chasov/
"""
#proxy.quit()


