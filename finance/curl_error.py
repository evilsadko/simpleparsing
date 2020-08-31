import os
import sys
#from libraries import curl
from parsing import *

#BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/"  # Корень проекта
#sys.path.append(BASE_PATH)  # Корень проекта в пути, чтобы работал импорт от корня
#print (BASE_PATH)




url = 'http://export.finam.ru/export9.out?market=14&em=22460&token=03AGdBq25JK0Ett3Df9GXK4-SGvLFFEkzkLNQHB05zskNzI5gNle1UUpE0TBoQopnd3O5CbsGPy5y6OpzM8gnt3er4AAOm6sQBw57u6IiLzUyqzj_DXRRPJ3f6zyLFnONJbEgRmrfApBAKhrXdcyZBbsFFxsnnRj33u9bdbDKEPjwMDKuAfKNhY6JFkZ9y9uaNwDiJZ_jDiLA55rEadG4AN6qqXZg27tAChzCPH086EmOIwqqYitizZrkWAs5A7KmniSStRhPm30PJUotqY5avPC7eWKeAJRaYBPYCieaKACuNK4QcOw031jGOslkyOXeyZSgXGvbSqXg4wnVovbWYDV3vbQRI1oCCTSf7v1KZ_7HgoIQu_Iig34dEc1eTSJY3407QFaStJkTU&code=SPFB.BR&apply=0&df=17&mf=8&yf=2019&from=17.9.2019&dt=17&mt=8&yt=2019&to=17.9.2019&p=1&f=SPFB.BR_2019917_2019917&e=.txt&cn=SPFB.BR&dtf=1&tmf=1&MSOR=1&mstime=on&mstimever=1&sep=1&sep2=1&datf=12&at=1'
#print (url)
sess = RequestLib()
response = sess.get(url, True).text
#response = curl.curl_get(url)

print("ANSWER:",response)
