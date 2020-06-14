from stem import Signal
from stem.control import Controller
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import time
from fake_useragent import UserAgent
import pickle

# signal TOR for a new connection
def switchIP():
    with Controller.from_port(port = 9051) as controller:
        controller.authenticate()
        controller.signal(Signal.NEWNYM)

# get a new selenium webdriver with tor as the proxy
def my_proxy(PROXY_HOST,PROXY_PORT):
    fp = webdriver.FirefoxProfile()
    #fp = webdriver.FirefoxProfile('/home/sadko/.mozilla/firefox/98dnn9yc.default')
    #webdriver.FirefoxProfile('~/.mozilla/firefox/98dnn9yc.default')
    #fp.set_preference("network.proxy.type", 1)
    #fp.set_preference("network.proxy.socks",PROXY_HOST)
    #fp.set_preference("network.proxy.socks_port",int(PROXY_PORT))

    #fp.update_preferences()
    options = Options()
    #options.add_argument('headless')
    options.add_argument("--headless")
    #options.headless = True
    return webdriver.Firefox(options=options, firefox_profile=fp)

def scroll():
    w = last_height//100
    igg = 100
    for i in range(w):
        proxy.execute_script("window.scrollTo(0, {})".format(igg))
        time.sleep(0.3)
        igg += 100
    

proxy = my_proxy("127.0.0.1", 9050)
#
#proxy.get("https://www.tateward.com/")
proxy.get("https://www.liveauctioneers.com/search/?keyword=rolex&sort=-relevance&status=online")
#time.sleep(10)
#time.sleep(2)
#proxy.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#time.sleep(2)
#proxy.find_element_by_css_selector('.close-button___3kR_Z').click()
#time.sleep(2)
last_height = proxy.execute_script("return document.body.scrollHeight")
print(last_height)
try:
    proxy.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    element = WebDriverWait(proxy, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "close-button___3kR_Z"))
    )
finally:
    proxy.find_element_by_css_selector('.close-button___3kR_Z').click()
    #proxy.quit()

scroll()

html = proxy.page_source
#cookies = proxy.get_cookies()
#print (html)
soup = BeautifulSoup(html, features = "html.parser")
J = soup.find_all('div', {"class": "card___1ZynM cards___2C_7Z"})
for iop in J:
   H = iop.find('img', {"class": "image___2rMaZ img-primary___vK3xm"})
   H1 = iop.find('div', {"class": "item-title-container___3j0W1"})#
   H_s = H1.find('span')
   H_a = iop.find('a', {"class": "link___ link-primary___ item-title___24bKg"}) 
   #H_price = iop.find('span', {"class": "item-current-bid___27IIy"})#
   
   #soup = BeautifulSoup(H)
   #time.sleep(1)
   try:
      print (type(H), H["src"], H_a["href"], H_s.text)#, H_s, H_a)#, H_price)#["src"])# H["src"]
   except:
      print ("ERROR",type(H))

proxy.quit()
#https://www.liveauctioneers.com/item/86200814_1964-diamond-rolex-manual-wind-wrist-watch-in-18k
#<button class="close-button___3kR_Z" e2e="closeButton" type="submit"><span>×</span></button>
#session = requests.session()
##session.proxies = {}
##session.proxies['http'] = 'socks5://127.0.0.1:9050'
##session.proxies['https'] = 'socks5://127.0.0.1:9050'
##headers = {}
##headers['User-agent'] = UserAgent().random
##headers['Accept-Language'] = "en,en-US;q=0,5"
##headers['Content-Type'] = "application/x-www-form-urlencoded"
##headers['Connection'] = "keep-alive"
##headers['Accept'] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
#for cookie in cookies:
#       if cookie['value'] == False:
#          cookie['value'] = True
#       session.cookies.set(cookie['name'], cookie['value'])
##read = session.get("https://www.chrono24.com.ru/search/browse.htm?char=A-Z", headers=headers)    
#print (session.cookies)#(read.text, read)   


#ix = 0
#try:
#  while True:
#      ix += 1
#except KeyboardInterrupt: 
#  cookies = proxy.get_cookies()
#  print (cookies)
#  #pickle.dump(cookies, open("cookies.pkl","wb"))   
#  pass
#https://stackoverflow.com/questions/20986631/how-can-i-scroll-a-web-page-using-selenium-webdriver-in-python
#https://stackoverflow.com/questions/21350605/python-selenium-click-on-button
#https://stackoverflow.com/questions/26566799/wait-until-page-is-loaded-with-selenium-webdriver-for-python
#https://stackoverflow.com/questions/15122864/selenium-wait-until-document-is-ready/15136386
#https://habr.com/ru/post/273089/
