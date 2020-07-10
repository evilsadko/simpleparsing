from bs4 import BeautifulSoup
#from requests import Session as R
import requests as R
import time
import random

#htt = "https://www.drive2.ru/cars/"
htt = "https://www.drive2.ru/cars/?all"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
get_f_page = R.get(htt, headers=headers)

soup = BeautifulSoup(get_f_page.text)
cl = soup.find_all('nav', {"class": "c-makes"})
new = []
for link in cl:
       
       new = link.find_all('a')
       
#print (new)
#with open('data_cars.txt', 'w') as f:
#        for g in new:
#           f.write(g.text+","+g.get('href')+'\n')

# Car list href
car_href = {}
for g in new:
     car_href[g.text] = g.get('href')
     #print(g.text+","+g.get('href')+'\n')
     
# Fiend button
# r-button-unstyled button 
# print
Link = "https://www.drive2.ru"
with open('data_cars_1.txt', 'w') as f:
        for J in car_href.keys():
            cret_new_link = Link + car_href[J]
            get_f_page = R.get(cret_new_link, headers=headers)
            soup = BeautifulSoup(get_f_page.text)
            cl = soup.find_all('button', {"class": "r-button-unstyled"})
            SEC = random.choice([1,2,3,4,5,6,0.1,0,3])
            try:
               print (J, cl[0]["data-context"], type(cl))#(soup)
               f.write(J+";"+car_href[J]+";"+ cl[0]["data-context"] +'\n')
            except IndexError:
               print (cl, get_f_page, SEC)#(get_f_page.text, get_f_page.headers, get_f_page, SEC)  
            
            
            time.sleep(SEC)

# Get href from list
#for J in car_href.keys():
#    cret_new_link = Link + car_href[J]
#    get_f_page = R.get(cret_new_link, headers=headers)
#    soup = BeautifulSoup(get_f_page.text)
#    cl = soup.find_all('div', {"class": "o-grid"})
#    print (cl)#(soup)
#    time.sleep(1)
 
 
#Разработал новый тип капчи который сложный для робота
#Выбрать подсвеченную картинку разный оттенок картинки для квадрата
#Станет смертью для AI + шумы, как то так!!! Переложить часть на клиента     
#<a class="u-link-area" data-ym-target="catalog_brand2car" href="/r/acura/rdx/476021465691455550/"></a> = Ссылка на машину
#
#<div class="c-car-card-sa__caption">
#<span class="c-car-title c-link">Acura RDX Белая« РЕДИСКА»</span> = имя машины
#</div>
#
# <div class="c-car-card-sa__location"><span title="Ноябрьск, Ямало-Ненецкий АО, Россия">Ноябрьск, Россия</span></div> - локация
#
# <div class="c-car-card-sa__drive" style="border-color: #ff0033;" title="Драйв">64</div> - Драйв
# <div class="c-car-card-sa__logbook" data-tt="Записей в бортжурнале">10</div>

# Загрузить еще, порядок сортировки
#<button class="r-button-unstyled c-catalog-button" data-action="catalog.morecars" data-slot="catalog.more" data-context="b_2" data-sort="Drive" data-start="20">Показать ещё <span class="c-catalog-spin" data-slot="catalog.spin"></span>
#</button>
