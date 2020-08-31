# -*- coding: utf-8 -*-
from datetime import date, timedelta, datetime
from fake_useragent import UserAgent
import tornado.httpserver
import tornado.ioloop
import tornado.web
import ssl
import json
import time
import requests as R
import numpy as np
import cv2
import random
import os
import threading
from parsing import *


acc_key = ""
sess = RequestLib()

class getToken(tornado.web.RequestHandler):
    def get(self):
        print ("GET")
        self.write("hello")
    def post(self):
        data = json.loads(self.request.body)
        print ("POST", data)
        try:
          chat_id = data["message"]["from"]["id"]
          text_mess = data["message"]["text"]
          print (text_mess)
          if text_mess == "parser 1":
                 #op = "info"
                 name = "%s.%s.%s" % (time.strftime("%d"), time.strftime("%m"), time.strftime("%Y"))
                 classdb.create_collection(name)
                 dump = classdb.see_all_post()
                 print (">>>", dump)
                 if len(dump) != 0:
                         for op in dump:
                            my_l = "https://api.telegram.org/bot"+acc_key+"/sendMessage?chat_id="+str(chat_id)+"&text="+str(op)+"&parse_mode=html"
                            #print ("PARSER",str(chat_id), my_l)
                            r = sess.get(my_l)
                            print (r.text, r)
                 else:
                         my_l = "https://api.telegram.org/bot"+acc_key+"/sendMessage?chat_id="+str(chat_id)+"&text="+str("выходной")+"&parse_mode=html"        
                         r = sess.get(my_l)
                         print (r.text, r) 
        except KeyError:
          print ("ERROR", data)
        #-------------------->
        #files = sess.get("https://api.telegram.org/bot"+acc_key+"/getFile?file_id=AgACAgIAAxkBAANYX0TtSf9F29qtohwd4fRt3tbPUOwAAm6uMRs9VyhK-m0Xn2NXE9LNBNmWLgADAQADAgADeAADkXkAAhsE")
        #files = sess.get("https://api.telegram.org/file/bot"+acc_key+"/photos/file_1.jpg")
        #with open("file_1.jpg", 'wb') as new_file:
        #    new_file.write(files.content)
        #file = open("file_0.jpg","wb")
        #file.write(files.content)
        #file.close()
        #-------------------->
 
def thread_function():
        while True:
           if int(time.strftime("%M")) % 10 == 0: # 1 минута
              print (time.time(), time.ctime(), time.strftime("%M"))
              #************PARSING*********
              prime_ru()
              time.sleep(60*10)  
        
application = tornado.web.Application([
    (r'/', getToken),
])

                 


if __name__ == '__main__':
    threads = []
    x = threading.Thread(target=thread_function)
    threads.append(x)
    x.start()
    http_server = tornado.httpserver.HTTPServer(application, ssl_options={"certfile":"ssl/cert.crt",
                                                                          "keyfile":"ssl/cert.key",
                                                                          "ssl_version": ssl.PROTOCOL_TLSv1})
    http_server.listen(8443)
    tornado.ioloop.IOLoop.instance().start()
    
#{'update_id': 583012228, 'message': {'message_id': 6, 'from': {'id': 603789567, 'is_bot': False, 'first_name': 'Victor', 'username': 'EvilSadko', 'language_code': 'ru'}, 'chat': {'id': 603789567, 'first_name': 'Victor', 'username': 'EvilSadko', 'type': 'private'}, 'date': 1598883774, 'photo': [{'file_id': 'AgACAgIAAxkBAAMGX00Hvtoodjvfs-7zFbSP05VwdngAAqmvMRufTmhKAk80xBeA4gboCG2XLgADAQADAgADbQADQzAAAhsE', 'file_unique_id': 'AQAD6Ahtly4AA0MwAAI', 'file_size': 25667, 'width': 320, 'height': 240}, {'file_id': 'AgACAgIAAxkBAAMGX00Hvtoodjvfs-7zFbSP05VwdngAAqmvMRufTmhKAk80xBeA4gboCG2XLgADAQADAgADeAADRDAAAhsE', 'file_unique_id': 'AQAD6Ahtly4AA0QwAAI', 'file_size': 105954, 'width': 691, 'height': 518}]}}

#{"ok":true,"result":{"file_id":"AgACAgIAAxkBAAMOX00O0wx1D2xcvNY9otEXmsT9pjwAAqWvMRufTmhKXU4eozSwUOMaj1GXLgADAQADAgADdwADcocAAhsE","file_unique_id":"AQADGo9Rly4AA3KHAAI","file_size":543678,"file_path":"photos/file_0.jpg"}}


