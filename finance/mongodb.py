# -*- coding: utf-8 -*-
import pymongo
import time
import os

mongodb_uri = os.getenv('MONGODB_URI', default='mongodb://localhost:27017/')

class DataBase(object):
     def __init__(self, test="test"):
         self.client = pymongo.MongoClient(mongodb_uri) #MongoClient('localhost', 27017)

         self.db = self.client[test]
         self.n ="collection" 
       
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
         
     def see_all_post_v2(self, x, y, z):
         if z == None:
            return list(self.db[self.n].find().skip(x).limit(y))
         else:
            return list(self.db[self.n].find(z).skip(x).limit(y))
         
     def find_by_id(self, idx):
         return list(self.db[self.n].find(idx))
 
     def see_post(self, idx):
         return self.db[self.n].find_one(idx)
         
     def upd_post(self, idx, post):
         return self.db[self.n].update_one({"_id" : idx},
                                           {"$set": post}, upsert=True)

     def del_all_post(self):
         self.db[self.n].delete_many({}) 

     def del_post(self):
         for i in self.db[self.n].find():
                 result = self.db[self.n].find_one(i["_id"])
                 result = self.db[self.n].delete_one(result)
                 result.deleted_count 

     def del_one_post(self, idx):
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
     # Удалить базу
     def del_db_by_name(self, x):
         self.client.drop_database(x)
     # Удалить коллекцию
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
             
             
             

#from bs4 import BeautifulSoup
if __name__ == "__main__":
        print ("Start")
        db = DataBase("invest")
        t = db.see_collection()
        name = "%s.%s.%s" % (time.strftime("%d"), time.strftime("%m"), time.strftime("%Y"))
        db.create_collection("27.08.2020")
        P = db.see_all_post_v2(0,0,{"date":"27.08.2020 17:58:12"})
        print (name, P)
#        db.create_collection(t[0])
        for i in db.see_all_post():
            P = db.see_all_post_v2(0,0,{"date":i["date"]})
            print (i, ">>>>>", P,"\n")
        #print (len(db.see_all_post()))
        #print (db.see_all_post_v2(0,0, {"date":"27.08.2020 08:07:11"}))
        #27.08.2020 17:58:12
        

        
        
