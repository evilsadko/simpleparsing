#### Парсинг сайтов, создания базы данных и обучение нейронной сети (часы, автомобили)
connect_ws.py - подключение к websocket www.investing.com для сбора данных </br>
#8833 - brent oil - https://ru.investing.com/commodities/brent-oil-historical-data</br>
#8830 - золото - https://ru.investing.com/commodities/gold-streaming-chart</br>
#8849 - wti oil - https://ru.investing.com/commodities/crude-oil-historical-data</br>
#2186 - USD/RUB - https://ru.investing.com/currencies/usd-rub-historical-data </br>
https://habr.com/ru/post/396505/</br>
https://habr.com/ru/post/327022/</br>
https://habr.com/ru/post/332700/</br>
https://github.com/co11ter/goFAST - FAST</br>
"""
https://ru.wikipedia.org/wiki/Financial_Information_eXchange
https://ru.wikipedia.org/wiki/FAST_протокол
https://www.finam.ru/profile/tovary/brent/export/?market=24&em=19473&token=&code=BZ&apply=0&df=22&mf=7&yf=2020&from=22.08.2020&dt=22&mt=7&yt=2020&to=22.08.2020&p=1&f=BZ_200822_200822&e=.txt&cn=BZ&dtf=1&tmf=1&MSOR=1&mstime=on&mstimever=1&sep=1&sep2=1&datf=12&at=1
беру последню последнюю цену за день. Предпологаю что следующая цена будет +/-1%
коридор движения цены +/- 1%
волатильность - уровень колебаний/волнений
Буре последню цену дня рабочего
Начинаю с рабочего дня - brent - расчитывать процент 
50 вчера 49 87
верхний потолок
нижний потолок
процент
свеча - больше чем минута нет - показатель
"""
