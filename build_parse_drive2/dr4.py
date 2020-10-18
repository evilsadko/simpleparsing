from bs4 import BeautifulSoup
#from requests import Session as R
import requests as R
import time
import random
import os
import json

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

                           
path = "data"

dirn = os.walk(path)
#ls = ["bmw","mercedes","audi","opel","landrover","mitsubishi","nissan","subaru","toyota","porsche","ferrari","lamborghini"]
ls = ["honda", "lada", "tesla","peugeot","acura","alfaromeo","infiniti", "mazda"]
for U in dirn:
   for P in U[2]:
       fl = [os.path.join(U[0], P)]
       #print (fl)
       OP = open(fl[0],"r")
       lS = OP.readlines()
       for st in lS:
           htt = "https://www.drive2.ru"+st.split("\n")[0]
           print (htt)
           
           if st.split("/")[2] in ls:
               dir_save = create_dir(st.split("\n")[0])
               try:
                       p_parse = R.get(htt, headers=headers)
                       soup = BeautifulSoup(p_parse.text)
                       
                       car_info = soup.find("span",{"class":"u-break-word"})
                       car_rate = soup.find("span",{"class":"r-button-unstyled c-round-num-block"})
                       
                       car_rate = car_rate.find("strong")
                       user_info = soup.find("div",{"class":"c-user-card__info"})
                       user_link = soup.find("a",{"class":"c-link c-link--color00 c-username c-username--wrap"})
                       print (user_link["href"])#(car_info.text, car_rate.text)#, user_info.text)
                       
                       f_inf = open(dir_save+"/info.txt", "w")
                       f_inf.write(car_info.text+";"+car_rate.text+"\n")
                       f_inf.write(user_link["href"]+"\n")
                       f_inf.write(user_info.text+"\n")
                       f_inf.close()
                       
                       cl = soup.find_all('div', {"class": "c-slideshow__hd"})
                       for K in cl:
                          Kcl = K.find("img")
                          print (Kcl["src"], Kcl["src"].split("/")[-1])
                          response = R.get(Kcl["src"], headers=headers)
                          print (response)
                          if response.status_code == 200:
                              with open(dir_save+"/"+Kcl["src"].split("/")[-1], 'wb') as fli:
                                   fli.write(response.content)

                       SEC = random.choice([2,3,4,5,3,1,1.1,1.5, 0.7])
                       time.sleep(SEC)
               except:
                       pass
#print (dirn)
                           
