import os
import cv2
import numpy as np
from mongodb import *


def imgs(x):
      cv2.imshow('Rotat', np.array(x))
      cv2.waitKey(0)
      cv2.destroyAllWindows()
      
class DATA(object):
   def __init__(self):
       self.label = {}
       self.txt = {}

   def parseIMG(self, dir_name):
       path = dir_name+"/"
       print ("PARSING",path)
       for r, d, f in os.walk(path):
           for ix, file in enumerate(f):#[:20000]
#                           #print (file)
                      if ".png" in file: #".jpg" or 
                          img = cv2.imread(os.path.join(r, file))
                          self.file[file.split(".")[0]] = [os.path.join(r, file), img]
                      if ".jpg" in file: #".jpg" or 
                          #img = cv2.imread(os.path.join(r, file))
                          #self.file[file.split(".")[0]] = [os.path.join(r, file), img]   
                          self.label[file.split(".")[0]] = [os.path.join(r, file)] 
#                      if ".json" in file:
#                          #jsf = open(os.path.join(r, file), 'r')
#                          self.label[file.split(".")[0]] = [os.path.join(r, file)]
#                      if ".txt" in file:
#                          #jsf = open(os.path.join(r, file), 'r')
#                          self.txt[file.split(".")[0]] = [os.path.join(r, file)]
                          #self.label[file.split(".")[0]] = [os.path.join(r, file)]
#P = DATA()
#P.parseIMG("data")

G = DATA()
G.parseIMG("data_img")

#Dict = {}
print (len(G.txt), len(G.label))
#print (P.label.keys())
for i in G.label:
    
    #fl_open = open(P.label[i][0]).readlines()
    #P.label[i].append()
    g = G.label[i][0].split("/")
    dump = {"mark" : g[-4],
            "model" : g[-3],
            "_id_" : g[-2], "fl":G.label[i][0]}
    print (dump)            
    #print (_id, mark, model, G.label[i][0])
    img = open(G.label[i][0],"rb").read()
    nparr = np.fromstring(img, np.uint8)
    img_t = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    #imgs(img_t)
    imgs_data_write(nparr, dump)
    #Dict[]
#    for o in fl_open:
#        split_first_str = o.split("\n")[0].split("/")[-2]
#        list = P.label[i]
#        list.append(split_first_str)
        #P.label[i] = list
        #print (list, split_first_str)
        
        
#for i in P.label:
    #fl_open = open(P.label[i][0]).readlines()
#    for o in fl_open:
#        split_first_str = o.split("\n")[0].split("/")[-2]
#        list = P.label[i]
#        list.append(split_first_str)
#    print (i)        
