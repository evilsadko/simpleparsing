# -*- coding: utf-8 -*-
import pymongo
import os

mongodb_uri = os.getenv('MONGODB_URI', default='mongodb://localhost:27017/')



class DataBase(object):
     def __init__(self):
         self.client = pymongo.MongoClient(mongodb_uri) #MongoClient('localhost', 27017)

         # 2 вариант
         #self.db = self.client["t"] 
         #self.n ="collection"
         
         
         #self.db = self.client["x"] 
         #self.n ="collection"
         #self.db = self.client["watch"] 
         #self.db = self.client["watch_t1"] 
         #wself.db = self.client["watch_t2"] 
         #self.db = self.client["watch_t3"] 
         #self.db = self.client["watch_t4"] # Anticourum Rolex 
         #self.db = self.client["watch_t5"] # Anticourum Full github
         #self.db = self.client["watch_live"]
         #self.db = self.client["watch_live1"] # 7792 liveauctioneers 0-20
         #self.db = self.client["watch_live2"] # 7544 liveauctioneers 20-40
         #self.db = self.client["watch_live3"] #--->7500 liveauctioneers 40-60
         #self.db = self.client["watch_ebay"]#["watch_linv"] #invaluable
         #self.db = self.client["watch_artinfo"]
         #self.db = self.client["temp_parser1"]
         self.db = self.client["service_db1"]
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

from bs4 import BeautifulSoup
if __name__ == "__main__":
        #------->db.del_all_post()
        print ("Start")
        db = DataBase()
#        db.db = db.client["watch_t5"]
        db.create_collection("Watch")
        db.del_all_post()
#        
#        #db.create_collection("Brand")
        G = db.see_all_post()
        print (len(G))
#        #---------------------------->
#        db.db = db.client["temp_parser"]
#        db.create_collection("Watch")
#        G1 = db.see_all_post()
#        #---------------------------->

        
        
