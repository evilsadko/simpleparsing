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
         #self.db = self.client["watch_t2"] 
         #self.db = self.client["watch_t3"] 
         #self.db = self.client["temp_parser"] 
         self.db = self.client["service_db1"]
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
     def funcPrep(self, x):
         self.z=x
         
#     def see_all_post_v2(self, x, y):
#         if self.z == None:
#            return list(self.db[self.n].find().skip(x).limit(y))
#         else:
#            return list(self.db[self.n].find(self.z).skip(x).limit(y))
#         
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

     def full_text(self, text, x, y):
         count = self.db[self.n].find({"$text": {"$search": text}}).count() 
         if count > y:
             return list(self.db[self.n].find({"$text": {"$search": text}}).skip(x).limit(y)), count
         else:
             return list(self.db[self.n].find({"$text": {"$search": text}})), count 

if __name__ == "__main__":
        print ("Start")
        classDB = DataBase()
        classDB.create_collection("Watch")
        #classDB.db["Watch"].create_index([("title", pymongo.TEXT)], name='search_index', default_language='english')
        classDB.db["Watch"].create_index([("Title", "text")])
        #F = 
        #F = list(classDB.db["Watch"].find({"$text": {"$search": "Rolex"}}).skip().limit())
        #F = list(classDB.db["Watch"].find({"$text": {"$search": "Rolex"}}).skip(10).limit(100))
        #Count = classDB.db["Watch"].find({"$text": {"$search": "Daytona"}}).count() 
        #F = classDB.full_text("Rolex", 0, 0)
        
        #.createIndex( { "title": "text" } )
        #F = classDB.db["Watch"].find().skip(10).limit(20)
        #db.reviews.createIndex( { comments: "text" } )
        #print (classDB.count())
        #G = classDB.see_all_post_v2(10, 1000, None)
        #print (len(F[0]), F[1], F[0][10])#(len(list(F)))
        #classDB.see_client()
#Daytona       
#class Car(models.Model):
#        color = models.CharField(...)


#class Person(Model):
#        name = models.CharField(...)
#        car = models.ForeignKey(...)

#people = Person.objects.filter(...)
#for person in people:
#    car = person.car

#from django.db.models import Q
#3JAAuSG2n 2K7G, 2020Sold Item
#0 23 567 9 1 345    900000000
# 1  4   8 10 12 16 17 18 19
#
#3JAAuSG2n 2K7G, 2020Sold Item
#SLZToYldUZ JCuSn Y25V, 2020Sold Item  
#3USSoldTR3  2JJun 27P, 32M020Sold Item
#Jun 25, 2020 , 3:16PM

#'$22.01\u2002\u20029 bids'
# Получать по индексу
# 3 2 27 2020
#my_filter_qs = Q()
#for creator in creator_list:
#    my_filter_qs = my_filter_qs | Q(creator=creator)
#my_model.objects.filter(my_filter_qs)
#https://ru.bmstu.wiki/%D0%9F%D0%BE%D0%BB%D0%BD%D0%BE%D1%82%D0%B5%D0%BA%D1%81%D1%82%D0%BE%D0%B2%D1%8B%D0%B9_%D0%BF%D0%BE%D0%B8%D1%81%D0%BA_%D0%B2_MongoDB
#db.your_collection.find(
#  {
#    $text: { $search: "sport hockey" }
#  }, {
#    score: { $meta: "textScore" }
#  }
#).sort(
#  {
#    score: { $meta: "textScore" }
#  }
#).limit(2)
#https://stackoverflow.com/questions/33541290/how-can-i-create-an-index-with-pymongo



