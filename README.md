sudo apt install -y mongodb <br/>
sudo pip install pysocks <br/>
sudo pip install requests <br/>
sudo pip install bs4 <br/>
sudo pip install fake-useragent <br/>
sudo pip install pymongo <br/>
sudo pip install tornado <br/>
sudo pip install opencv-python <br/>

1 "POST", "http://178.158.131.41:8800/ - Загрузка больше картинок json: <br/>
пример:
```json
{"process":"loadMore","data_size":100,"start":300}

         {
         "0": {"_id": "5ebda92ab2c79a1115edb9c5", "image": "antiquorum/Ulysse Nardin/3_3_medium_219.jpg", "brand": "Ulysse Nardin", "model": "El Toro Perpetual Calendar", "price": [15000, 25000], "link": "https://catalog.antiquorum.swiss/en/lots/ulysse-nardin-ref-320-00-el-toro-perpetual-calendar-lot-317-219?browse_all=1&page=3&q=Ulysse+Nardin", "info": {"Brand": "Ulysse Nardin", "Model": "El Toro Perpetual Calendar", "Reference": "Ref 320-00", "Year": "Circa 2012", "Bracelet": "Leather with an 18k white gold Ulysse Nardin double deployant clasp", "Numbers": "Case N 499/500", "Caliber": "UN 032", "Dimensions": "43 mm", "Signature": "Dial", "Accessories": "International warranty card"}, "data_size": 100, "start": 300}, 
         "1": {"_id": "5ebda92ab2c79a1115edb9c6", "image": "antiquorum/Ulysse Nardin/2_4_medium_240.jpg", "brand": "Ulysse Nardin", "model": "Freak", "price": [20400, 33150], "link": "https://catalog.antiquorum.swiss/en/lots/ulysse-nardin-ref-016-88-freak-lot-323-240?browse_all=1&page=2&q=Ulysse+Nardin", "info": {"Brand": "Ulysse Nardin", "Model": "Freak", "Reference": "016-88", "Year": "Circa 2000-2002", "Movement No": "014", "Calibre ": "UN 200", "Bracelet": "Navy-blue leather UN strap", "Diameter": "43 mm", "Signature": "Dial", "Accessories": "Box and papers "}, "data_size": 100, "start": 300},
         }
```

2 "POST", "http://178.158.131.41:8800/search" - <br/>
пример: 
```json
{"process":"SearchMore","data_text":"Chanel","type":"Brand"} "Brand/Model"

         {
         "0": {"_id": "5ebda942b2c79a1115edc2f8", "image": "antiquorum/Chanel/0_12_medium_101.jpg", "brand": "Chanel", "model": "J12", "price": [1500, 2500], "link": "https://catalog.antiquorum.swiss/en/lots/chanel-ref-h1007-j12-lot-313-101?browse_all=1&page=1&q=Chanel", "info": {"Brand": "Chanel", "Model": "J12", "Reference": "Ref H1007", "Year": "Circa 2010", "Bracelet": "Ceramic Chanel bracelet with double deployant clasp", "Numbers": "Case N 76233", "Caliber": "2894-2", "Dimensions": "42 mm", "Signature": "Dial"}, "data_size": 31, "posts_count": 31}, 
         "1": {"_id": "5ebda942b2c79a1115edc302", "image": "antiquorum/Chanel/1_12_medium_101.jpg", "brand": "Chanel", "model": "J12", "price": [1500, 2500], "link": "https://catalog.antiquorum.swiss/en/lots/chanel-ref-h1007-j12-lot-313-101?browse_all=1&page=1&q=Chanel", "info": {"Brand": "Chanel", "Model": "J12", "Reference": "Ref H1007", "Year": "Circa 2010", "Bracelet": "Ceramic Chanel bracelet with double deployant clasp", "Numbers": "Case N 76233", "Caliber": "2894-2", "Dimensions": "42 mm", "Signature": "Dial"}, "data_size": 31, "posts_count": 31}
         }
```
