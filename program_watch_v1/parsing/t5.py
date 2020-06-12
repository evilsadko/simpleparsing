from stem import Signal
from stem.control import Controller
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
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
    fp.set_preference("network.proxy.type", 1)
    fp.set_preference("network.proxy.socks",PROXY_HOST)
    fp.set_preference("network.proxy.socks_port",int(PROXY_PORT))
    #fp.update_preferences()
    options = Options()
    #options.headless = True
    return webdriver.Firefox(options=options, firefox_profile=fp)

proxy = my_proxy("127.0.0.1", 9050)
#
#proxy.get("https://www.tateward.com/")
proxy.get("https://www.chrono24.com.ru/search/browse.htm?char=A-Z")
html = proxy.page_source
cookies = proxy.get_cookies()
print (cookies)


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
