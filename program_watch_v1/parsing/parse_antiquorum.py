from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import requests as R
import time
import random
import json
import os

class RequestLib():
    def __init__(self):
        self.session = R.session()
        #self.session.proxies = {}
        #self.session.proxies['http'] = 'socks5://127.0.0.1:9050'
        #self.session.proxies['https'] = 'socks5://127.0.0.1:9050'
        self.headers = {}
        self.headers['User-agent'] = UserAgent().random
        self.headers['Accept-Language'] = "en,en-US;q=0,5"
        self.headers['Content-Type'] = "application/x-www-form-urlencoded"
        self.headers['Connection'] = "keep-alive"
        self.headers['Accept'] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
    def get(self, http):
        print (http)
        get_page = self.session.get(http, headers=self.headers) 
        return get_page.text 
    def get_img(self, http): 
        get_page = self.session.get(http, headers=self.headers) 
        return get_page   
         
def utils_help(x):
    y = []
    for i in x:
       temp = i.text
       temp = temp.split("\t")
       t0 = [i for i in temp[0].split(" ")[1:-2]]
       t0.append(temp[1].split(" ")[1])
       y.append(t0)
    return y   
       
       #yield t0 
def utils_info(x):
    print (x)   

def create_dir(x):
   x = "antiquorum/"+x
   try:
       os.mkdir(x)
   except FileExistsError:
       pass
   return x    
       


def TT():
  F = open("watch_mark.txt", "r").readlines()
  for f in F:
    T = True
    brand = f.split("\n")[0].split(";")[1]
    path = create_dir(brand)
    #for i in range(49):
    for i in range(4):
      #print (brand)
      SEC = random.choice([2,3,4,5,3,1,1.1,1.5, 0.7])
      time.sleep(SEC)
      if T:
      #try:
              #if T:
                
                Sess = RequestLib()
                http = "https://catalog.antiquorum.swiss/en/lots?page={}&q={}".format(i, brand)
                print ("parsing page", i, brand, http)
                sess = Sess.get(http)
                #print (sess)
                soup = BeautifulSoup(sess)
                J = soup.find_all('div', {"class": "shadow mt-4"})
                HJ = soup.find_all('div', {"class": "row"})
                if len(J) != 0:
                   for ix, link in enumerate(J):
                            time.sleep(1)
                            try:
                               a_link = link.find("a", {"class": "btn btn-danger ladda-button wIndicator"}).text
                            except AttributeError:  
                               a_link = None 
                            try:     
                               price_link = link.find_all("p", {"class": "N_lots_estimation"})#.text
                               price_link = utils_help(price_link)
                            except AttributeError: 
                               price_link = None 
                            try:   
                               info_model = link.find_all("div", {"class": "pt-2 shadow-sm p-2"})
                            except AttributeError: 
                               info_model = None
                               
                            try:   
                               info_lot = link.find_all("div", {"class": "N_lots_price mt-0"})
                            except AttributeError: 
                               info_lot = None
   
                            try:   
                               info_solid = link.find_all("h4")
                            except AttributeError: 
                               info_solid = None                               
                            try:
                               lot_sold = HJ[ix].find("div", {"class": "N_lots_price mt-0"})
                               lot_sold = lot_sold.find("p").text.replace(",", "").replace(":", "").replace("\n","").replace("\t","")#\n\t\t\t\t\t\t
                               lot_sold = lot_sold.split(" ")
                            except AttributeError:  
                               lot_sold = None
                            except IndexError:
                               lot_sold = None 
                            
                            try:
                               new = link.find('div', {"class": "N_lots_description col"}).find('span')['content']
                               href = "https://catalog.antiquorum.swiss"+str(link.find('a')["href"]) #href["href"], 
                               img_link = link.find("img", {"class": "lot_image"})['src']
                               
                               #D[ix] = {"title":new, "href":href, "img":img_link}
                               #print (path)
                               G = open(path+"/"+ str(i)+ "_"+ str(ix) + "_" + img_link.split("/")[-1].split(".")[0] + ".txt", "w")
                               G.write("{}\n{}\n{}\n".format(href, img_link, new))
                               G.write("{}\n".format(info_model)) 
                               G.write("{}\n".format(info_solid))
                               G.write("{}\n".format(lot_sold))
                               G.write("{}\n".format(info_lot))
                               G.write("{}\n".format(price_link))
                               G.close()
                               
                               response = Sess.get_img(img_link)
                               print (img_link, response)
                               if response.status_code == 200:
                                   with open(path+"/"+ str(i)+ "_"+ str(ix) + "_" + img_link.split("/")[-1], 'wb') as fli:
                                       fli.write(response.content) 
                            except AttributeError:
                               pass                
                else:
                   T = False 
      #except R.exceptions.ConnectionError:      
      #        pass
TT()

