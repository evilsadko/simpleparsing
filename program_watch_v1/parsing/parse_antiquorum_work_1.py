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
         
def utils_help(x):
    y = []
    for i in x:
       temp = i.text
       temp = temp.split("\t")
       t0 = [i for i in temp[0].split(" ")[1:-2]]
       t0.append(temp[1].split(" ")[1])
       y.append(t0)
    return y   
       

def create_dir(x):
   x = "antiquorum/"+x
   try:
       os.mkdir(x)
   except FileExistsError:
       pass
   return x    
       

def func_info(x):
    soup = BeautifulSoup(x)
    l = soup.find_all("p")
    #print (l)#[0]
    G = {}
    for i in l[:]:
        t = i.find("strong")
        P = i.text.split(t.text)
        #print (t.text, P[-1])#[0]
        #tt = string_form(i.text.split(" "))
#        try:
#           J = P[-1].split(",")[0]
#        except:
#           J = P[-1]
        t = t.text.replace("\u2003", "").replace('“','').replace('”','').replace('.','').replace('’’’', '').replace('.', '').replace('"',"").replace("'","").replace("\n", "").replace("\r", "")   
        J = P[-1].replace("\u2003", "").replace('“','').replace('”','').replace('.','').replace('’’’', '').replace('.', '').replace('"',"").replace("'","").replace("\n", "").replace("\r", "") 
#        #G.append({t:J})
        G[t] = J
    #print (G)
    return G     

def dict_brand():
        BR = {}
        R = open("watch_mark.txt", "r").readlines()
        for r in R:
          r = r.split("\n")[0].split(";")
          #print (r[0], r[1]) 
          BR[r[1]]=r[0]      
        return BR

class DATA(object):
        def __init__(self):
            self.txt = {}
            self.file = {}
            
        def parseIMG(self, dir_name):
                path = "{}/".format(dir_name)
                print ("PARSING",path)
                for r, d, f in os.walk(path):
                    for ix, file in enumerate(f):
                        #print (file)
                        if ".jpg" in file:
                           self.file[file.split(".")[0]] = [os.path.join(r, file)]
                        if ".txt" in file:
                           self.txt[file.split(".")[0]] = [os.path.join(r, file)]

Brand = {}
Model = {}
def ModelSee():
        #classDB.create_collection("Watch")#"Model"
        classDB.create_collection("Brand") 
        LX = classDB.see_post({"BrandName":"Vulcain"})
        #print (LX)
        classDB.create_collection("Model") 
        #print (classDB.see_all_post())
        print (list(classDB.find_many_post({"brend_id":LX["_id"]})))
def func_stat():
        classDB.create_collection("Brand")
        r1 = classDB.see_all_post()
        for u in r1:
           classDB.create_collection("Model") 
           posts_ = classDB.find_many_post({"brend_id":ObjectId(u['_id'])})
           #print (list(posts_))
           classDB.create_collection("Brand")
           classDB.upd_post(ObjectId(u['_id']), {"list":list(posts_)})       
def createDB_1():
        name_t = "create_temp_bd.json"
        D = DATA()
        D.parseIMG("model_mark")
        B = dict_brand()
        D = D.txt
        for ixx, i in enumerate(D.keys()):
           F = open(D[i][0], "r").readlines()
           
           #print (B[i], i)
           M = []
           for p in F:
               p = p.split(";")
               print (p[0], p[1])
               M.append({"WorkName":p[1], "ModelName":p[0]})
           Brand[ixx] = {"BrandName":B[i], "WorkName":i, "models": M}
        A = open(name_t, "w")
        json.dump(Brand, A)
        A.close()   
        #OPEN
#--------------------------------------------------------->        
        A = open(name_t, "r")
        A = json.load(A)
        Midx = 0
        Bidx = 0
        for i in A.keys():
            classDB.create_collection("Brand")
            obj = {"BrandName":A[i]["BrandName"],
                   "WorkName":A[i]["WorkName"]}
            idx = classDB.create_post(obj) 
            Bidx += 1
            if A[i]["models"] != []:
               classDB.create_collection("Model")
               for K in A[i]["models"]:
                   Midx +=1
                   K["brend_id"] = idx
                   classDB.create_post(K)              
        
        func_stat()

def createDB():
        F = open("watch_mark.txt", "r").readlines()
        for f in F:
            brand = f.split("\n")[0].split(";")[1]
            #brand = "Rolex"
            path = create_dir(brand)
            for i in range(49):
            #for i in range(2):
                SEC = random.choice([2,3,4,5,3,1,1.1,1.5, 0.7])
                time.sleep(SEC)
                Sess = RequestLib()
                http = "https://catalog.antiquorum.swiss/en/lots?page={}&q={}".format(i, brand)

#                http = "https://catalog.antiquorum.swiss/en/lots?page=1&q=Rolex"
                #path = create_dir("Rolex")
                #print ("parsing page", i, brand, http)
                sess = Sess.get(http)
                #print (sess)
                soup = BeautifulSoup(sess)
                J = soup.find_all('div', {"class": "shadow mt-4"})
                HJ = soup.find_all('div', {"class": "row"})
                if len(J) != 0:
                   for ix, link in enumerate(J):
                            time.sleep(1)
                            try:     
                               price_link = link.find_all("p", {"class": "N_lots_estimation"})#.text
                               price_link = utils_help(price_link)
                               price_link = str(price_link).replace(",", "").replace(".", "")
                               price_link = ast.literal_eval(price_link.replace(" ", ","))
                            except AttributeError: 
                               price_link = None 
                            try:   
                               info_model = link.find("div", {"class": "pt-2 shadow-sm p-2"})
                               info_model = func_info(str(info_model))
                            except AttributeError: 
                               info_model = None
                               
                            try:   
                               lot_id = link.find_all("h4")
                               lot_id  = str(lot_id[0]).replace('</h4>','').replace('<h4>','').replace('[','').replace(']','')
                            except AttributeError: 
                               lot_id = None                               
                               #N_lots_price mt-0
                            try:
                               lot_sold = HJ[ix].find("div", {"class": "N_lots_price mt-0"})
                               lot_sold = lot_sold.find("p").text.replace(",", "").replace(":", "").replace("\n","").replace("\t","")#\n\t\t\t\t\t\t
                               lot_sold = lot_sold.split(" ")[1:-1]
                            except AttributeError:  
                               lot_sold = None
                            except IndexError:
                               lot_sold = None 
                            #print (">>>>",lot_sold)
                            try:
                               title = link.find('div', {"class": "N_lots_description col"}).find('span')['content']
                               title = title.replace("\u2003", "").replace('“','').replace('”','').replace('.','').replace('’’’', '').replace('.', '').replace('"',"").replace("'","").replace("\n", "").replace("\r", "")  
                            except AttributeError:  
                               title = None
                            except IndexError:
                               title = None 
                            #print (">>>>",lot_sold)
                            try:
                            #if T:
                               href = "https://catalog.antiquorum.swiss"+str(link.find('a')["href"]) #href["href"], 
                               img_link = link.find("img", {"class": "lot_image"})['src']
                               img_link_local = path+"/"+ str(i)+ "_"+ str(ix) + "_" + img_link.split("/")[-1]
                               #D[ix] = {"title":new, "href":href, "img":img_link}
                               #print (href, img_link, title)
                               #print (lot_id, lot_sold)
                               #print (info_model, price_link)
                               dump = {"Brand":None, "Model": None, "Price":price_link, "Info": info_model, "link":href, "Image":img_link_local, "lot_id":lot_id, "title":title, "lot_sold":lot_sold, "img_link":img_link}
                               #print (info_model)
                               if info_model != None:
                                       for A in info_model.keys():
                                           #print (A)
                                           if A == "Model":
                                                dump["Model"] = info_model[A]
                                           if A == "Brand":
                                                dump["Brand"] = info_model[A]
                               print (dump)

                               classDB.create_collection("Watch")  
                               idx = classDB.create_post(dump) 
                               response = Sess.get_img(img_link)
                               #print (img_link, response)
                               if response.status_code == 200:
                                   with open(img_link_local, 'wb') as fli:
                                       fli.write(response.content)  

                            except TypeError:
                               print ("ERRor")
                               pass      
            
      #except R.exceptions.ConnectionError:      
      #        pass
def clearDB():  
        classDB.create_collection("Watch")#"Model" 
        classDB.del_all_post()
        
        classDB.create_collection("Model")
        classDB.del_all_post()
        
        classDB.create_collection("Brand")
        classDB.del_all_post()
        
        classDB.create_collection("Stat")
        classDB.del_all_post()
                          
classDB = DataBase()
#classDB.create_collection("Watch")
#print(classDB.see_all_post())
clearDB() 
createDB_1()
createDB()
