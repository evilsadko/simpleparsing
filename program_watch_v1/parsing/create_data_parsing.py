# -*- coding: utf-8 -*-
import pymongo
import os
import json
import ast
import numpy as np
from bs4 import BeautifulSoup
from data_base import DataBase

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


def string_form(x):
    str = ""
    for i in x:
       str += i+" "
    return str
    
    
def file_parse(x):
    soup = BeautifulSoup(x)
    l = soup.find_all("p")#.text
    G = []
    for i in l[1:]:
        t = i.find("strong")
        P = i.text.split(t.text)
        #tt = string_form(i.text.split(" "))
        try:
           J = P[-1].split(",")[0]
        except:
           J = P[-1]
        t = t.text   
        G.append({t:J})
    return G        

def data_info():
        T = DATA()
        TEMP = {}
        G = T.parseIMG("antiquorum")
        print (len(T.file.keys()), len(T.txt.keys()))
        for o in T.txt.keys():
            if o in T.file.keys():
               print (o, T.file[o], T.txt[o])
               TEMP[o] = {"img":T.file[o][0], "info":T.txt[o][0]}
        with open("data_file.json", "w") as write_file:
            json.dump(TEMP, write_file)


"""
Brand = { "FullName":
      "WorkName":
      "ModelId"
    }
    
Model = { "WorkName":
          "ModelName":
}
У нас будут колекции model, brend, watch
дальше будем добовлять watch по дате
для дальнейшего анализа в бд watch     
"""
def sum_price(x):
    s = ""
    for i in x:
        s += i
    return int(s)    
def func_price(HK):
       for opx in HK:
           kl = opx.split("\n")[0]
           kl = kl.split(";")[0]
           try:
             #print (">>>>>>>>>>>", kl, type(kl), len(kl))
             kl = ast.literal_eval(kl)
             
             for opj in kl:
                  for i_opj in opj:
                       if i_opj == "USD":
                         s = sum_price(opj[1].split(","))
                         s1 = sum_price(opj[2].split(","))
                         #print (">>>>>>>>>>>", opj[1].split(","), opj[2].split(","), s, s1)#, s1)
                         return [s, s1] 
           except TypeError:
                 #price = []
                 pass
                 #print ("TypeError",kl) 
           except SyntaxError:
                 pass
                 #print ("SyntaxError",kl) 
           except ValueError:
                 pass
                 #print ("ValueError",kl)
           #print (price) 


def file_parse_str(HK):
       str_1 = ""
       for opx in HK:
           kl = opx.split("\n")[0]
           kl = kl.split(";")[0]
           try:
             kl = ast.literal_eval(kl)
           except SyntaxError:
                 str_1 += kl
                 #print ("SyntaxError >>>>>>>>>>>>>>",kl) 
           except ValueError:
                 pass      
       return str_1


def func_info(HK):
       str_1 = ""
       for opx in HK:
           kl = opx.split("\n")[0]
           kl = kl.split(";")[0]
           try:
             kl = ast.literal_eval(kl)
           except:# ValueError:
                 str_1 += str(kl)
       return str_1          
                         
def func_link(x):
    for p in x:
       try:
          if p.split("\n")[0].split(";")[-2].split(":")[0] == "https":
             #print (">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<", )#.split(":")[0])
             return p.split("\n")[0].split(";")[-2] 
       except IndexError:
          pass   
    
def func0(x):
   _x = x
   x = x["img"].split("/")[1] # Brand
   return x
   #print (G)#(x, _x) _x['info']
   #classDB.create_collection("Obj")
   #classDB.create_post()
   #Model
   #classDB.create_collection("Model")
   #classDB.see_post()
   #print(classDB.see_all_post())#("OKKK<")#
#[['CHF', '4,000', '5000']];
#[];
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

   
 
       
def createDB():
        T = DATA()
        TEMP = {}
        G = T.parseIMG("antiquorum")
        print (len(T.file.keys()), len(T.txt.keys()))
        for o in T.txt.keys():
            if o in T.file.keys():
               info_f = T.txt[o][0]
               img_link = T.file[o][0] # Image
               brand_f = img_link.split("/")[1]
               classDB.create_collection("Brand")
               brand_0 = classDB.one_find_post({"BrandName":brand_f})
               
               try:
                       HK = open(info_f, "r").readlines()
                       price = func_price(HK)
                       link = func_link(HK)
                       info_0 = func_info(HK)
                       info_1 = file_parse(info_0)
                       info_2 = file_parse_str(HK)
                       info_3 = info_2.replace("]","").split("[")[0]
                       #info_4 = info_2.replace("]","").split("[")[1]
                       dump1 = {}
                       for ixx in info_1:
                           dump1[list(dict(ixx).keys())[0].replace('“','').replace('”','').replace('.','').replace('’’’', '').replace('.', '').replace('"',"").replace("'","")] = list(dict(ixx).values())[0].split("\u2003")[1].replace('“','').replace('”','').replace('.','').replace('’’’', '').replace('.', '').replace('"',"").replace("'","")
                       dump = {"Brand":None, "Model": None, "Price":price, "Info": dump1, "Info_3":str(info_3), "link":link, "Image":img_link}
                       
                       for d_k in dump1.keys():
                           if d_k == "Model":
                              i_d_k = dump1[d_k]
                              dump["Model"] = i_d_k
                           if d_k == "Brand":
                              i_d_k = dump1[d_k]
                              dump["Brand"] = i_d_k
                       classDB.create_collection("Watch")  
                       classDB.create_post(dump)     
#               #except TypeError:#
               except IndexError:#
                    print ("@@@@@@@@@@@@@@@@@@@@@ IndexError")
                    #result_1 = None

def clearDB():  
        classDB.create_collection("Watch")#"Model" 
        classDB.del_all_post()
        
        classDB.create_collection("Model")
        classDB.del_all_post()
        
        classDB.create_collection("Brand")
        classDB.del_all_post()
        
        classDB.create_collection("Stat")
        classDB.del_all_post()
                          
if __name__ == "__main__":
        print ("Start ....")
        classDB = DataBase()
        clearDB() 
#        classDB.create_collection("Watch") 
#        clearDB()       
#        classDB.create_collection("Model")
#        clearDB()  
#        classDB.create_collection("Brand")
#        clearDB()
#        res = classDB.see_all_post()
#        print (res)
#        clearDB()
        createDB_1()
        createDB()
        
        #ModelSee()
 
        #classDB.create_post({"ok":"ok"})
        #classDB.del_all_post()
        #res = classDB.one_find_post("Price")#{"Price"}
#---------------------------------->         
#        res = classDB.see_all_post()
#        for i in res:
#          #print (i["link"])
#          try:
#            min_p = i["Price"][0]
#            max_p = i["Price"][1]
#            print (min_p, max_p, "\n")
#          #except KeyError:
#          except TypeError:
#            pass  
#---------------------------------->   
    

                    
                    
                    



        
 
        
