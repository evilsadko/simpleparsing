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
         #self.db = self.client["watch"] #Work работает первая
         #self.db = self.client["watch_t"]  #
         #self.db = self.client["watch_t1"]
         self.db = self.client["watch_t2"]
         self.n ="collection"
         self.u ="user"
         
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
                 #print (post)
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

 
     def one_find_post(self, name):
         result = self.db[self.n].find_one(name)#({"name_id":name})
         return result  
     def find_many_post(self, idx):
         #print (idx, self.n)
         return self.db[self.n].find(idx)
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
     
     def count(self):
         return self.db[self.n].find().count()


     def del_db_by_name(self, x):
         self.client.drop_database(x)

     def del_collection(self):
         result = self.db[self.n].drop() 

     def see_collection(self):
        list = []
        for i in self.db.collection_names():#3.6 #list_collection_names(): 2.7
           #print(i)
           list.append(i)
        return list

     def see_client(self):
         for idb in self.client.database_names():
             print (idb, "Имя базы данных")


if __name__ == "__main__":
        print ("Start DB")
        #classDB = DataBase()
        #classDB.see_client()


