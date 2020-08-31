# -*- coding: utf-8 -*-
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import threading
import numpy as np
import cv2
import requests as R
import time
import random
import json
import os, sys
import pandas as pd
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from mongodb import DataBase

class RequestLib(object):
    def __init__(self):
        proxies = '../data_mining/misc_files/proxies/proxy_list.txt'
        with open(proxies) as file:
              self.proxy_list = [x for x in file.read().strip().split("\n") if x and x.strip()]
        self.session = R.session()
        self.session.proxies = {}
        self.headers = {}
        self.headers['User-agent'] = UserAgent().random
        self.headers['Accept-Language'] = "en,en-US;q=0,5"
        self.headers['Content-Type'] = "application/x-www-form-urlencoded"
        self.headers['Connection'] = "keep-alive"
        self.headers['Accept'] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"

    def get(self, http, proxy=False):
        #print (http)
        if proxy == False:
                self.session.proxies['http'] = 'socks5://127.0.0.1:9050'
                self.session.proxies['https'] = 'socks5://127.0.0.1:9050'
        if proxy == True:
                data = self.get_proxy()
                print (data)
                self.session.proxies['http'] = "http://{}:{}@{}:{}".format(data['login'], data['passwd'],
                                                                           data['ip'], data['port'])
                self.session.proxies['https'] = "http://{}:{}@{}:{}".format(data['login'], data['passwd'],
                                                                            data['ip'], data['port'])    
        get_page = self.session.get(http, headers=self.headers)#, timeout=(10, 10)) 
        return get_page
        
    def get_proxy(self):
        if len(self.proxy_list):
            proxy = random.choice(self.proxy_list)
            if '@' in proxy:
                 proxy = proxy.replace('@', ':')
            ip, port, login, passwd = proxy.split(':')
            return {'ip': ip, 'port': port, 'login': login, 'passwd': passwd}
        

#-------------------->
#EXCEL
excel_file = "ls.xlsx"
movies = pd.read_excel(excel_file)
temp_list = []
for i in movies.values:
     temp_list.append(i)

#--------------------->
classdb = DataBase("invest")
Sess = RequestLib()

def prime_ru():
        html = Sess.get("https://disclosure.1prime.ru/news/?p=0", True).text
        soup = BeautifulSoup(html, features = "html.parser")
        date_main = soup.find('span', {"id": "ctl00_Main_NewsDate"}).text.split(" ")[-1]
        content = soup.find('td', {"class": "center_column_container"})
        
        #print (date_main, link_page)
        J = soup.find_all('div', {"class": "news"})
        if len(J) == 50:
            link_page = content.find_all('div')[-1].find_all('a')
            for H in link_page:
                    gen_link = "https://disclosure.1prime.ru/news/"+H["href"]
                    #print (gen_link)
                    html = Sess.get(gen_link, True).text
                    soup = BeautifulSoup(html, features = "html.parser")
                    J = soup.find_all('div', {"class": "news"})
                    for i in J:
                            a_links = i.find_all('a')[0]
                            date = i.find('p', {'class':'date'}).text
                            if a_links.text in temp_list:
                               #print (a_links.text, a_links["href"], "\n")
                                      classdb.create_collection(date_main)
                                      P = classdb.see_all_post_v2(0,0,{"date":date}) 
                                      #print (P) 
                                      if P == []:
                                          #classdb.create_collection(date_main)
                                          dump = {"date":date, "site":"prime", "title":a_links.text, 
                                                  "href":"https://disclosure.1prime.ru"+a_links["href"]}
                                          classdb.create_post(dump) 
                                      else:
                                          print ("Error prime", P.keys())                                 
                                               
        else:
            link_page = []  
            for i in J:
               a_links = i.find_all('a')[0]
               date = i.find('p', {'class':'date'}).text
               if a_links.text in temp_list:
                     #print (a_links.text, a_links["href"], "\n")
                             classdb.create_collection(date_main)
                             P = classdb.see_all_post_v2(0,0,{"date":date})  
                             if P == []:
                                 classdb.create_collection(date_main)
                                 dump = {"date":date, "title":a_links.text, 
                                         "href":"https://disclosure.1prime.ru"+a_links["href"]}
                                 classdb.create_post(dump)
                             else:
                                 print ("Error prime", P.keys())    
#--------------------------->
def e_disclosure():
        url = "https://www.e-disclosure.ru/"
        html = Sess.get(url, True).text
        soup = BeautifulSoup(html, features = "html.parser")
        J = soup.find_all('table', {"class": "live noBorderTbl"})[0]
        J = J.find_all('tr')
        count = soup.find_all('div', {"class": "report"})[0]
        count = count.find("strong").text
        #print("ANSWER:",count.text)
        if count != 0:  
                for i in J:
                   temp = i.find_all("td")
                   date = temp[0].text
                   link = temp[1].find_all("a")
                   name = "%s.%s.%s" % (time.strftime("%d"), time.strftime("%m"), time.strftime("%Y"))
                   classdb.create_collection(name)
                   P = classdb.see_all_post_v2(0,0,{"date":date})
                   if P == []:
                       dump = {"date":date, "site":"disclosure", "title":link[-1].text, "href":link[-1]["href"]}
                       classdb.create_post(dump) 
                   else:
                       print ("Error disclosure", P.keys())  

if __name__ == '__main__':
        print ("START")
        #e_disclosure() 
        #prime_ru()

#http://icanhazip.com   
#Sess = RequestLib()
#print (Sess.get("http://icanhazip.com", True).text)                                                                   
#1 Перезапись данных
#2 Хранить информацию по ссылке
#3 Полная ссылка
#4 Сделать более человеческий вывод
#5 Вывод начиная с последней новости
