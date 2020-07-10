from bs4 import BeautifulSoup
#from requests import Session as R
import requests as R
import time
import random
import os
import json

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
open_f = open("data_cars_w.txt").readlines()

for H in open_f:
   idx = 0 #1199 max
   size_sort = 0
   file_open = open("data/"+H.split(";")[0]+".txt","w")
   link_parse = "https://www.drive2.ru" + H.split(";")[1]
   get_f_page = R.get(link_parse, headers=headers)
   soup = BeautifulSoup(get_f_page.text)
   #cl = soup.find_all('div', {"class": "o-grid"})   
   cl = soup.find_all('a', {"class": "u-link-area"})
   for HJ in cl:
       file_open.write(HJ.get('href')+"\n")
       print (HJ.get('href'))
   while idx != 60:
              SEC = random.choice([2,3,4,5,3,1,1.1,1.5, 0.7])
   
              #os.mkdir(H.split(";")[0])
              new_link = "https://www.drive2.ru/ajax/carsearch.cshtml?context={}&start={}&sort=Drive&index={}".format(H.split(";")[-1], size_sort, idx)
              
              get_f_page = R.get(new_link, headers=headers)
              try:
                      Js = json.loads(get_f_page.text)
                      #print (Js["html"])
                      soup = BeautifulSoup(Js["html"])
                      cl = soup.find_all('a', {"class": "u-link-area"})
                      if len(cl) != 0:
                         for K in cl:
                            file_open.write(K.get('href')+"\n")
                            print (K.get('href'))
                      print (idx, size_sort)
                      idx +=1
                      size_sort += 20
                      time.sleep(SEC) 
              except json.decoder.JSONDecodeError:
                      print (get_f_page, "Error Decode")
              except KeyError:
                      idx = 60
                      print (get_f_page.text, "KeyError")        
                      
   file_open.close() 
