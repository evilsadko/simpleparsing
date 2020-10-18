from bs4 import BeautifulSoup
#from requests import Session as R
import requests as R
import time
import random
import os
import json
from fake_useragent import UserAgent
from stem import Signal
from stem.control import Controller
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

class DATA(object):
        def __init__(self):
            self.file = {}
            self.csv = "";
            
        def parseCSV(self):
              with open(self.csv, 'r') as g:
                             for gh in g.readlines():
                                         gh = gh.split('\n')[0].split(';') 
                                         try:
                                              list = self.file[gh[0]]
                                              if gh[1] != 'no_matching_images':
                                                  convRUC = [int(i) for i in gh[1].split(':')[1].split('/')]
                                                  list.append(convRUC)
                                                  self.file[gh[0]] = list
                                              else:
                                                  list.append([])
                                                  self.file[gh[0]] = list
                                         except KeyError:
                                              pass

        def parseIMG(self, dir_name, tp):
                path = "data/"+dir_name
                print ("PARSING",path)
                valid_images = [".jpg",".png"]
                for r, d, f in os.walk(path):
                    for ix, file in enumerate(f):
                        if valid_images[0] in file or valid_images[1] in file:
                          if int(tp) == 4:
                                   self.file[file.split(".")[0]] = [os.path.join(r, file)]
                          else:         
                                   self.file[os.path.join(r, file)] = [os.path.join(r, file)]
                        if ".csv" in file:
                           self.csv = os.path.join(r, file)

path_img = "data_img/"
def create_dir(x):
   
   x = x.split("/")
   #try:
   x1 = path_img+x[2]
   try:
       os.mkdir(x1)
   except FileExistsError:
       pass
   x2 = x1+"/"+x[3]
   try:   
       os.mkdir(x2)
   except FileExistsError:
       pass
   x3 = x2+"/"+x[4]
   try:
       os.mkdir(x3)
   except FileExistsError:
       pass   
   #except:  
   #print (x[2], x[3], x[4])
   return x3
   #os.mkdir(car_info.text)

#---------------------------------------_>
class RequestLib():
    def __init__(self):
        self.session = R.session()
        self.session.proxies = {}
        #self.session.proxies['http'] = 'socks5://127.0.0.1:9050'
        #self.session.proxies['https'] = 'socks5://127.0.0.1:9050'
        self.headers = {}
        self.headers['User-agent'] = UserAgent().random
        self.headers['Accept-Language'] = "en,en-US;q=0,5"
        self.headers['Content-Type'] = "application/x-www-form-urlencoded"
        self.headers['Connection'] = "keep-alive"
        self.headers['Accept'] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
    def get(self, http):
        #print (http)
        self.headers['User-agent'] = UserAgent().random
        get_page = self.session.get(http, headers=self.headers)#, timeout=(10, 10)) 
        return get_page#.text 
Sess = RequestLib()
#---------------------------------------_>
def my_proxy(PROXY_HOST,PROXY_PORT):
    fp = webdriver.FirefoxProfile()
    #fp.set_preference("network.proxy.type", 1)
    #fp.set_preference("network.proxy.socks",PROXY_HOST)
    #fp.set_preference("network.proxy.socks_port",int(PROXY_PORT))

    fp.update_preferences()
    options = Options()
    #options.add_argument('headless')
    options.add_argument("--headless")
    #options.headless = True
    return webdriver.Firefox(options=options, firefox_profile=fp)

def scroll():
    last_height = proxy.execute_script("return document.body.scrollHeight")
    w = last_height//100
    igg = 100
    for i in range(w):
        proxy.execute_script("window.scrollTo(0, {})".format(igg))
        time.sleep(0.3)
        igg += 100

proxy = my_proxy("127.0.0.1", 9050)
                           
path = "data"

def func_(htt, dir_save):
                   #p_parse = Sess.get(htt)
                   #soup = BeautifulSoup(p_parse.text)
                   proxy.get(htt)
                   try:
                        #element = WebDriverWait(proxy, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "l-body")))
                        
                        scroll()
                   finally:
                        pass
                   def PP():
                       html = proxy.page_source
                       soup = BeautifulSoup(html)
                       
                       car_info = soup.find("span",{"class":"u-break-word"})
                       car_rate = soup.find("span",{"class":"r-button-unstyled c-round-num-block"})
                       
                       car_rate = car_rate.find("strong")
                       user_info = soup.find("div",{"class":"c-user-card__info"})
                       user_link = soup.find("a",{"class":"c-link c-link--color00 c-username c-username--wrap"})
                       #print (user_link["href"])#(car_info.text, car_rate.text)#, user_info.text)
                       
                       f_inf = open(dir_save+"/info.txt", "w")
                       f_inf.write(car_info.text+";"+car_rate.text+"\n")
                       f_inf.write(user_link["href"]+"\n")
                       f_inf.write(user_info.text+"\n")
                       f_inf.close()
                       
                       cl = soup.find_all('div', {"class": "c-slideshow__hd"})
                      
                       for K in cl:
                          Kcl = K.find("img")
                          #print (Kcl["src"], Kcl["src"].split("/")[-1])
                          response = Sess.get(htt)#R.get(Kcl["src"], headers=headers)
                          print (response)
                          if response.status_code == 200:
                              with open(dir_save+"/"+Kcl["src"].split("/")[-1], 'wb') as fli:
                                   fli.write(response.content)
                          #else:
                              #cl = PP() #func_(htt, dir_save)  

                       SEC = random.choice([2,3,4,5,3,1,1.1,1.5, 0.7])
                       time.sleep(SEC)
                   PP()  

dirn = os.walk(path)
ls = ["bmw","mercedes","audi","opel","landrover","mitsubishi","nissan","subaru","toyota","porsche","ferrari","lamborghini"]#"bmw", 
for U in dirn:
   for P in U[2]:
       fl = [os.path.join(U[0], P)]
       #print (fl)
       OP = open(fl[0],"r")
       lS = OP.readlines()
       for st in lS:
           htt = "https://www.drive2.ru"+st.split("\n")[0]
           dir_save = create_dir(st.split("\n")[0])
           if st.split("/")[2] in ls:
                 print (htt, st.split("/")[-2])
                 func_(htt, dir_save)
           #try:
#           func_(htt, dir_save)
#                   p_parse = Sess.get(htt)
#                   soup = BeautifulSoup(p_parse.text)
#                   
#                   car_info = soup.find("span",{"class":"u-break-word"})
#                   car_rate = soup.find("span",{"class":"r-button-unstyled c-round-num-block"})
#                   
#                   car_rate = car_rate.find("strong")
#                   user_info = soup.find("div",{"class":"c-user-card__info"})
#                   user_link = soup.find("a",{"class":"c-link c-link--color00 c-username c-username--wrap"})
#                   #print (user_link["href"])#(car_info.text, car_rate.text)#, user_info.text)
#                   
#                   f_inf = open(dir_save+"/info.txt", "w")
#                   f_inf.write(car_info.text+";"+car_rate.text+"\n")
#                   f_inf.write(user_link["href"]+"\n")
#                   f_inf.write(user_info.text+"\n")
#                   f_inf.close()
#                   
#                   cl = soup.find_all('div', {"class": "c-slideshow__hd"})
#                   for K in cl:
#                      Kcl = K.find("img")
#                      print (Kcl["src"], Kcl["src"].split("/")[-1])
#                      response = R.get(Kcl["src"], headers=headers)
#                      print (response)
#                      if response.status_code == 200:
#                          with open(dir_save+"/"+Kcl["src"].split("/")[-1], 'wb') as fli:
#                               fli.write(response.content)

#                   SEC = random.choice([2,3,4,5,3,1,1.1,1.5, 0.7])
#                   time.sleep(SEC)
           #except:
                   #print (htt)
                   #pass
                   #func_(htt, dir_save)
#print (dirn)
                           
