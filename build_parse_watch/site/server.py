# -*- coding: utf-8 -*-
import tornado.ioloop
import tornado.web
import tornado.websocket
import uuid
import json
import base64
import cv2
import os, sys
import numpy
import time
import io
import requests
import string
import random
from data_base import DataBase
from bson.objectid import ObjectId
import matplotlib 
import matplotlib.pyplot as plt 


dbclass = DataBase()
dbclass.see_collection()
dbclass.create_collection("Brand")
r1 = dbclass.see_all_post()
dbclass.create_collection("Model")
r2 = dbclass.see_all_post()
#dbclass.create_collection("Stat")
#r3 = dbclass.see_all_post()
#dbclass.del_all_post()
def func_stat():
        for u in r1:
           dbclass.create_collection("Model") 
           posts_ = dbclass.find_many_post({"brend_id":ObjectId(u['_id'])})
           dbclass.create_collection("Brand")
           dbclass.upd_post(ObjectId(u['_id']), {"list":posts_ })
           #print (posts_, len(posts_))
def func_stat2():           
        for u in r1:
                   if u["list"] != []:
                       t_list = []
                       #temp_db = {} 
                       for model_ in u["list"]:
                            dbclass.create_collection("Watch")
                            posts_ = dbclass.find_many_post({"Brand":u['BrandName']})
                            posts_1 = dbclass.find_many_post({"Model":model_['ModelName']})
                            if len(posts_) != 0 or len(posts_1) != 0:
                               t_list.append({"size":len(posts_1), "model":model_['ModelName'].replace('\u2003', '').replace('“','').replace('”','').replace('.','').replace('’’’', '').replace('.', '').replace('"',"").replace("'","")})
                               
                               
                               #dbclass.create_collection("Stat")
                               #dbclass.create_post(temp_db)  
                       temp_db = {"Brand":u['BrandName'].replace('\u2003', '').replace('“','').replace('”','').replace('.','').replace('’’’', '').replace('.', '').replace('"',"").replace("'",""), "size":len(posts_), "Models":t_list}
                       #print (">>>>>>>>>>>>",temp_db)
                       dbclass.create_collection("Stat")
                       dbclass.create_post(temp_db)  
dbclass.create_collection("Stat")
#-------->
#dbclass.del_all_post()
#func_stat() 
#func_stat2() 
#--------->
r3 = dbclass.see_all_post()

print (len(r3), len(r1), len(r2))

def generateRandomString(length):
    s = string.ascii_lowercase + string.digits + string.ascii_uppercase
    return str(''.join(random.sample(s, length)))

class BaseHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET')
    def get_current_user(self):
        return self.get_secure_cookie("name_id")



class MainHandler(BaseHandler):
    #dbclass = DataBase()
    #t_list = dbclass.see_collection()
    #print (len(t_list))


    def get(self):   
        dbclass.create_collection("Watch")
        #posts = self.dbclass.see_all_post()
        posts_count = dbclass.count()
        dbclass.funcPrep(None)
        
        posts = dbclass.see_all_post_v2(0, 100, None)#(150, 150)
        #print (len(posts))
        #posts = dbclass.see_all_post_v2(150, 150)
        dc = {}
        #"lot_id":lot_id, "title":title, "lot_sold":lot_sold, "img_link":img_link
        for ix, post in enumerate(posts):
                            dc[ix] = {"_id":str(post["_id"]), "image":post["Image"],
                                       "brand":post["Brand"], "model":post["Model"],
                                       "price":post["Price"], "link":post["Link"],
                                       "info": post["Info"], "title":post["Title"],
                                       "lot_id":post["Lot_id"], "lot_sold":post["Lot_sold"],
                                       "date_action":post["Date_action"], 'auctioner':post["Auctioner"],
                                       "img_link":post["Img_link"],
                                       "data_size":len(posts),
                                       "posts_coun": posts_count,
                                       "start":0}#
             #print (post["title"])
        posts = json.dumps(dc)
        #posts = json.loads(posts) base1.html
        #self.render("base4.html", title="Анализ данных", items=posts)
        
        self.render("test.html", title="Анализ данных", items=posts)
        #self.write(posts)
    def post(self):
        data_json = json.loads(self.request.body) 
        if data_json['type'] != "None":
            posts = dbclass.see_all_post_v2(data_json["start"], data_json["data_size"],
                                            {data_json['type']:data_json['data_text']})
        else:
            posts = dbclass.see_all_post_v2(data_json['start'], data_json["data_size"], None)
        dc = {}
        for ix, post in enumerate(posts):
#             dc[ix] = {"_id":str(post["_id"]), "image":post["Image"],
#                       "brand":post["Brand"], "model":post["Model"],
#                       "price":post["Price"], "link":post["link"],
#                       "info": post["Info"], "data_size":len(posts),
#                       "start":data_json['start']}#
                            dc[ix] = {"_id":str(post["_id"]), "image":post["Image"],
                                       "brand":post["Brand"], "model":post["Model"],
                                       "price":post["Price"], "link":post["Link"],
                                       "info": post["Info"], "title":post["Title"],
                                       "lot_id":post["Lot_id"], "lot_sold":post["Lot_sold"],
                                       "date_action":post["Date_action"], 'auctioner':post["Auctioner"],
                                       "img_link":post["Img_link"],
                                       "data_size":len(posts),
                                       "start":data_json['start']}#
        posts = json.dumps(dc)	
        self.write(posts)

class SearchHandler(BaseHandler):
    def get(self): 
        posts = json.dumps(r3)	
        self.write(posts)
    def post(self): 
        data_json = json.loads(self.request.body)
        #J = data_json['data_text']
        dbclass.create_collection("Watch")
        #posts = dbclass.find_many_post({data_json['type']:data_json['data_text']})
        posts_count = dbclass.count1({data_json['type']:data_json['data_text']})
        posts = dbclass.see_all_post_v2(0, 100, {data_json['type']:data_json['data_text']})
        print (posts_count, len(posts))#, data_json)
        dc = {}
        min_l = []
        max_l = []
        x = []
        y = [] 
        max_i = 0
        min_i = 0
        for ix, post in enumerate(posts):
#                     if post["Price"] != None:
#                        min_l.append(post["Price"][0])
#                        min_i += post["Price"][0]
#                        max_l.append(post["Price"][1])
#                        max_i += post["Price"][1]
#                        #print (post["Price"][0], post["Price"][1])
#                        x.append(ix)    

#                     dc[ix] = {"_id":str(post["_id"]), "image":post["Image"],
#                       "brand":post["Brand"], "model":post["Model"],
#                       "price":post["Price"], "link":post["link"],
#                       "info": post["Info"], "data_size":len(posts),
#                       "posts_count":posts_count}#,
                            dc[ix] = {"_id":str(post["_id"]), "image":post["Image"],
                                       "brand":post["Brand"], "model":post["Model"],
                                       "price":post["Price"], "link":post["Link"],
                                       "info": post["Info"], "title":post["Title"],
                                       "lot_id":post["Lot_id"], "lot_sold":post["Lot_sold"],
                                       "date_action":post["Date_action"], 'auctioner':post["Auctioner"],
                                       "img_link":post["Img_link"],
                                       "data_size":len(posts), "posts_count":posts_count,
                                       "start":0}#
                       
                       #"start":data_json['start']}#
#        print (min(min_l), min_i/len(posts),  max(min_l), "<---->", min(max_l), max_i/len(posts), max(max_l))#(min_l, max_l)    
#        dc["info"] = {"min_min": min(min_l), "min_mid": min_i/len(posts), "min_max": max(min_l),
#                      "max_min": min(max_l), "max_mid": max_i/len(posts), "max_max": max(max_l),
#                      }
        self.write(json.dumps(dc))              
#        fig, ax = plt.subplots()
#        ymax = max(max_l)
#        xmax = x[max_l.index(ymax)]

#        ymax=round(ymax,2) 
#        ax.annotate('MAX:'+str(ymax), xy=(xmax, ymax*(1.005)), horizontalalignment='center')
#        ax.plot(x, max_l, color="g")
#        plt.title(data_json['data_text'], fontsize=20)
#        plt.grid() 
#        plt.savefig('data.png')
class PostHandler(BaseHandler):
    def get(self, ids): 
        #key = self.get_argument()
        dbclass.create_collection("Watch")
        post = dbclass.see_post({"_id":ObjectId(ids)})
        dc = {"_id":str(post["_id"]), "image":post["Image"],
                                      "brand":post["Brand"], "model":post["Model"],
                                      "price":post["Price"], "link":post["Link"],
                                      "info": post["Info"], "title":post["Title"],
                                      "lot_id":post["Lot_id"], "lot_sold":post["Lot_sold"],
                                      "date_action":post["Date_action"], 'auctioner':post["Auctioner"],
                                      "img_link":post["Img_link"],
                                      "lot_id":post["Lot_id"], "lot_sold":post["Lot_sold"]}#
        #print(ids, dc)
        self.write(json.dumps(dc))
        
class CountHandler(BaseHandler):
    def post(self): 
        data_json = json.loads(self.request.body)
        #print (">>>>>>>>",self.request.body)
        #self.write("OK") 
        dbclass.create_collection("Watch")
        if data_json["all"] == 1:
                posts_s = dbclass.find_many_post({data_json["type"]:data_json['data_text']}) 
                dc = {"posts_count":len(posts_s)} 
                self.write(json.dumps(dc))  
        else:
                posts_count = dbclass.count()
                dc = {"posts_count":posts_count}#           
                self.write(json.dumps(dc))  
                
#

class FullText(BaseHandler):
    def post(self):
        dbclass.create_collection("Watch")
        data_json = json.loads(self.request.body) 
        #data_json['start'], data_json["data_size"]
        try:
                if data_json["data_text"] != "":
                        D = dbclass.full_text(data_json["data_text"], data_json["start"], data_json["data_size"]) 
                        dc = {} 
                        for ix, post in enumerate(D[0]):
                            #print (post)
                            dc[ix] = {"_id":str(post["_id"]), "image":post["Image"],
                                       "brand":post["Brand"], "model":post["Model"],
                                       "price":post["Price"], "link":post["Link"],
                                       "info": post["Info"], "title":post["Title"],
                                       "lot_id":post["Lot_id"], "lot_sold":post["Lot_sold"],
                                       "date_action":post["Date_action"], 'auctioner':post["Auctioner"],
                                       "img_link":post["Img_link"],
                                       "data_size":len(D[0]), "posts_count":D[1],
                                       "start":data_json['start']}#
                        self.write(json.dumps(dc))  
                else:
                        posts = dbclass.see_all_post_v2(data_json['start'], data_json["data_size"], None) 
                        posts_count = dbclass.count()  
                        dc = {} 
                        for ix, post in enumerate(posts):
                            #print (post)
                            dc[ix] = {"_id":str(post["_id"]), "image":post["Image"],
                                       "brand":post["Brand"], "model":post["Model"],
                                       "price":post["Price"], "link":post["Link"],
                                       "info": post["Info"], "title":post["Title"],
                                       "lot_id":post["Lot_id"], "lot_sold":post["Lot_sold"],
                                       "date_action":post["Date_action"], 'auctioner':post["Auctioner"],
                                       "img_link":post["Img_link"],
                                       "data_size":len(posts), "posts_count":posts_count,
                                       "start":data_json['start']}#
                        self.write(json.dumps(dc))  
        except KeyError:
                        posts = dbclass.see_all_post_v2(data_json['start'], data_json["data_size"], None) 
                        posts_count = dbclass.count()  
                        dc = {} 
                        for ix, post in enumerate(posts):
                            #print (post)
                            dc[ix] = {"_id":str(post["_id"]), "image":post["Image"],
                                       "brand":post["Brand"], "model":post["Model"],
                                       "price":post["Price"], "link":post["Link"],
                                       "info": post["Info"], "title":post["Title"],
                                       "lot_id":post["Lot_id"], "lot_sold":post["Lot_sold"],
                                       "date_action":post["Date_action"], 'auctioner':post["Auctioner"],
                                       "img_link":post["Img_link"],
                                       "data_size":len(posts), "posts_count":posts_count,
                                       "start":data_json['start']}#
                        self.write(json.dumps(dc))                                    
#    def post(self):
#        data_json = json.loads(self.request.body) 
#        if data_json['type'] != "None":
#            posts = dbclass.see_all_post_v2(data_json["start"], data_json["data_size"],
#                                            {data_json['type']:data_json['data_text']})
#        else:
#            posts = dbclass.see_all_post_v2(data_json['start'], data_json["data_size"], None)
#        dc = {}
#        for ix, post in enumerate(posts):
#             dc[ix] = {"_id":str(post["_id"]), "image":post["Image"],
#                       "brand":post["Brand"], "model":post["Model"],
#                       "price":post["Price"], "link":post["link"],
#                       "info": post["Info"], "title":post["title"],
#                       "lot_id":post["lot_id"], "lot_sold":post["lot_sold"],
#                       "data_size":len(posts),
#                       "start":data_json['start']}#
#        posts = json.dumps(dc)	
#        self.write(posts)        
                       
#/catalog/5ee06f2bb2c79a2e84317e4e      	
def make_app():
    settings = {
        "cookie_secret": generateRandomString(50),
        "login_url": "/",
    }
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/search", SearchHandler),
        (r"/text", FullText),
        (r"/catalog/(.*)", PostHandler), 
        (r"/count", CountHandler), 
        (r"/data_info/(.*)", tornado.web.StaticFileHandler, {'path':'./data_info'}), 
        (r"/(pv_layer_controls.png)", tornado.web.StaticFileHandler, {'path':'./'}),
        (r"/(style.css)", tornado.web.StaticFileHandler, {'path':'./'}),
    ], **settings)

if __name__ == "__main__":
    app = make_app()
    app.listen(8800, address='192.168.1.50') 
    tornado.ioloop.IOLoop.current().start()
        
#
"""
Выстраиваю список моделей
бренд
[{'_id': ObjectId('5ebb9c88b2c79a6b139fb311'), 'BrandName': 'Franck Muller', 'WorkName': 'franckmuller'}]
модель

"""


