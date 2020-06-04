# -*- coding: utf-8 -*-
import pymongo
import os
import json
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


Brand = {}
Model = {}
if __name__ == "__main__":
        classDB = DataBase()
#--------------------------------------------------------->
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
        
        
        #print (len(B.keys()), len(D.keys()))
        #print (D)#(B.values(), B.keys()) 
        #classDB = DataBase()
        #classDB.see_client()

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

#
#https://docs.google.com/document/d/1d49dnyelnCQcezfnI2UIomhYEIvpHC8XLaNLVsU58xo/edit

#https://auctions.fortunaauction.com/lots?search=rolex+submariner
#https://catalog.antiquorum.swiss/en/lots?utf8=%E2%9C%93&q=rolex+submariner   
#https://www.tateward.com/auction/search?st=rolex%20submariner&c=1&sd=1 
#invaluable.com
#violity.com
#Chrono24

#показал
#есть следующий виток по проекту
#по сути все работает верно, НО
#сайтов - дилеров и аукционов с которых нужно тянуть инфу - примерно - 50 шт
#самые жирные, судя по трафику:::
#— invaluable.com (3мл.трафик в мес)
#— violity.com (3мл.трафик в мес)

#основные задачи:
#— вытянуть всю инфу с каждого сайта (аукциона), учитывая что их 50 
#причем кроме модели - марки и описания
#нужно систематизировать показывать историю продаж-лотов
#самые важные критерии:: цена, продан-не продан
#для того чтобы зарегистрированные пользователи видели расширенную инфу

#— есть еще интересная задача, на этих двух аукционах (где по 3 мл. трафик) мы можем вытянуть мыльники 
#их зарегистрированных юзеров как-то? не ломая ничего конечно и не взламывая

#— вторая и второстепенная задача собрать всю всю инфу по всем маркам-моделям часов, 
#вплоть до истории бренда (тут возможет ручной ввод)

#п.с. подумай пож. как будем поэтапно реализовывать
#п.с. сколько надо времени, денег с нас
#п.с. + я думаю если уже искали инфу, то ее бы записать в базу и вывести то что уже искали, и подгрузить разницу, типа новые лоты часов 
#чтобы не грабить одно и то-же бесконечно        
# 
#        
