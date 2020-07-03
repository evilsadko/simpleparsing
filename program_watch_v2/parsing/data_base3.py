# -*- coding: utf-8 -*-
import pymongo
import os
import requests as R
import json
from fake_useragent import UserAgent
mongodb_uri = os.getenv('MONGODB_URI', default='mongodb://localhost:27017/')



class DataBase(object):
     def __init__(self):
         self.client = pymongo.MongoClient(mongodb_uri) #MongoClient('localhost', 27017)

         self.db = None #self.client["temp_parser"]
         self.n ="collection" 
         self.u ="user"
         #self.z = None
         
     def user_add(self, post):
         u ="user"
         post_id = self.db[u].insert_one(post).inserted_id
         return post_id
         
     def upd_user(self, idx, post):
         u ="user"
         return self.db[u].update_one({"_id" : idx},
                                      {"$set": post}, upsert=True)     
         
     def see_all_user(self):
         u ="user"
         return list(self.db[u].find().skip(40).limit(40))
#         list = []
#         for i in self.db[u].find():
#              i["_id"] = str(i["_id"])
#              list.append(i)
#         return list(self.db[u].find())#list  
     
         
     def see_count_user(self):
         u ="user"
         return self.db[u].find().count()  
       
          
     def get_one_user(self, name):
         u ="user"
         result = self.db[u].find_one({"name_id":name})
         return result                   
         
     def create_collection(self, x): #self.n
                self.n = x

     def create_post(self, post):
                 post_id = self.db[self.n].insert_one(post).inserted_id
                 return post_id

     def create_many(self, post):
                 self.db[self.n]
                 post_id = self.db[self.n].insert_many(post)
                 return post_id        


     def see_all_post(self):
         list = []
         for i in self.db[self.n].find():
              i["_id"] = str(i["_id"])
              list.append(i)
         return list
         
     def see_all_post_v1(self, x, y):
         return list(self.db[self.n].find().skip(x).limit(y))
         #return list(self.db[self.n].find().skip(40).limit(40))
     #def funcPrep(self, x):
     #   self.z=x
         
     def see_all_post_v2(self, x, y, z):
         if z == None:
            return list(self.db[self.n].find().skip(x).limit(y))
         else:
            return list(self.db[self.n].find(z).skip(x).limit(y))
         
     def find_many_post(self, idx):
         #print (idx, self.n)
         return list(self.db[self.n].find(idx))
 
     def see_post(self, idx):
         #print (idx, self.n)
         return self.db[self.n].find_one(idx)
         
     def upd_post(self, idx, post):
         #print (post)
         return self.db[self.n].update_one({"_id" : idx},
                                           {"$set": post}, upsert=True)


     def del_all_post(self):
         self.db[self.n].delete_many({}) 


     def del_post(self):
         for i in self.db[self.n].find():
                 print (i["_id"])#result, result["_id"] 
                 result = self.db[self.n].find_one(i["_id"])
                 result = self.db[self.n].delete_one(result)
                 result.deleted_count 

     def del_one_post(self, idx):
                 print (idx, self.n)
                 result = self.db[self.n].find_one({"_id":idx})
                 result = self.db[self.n].delete_one(result)
                 result.deleted_count 
     # Список баз
     #кол-во всех данных
     def count(self):
         return self.db[self.n].find().count()
     #кол-во фильтрованных данных
     def count1(self, x):
         return self.db[self.n].find(x).count()    


     def del_db_by_name(self, x):
         self.client.drop_database(x)

     def del_collection(self):
         result = self.db[self.n].drop() 

     def see_collection(self):
        list = []
        for i in self.db.collection_names(): #list_
           print(i)
           list.append(i)
        return list

     def see_client(self):
         for idb in self.client.database_names():
             print (idb, "Имя базы данных")


#        #------->db.del_all_post()
def antiquorum():
        print ("Start antiquorum")
        classdb = DataBase()
        classdb.db = classdb.client["watch_t5"]
        classdb.create_collection("Watch")
        G = classdb.see_all_post()
        print (len(G))
#        #---------------------------->
        classdb.db = classdb.client["temp_parser1"]
        #classdb.del_all_post()
        classdb.create_collection("Watch")
        for iop in G:
            dump = {'Brand':iop['Brand'], 'Model':iop['Model'], 'Title':iop['title'], 'Price':iop['Price'], 
                    'Info':iop['Info'], 'Link':iop['link'], 'Image':iop['Image'], 'Lot_id':iop['lot_id'],  
                    'Lot_sold':iop['lot_sold'], 'Img_link':iop['img_link'], 'Date_action':"", 
                    'Auctioner':{"href": "https://www.antiquorum.swiss/", "name":"Antiquorum"}}
            idx = classdb.create_post(dump) 
            print (dump, idx)   
            #print (iop.keys())
        G1 = classdb.see_all_post()
        print (len(G1))
def get_ls():
        my_l = "https://api.exchangeratesapi.io/latest?base=USD"
        r = R.get(my_l)
        G = json.loads(r.text)
        H = G["rates"]
        dict = {}
        for i in H.keys():
            dict[i] = round(H[i],2)
        return dict
        
        
def convertor(summ, current, received):
    #print (summ, current, received )
    heft = summ / current
    return round(heft * received, 2)

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


from bs4 import BeautifulSoup
if __name__ == "__main__":
        #------->db.del_all_post()
        print ("Start")
        classdb = DataBase()
        Sess = RequestLib()
        #classdb.db = classdb.client["watch_live1"]
        #classdb.db = classdb.client["watch_live2"]
        #classdb.db = classdb.client["watch_live3"]
        classdb.db = classdb.client["watch_t5"] #
        #classdb.db = classdb.client["watch_ebay"]
        #classdb.del_db_by_name("temp_parser")
# Create Index       
        #classdb.db["Watch"].create_index([("Title", "text")])
#---------------------------------->        
        classdb.create_collection("Watch")
        G = classdb.see_all_post()
        print (len(G))
        #---------------------------->
        classdb.db = classdb.client["temp_parser"]
        #classdb.del_all_post()
        classdb.create_collection("Watch")
        SZ=get_ls()
        #print (SZ)#(iop['lot_sold'])
        #print(convertor(100.0, SZ['HKD'], SZ['USD']))
        for iop in G:
#Antiquorum  
            if iop['lot_sold'] != None:
               try:
               #Antiquorum
                 t_price = convertor(float(iop['lot_sold'][2]), float(SZ[iop['lot_sold'][1]]), SZ['USD'])
                 dump = {'Brand':iop['Brand'], 'Model':iop['Model'], 'Title':iop['title'], 'Price':iop['Price'], 
                    'Info':iop['Info'], 'Link':iop['link'], 'Image':iop['Image'], 'Lot_id':iop['lot_id'],  
                    'Lot_sold':t_price, 'Img_link':iop['img_link'], 'Date_action':"", 
                    'Auctioner':{"href": "https://www.antiquorum.swiss/", "name":"Antiquorum"}}
                 #print (convertor(float(iop['lot_sold'][2]), float(SZ[iop['lot_sold'][1]]), SZ['USD']))
                 idx = classdb.create_post(dump)
               except KeyError:
                 pass             
#            if iop['lot_sold'] == None:   
#               Sess.headers['User-agent'] = UserAgent().random
#               response = Sess.get(iop['link']) 
#               #response.get_page#.text 
#               soup = BeautifulSoup(response.text) 
#               J = soup.find_all('div', {"class": "col-xs-12 col-md-6"}) 
#               G = J[-1].find_all("h4")
#               #print (iop['link'], G[-1].text) # iop['lot_sold'], iop['link'], iddd
#               if "Sold" in G[-1].text:
#                  t_price = convertor(float(G[-1].text.split(" ")[-2].replace(",", "")), float(SZ[G[-1].text.split(" ")[-3]]), SZ['USD'])
#                  #print (t_price)
#                  dump = {'Brand':iop['Brand'], 'Model':iop['Model'], 'Title':iop['title'], 'Price':iop['Price'], 
#                    'Info':iop['Info'], 'Link':iop['link'], 'Image':iop['Image'], 'Lot_id':iop['lot_id'],  
#                    'Lot_sold':t_price, 'Img_link':iop['img_link'], 'Date_action':"", 
#                    'Auctioner':{"href": "https://www.antiquorum.swiss/", "name":"Antiquorum"}}
#                  idx = classdb.create_post(dump)
                  
                  
#            if iop['lot_sold'] != None:
#               try:
#               #Antiquorum
#                 t_price = convertor(float(iop['lot_sold'][2]), float(SZ[iop['lot_sold'][1]]), SZ['USD'])
#                 dump = {'Brand':iop['Brand'], 'Model':iop['Model'], 'Title':iop['title'], 'Price':iop['Price'], 
#                    'Info':iop['Info'], 'Link':iop['link'], 'Image':iop['Image'], 'Lot_id':iop['lot_id'],  
#                    'Lot_sold':t_price, 'Img_link':iop['img_link'], 'Date_action':"", 
#                    'Auctioner':{"href": "https://www.antiquorum.swiss/", "name":"Antiquorum"}}
#                 #print (convertor(float(iop['lot_sold'][2]), float(SZ[iop['lot_sold'][1]]), SZ['USD']))
#                 idx = classdb.create_post(dump)
#               except KeyError:
#                 pass 
#            else:     
#                    dump = {'Brand':iop['Brand'], 'Model':iop['Model'], 'Title':iop['title'], 'Price':iop['Price'], 
#                            'Info':iop['Info'], 'Link':iop['link'], 'Image':iop['Image'], 'Lot_id':iop['lot_id'],  
#                            'Lot_sold':0, 'Img_link':iop['img_link'], 'Date_action':"", 
#                            'Auctioner':{"href": "https://www.antiquorum.swiss/", "name":"Antiquorum"}}
#                    idx = classdb.create_post(dump)     
#----------------------------------------->

#liveauctioneers 
#EUR €   
#USD $     
#            dump = {'Brand':"", 'Model':"", 'Title':iop['Title'], 'Price':"", 
#                    'Info':"", 'Link':iop['Link'], 'Image':"", 'Lot_id':"",  
#                    'Lot_sold':iop['Lot_sold'], 'Img_link':iop['Img_link'], 
#                    'Date_action':iop['Date_action'], 'Auctioner':iop['Auctioner']} 


#            dss = iop['Lot_sold'].split(" ")[-1].replace(",", "").replace("CA", "").replace("HF\xa02600", "").replace("A", "")         
#            #, iop['Link'])        
#            if dss != "Passed" and dss != "Closed":
#                  if dss[0] == "€":
#                     
#                     t_price = convertor(float(dss[1:]), float(SZ['EUR']), SZ['USD'])
#                     #print (dss[1:], t_price)
#                     dump = {'Brand':"", 'Model':"", 'Title':iop['Title'], 'Price':"", 
#                             'Info':"", 'Link':iop['Link'], 'Image':"", 'Lot_id':"",  
#                             'Lot_sold':t_price, 'Img_link':iop['Img_link'], 
#                             'Date_action':iop['Date_action'], 'Auctioner':iop['Auctioner']} 
#                     idx = classdb.create_post(dump)         
#                  else:
#                     try:
#                       t_price = convertor(float(dss[1:]), float(SZ['USD']), SZ['USD'])
#                       dump = {'Brand':"", 'Model':"", 'Title':iop['Title'], 'Price':"", 
#                               'Info':"", 'Link':iop['Link'], 'Image':"", 'Lot_id':"",  
#                               'Lot_sold':t_price, 'Img_link':iop['Img_link'], 
#                               'Date_action':iop['Date_action'], 'Auctioner':iop['Auctioner']} 
#                       idx = classdb.create_post(dump)          
#                       #print(t_price, dss)
#                     except ValueError:
#                       dss = str(iop['Lot_sold'].split(" ")[-1]).replace(",","")
#                       dss1 = iop['Lot_sold'].split(" ")[-2].split(" ")[-1]
#                       #print(">>>>>>", dss, dss1)
#                       t_price = convertor(float(dss), float(SZ[dss1]), SZ['USD']) 
#                       dump = {'Brand':"", 'Model':"", 'Title':iop['Title'], 'Price':"", 
#                               'Info':"", 'Link':iop['Link'], 'Image':"", 'Lot_id':"",  
#                               'Lot_sold':t_price, 'Img_link':iop['Img_link'], 
#                               'Date_action':iop['Date_action'], 'Auctioner':iop['Auctioner']}
#                       idx = classdb.create_post(dump)          
#            else:
#                     dump = {'Brand':"", 'Model':"", 'Title':iop['Title'], 'Price':"", 
#                             'Info':"", 'Link':iop['Link'], 'Image':"", 'Lot_id':"",  
#                             'Lot_sold':0, 'Img_link':iop['Img_link'], 
#                             'Date_action':iop['Date_action'], 'Auctioner':iop['Auctioner']}                                
#                     idx = classdb.create_post(dump)       

    
                       #print (dss, t_price)#.split(" "))#(dss, iop['Link'],  iop['Lot_sold'])#(dss[1:], t_price)  
#------------------------------------------------------------>                       
#ebay
#            dump = {'Brand':"", 'Model':"", 'Title':iop['Title'], 'Price':"", 
#                    'Info':"", 'Link':iop['Link'], 'Image':"", 'Lot_id':"",  
#                    'Lot_sold':iop['Lot_sold'], 'Img_link':iop['Img_link'], 
#                    'Date_action':iop['Date_action'], 'Auctioner':iop['Auctioner']} 

             
            #print (dump, idx)  
            
            
#            tiop = iop['Lot_sold']
#            try:
#              dump = {'Brand':"", 'Model':"", 'Title':iop['Title'], 'Price':"", 
#                    'Info':"", 'Link':iop['Link'], 'Image':"", 'Lot_id':"",  
#                    'Lot_sold':float(tiop.split("\u2002\u2002")[0].replace(",", "").replace("$", "")), 'Img_link':iop['Img_link'], 
#                    'Date_action':iop['Date_action'], 'Auctioner':iop['Auctioner']} 
#              idx = classdb.create_post(dump)      
#              #print (float(tiop.split("\u2002\u2002")[0].replace(",", "").replace("$", "")), iop['Link'])#.replace("\u2003", "")
#            except:
#              print (tiop.split("\u2002\u2002")[0].replace(",", "").replace("$", ""), iop['Link'])


#        print (len(classdb.see_all_post()))
        #27690

#------------------------------------------------>
        
        
