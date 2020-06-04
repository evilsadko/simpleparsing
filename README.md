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
{"process":"loadMore", "data_size": 10, "start": 8}

         {
          1:{"_id":str(post["_id"]), 
          "image":post["Image"],
          "brand":post["Brand"], 
          "model":post["Model"],
          "price":post["Price"], 
          "link":post["link"],
          "info": post["Info"], 
          "data_size":len(posts),
          "start":data_json['start']},
          2:{"_id":str(post["_id"]), 
          "image":post["Image"],
          "brand":post["Brand"], 
          "model":post["Model"],
          "price":post["Price"], 
          "link":post["link"],
          "info": post["Info"], 
          "data_size":len(posts),
          "start":data_json['start']}
         }
```

2 "POST", "http://178.158.131.41:8800/search" - <br/>
```json
{"process":"Search", "data_text": "name", "type": "Brand/Model"} 
```
пример: 
```json
{"process":"SearchMore","data_text":"Chanel","type":"Brand"}

         {
         "0": {"_id": "5ebda942b2c79a1115edc2f8", "image": "antiquorum/Chanel/0_12_medium_101.jpg", "brand": "Chanel", "model": "J12", "price": [1500, 2500], "link": "https://catalog.antiquorum.swiss/en/lots/chanel-ref-h1007-j12-lot-313-101?browse_all=1&page=1&q=Chanel", "info": {"Brand": "Chanel", "Model": "J12", "Reference": "Ref H1007", "Year": "Circa 2010", "Bracelet": "Ceramic Chanel bracelet with double deployant clasp", "Numbers": "Case N 76233", "Caliber": "2894-2", "Dimensions": "42 mm", "Signature": "Dial"}, "data_size": 31, "posts_count": 31}, 
         "1": {"_id": "5ebda942b2c79a1115edc302", "image": "antiquorum/Chanel/1_12_medium_101.jpg", "brand": "Chanel", "model": "J12", "price": [1500, 2500], "link": "https://catalog.antiquorum.swiss/en/lots/chanel-ref-h1007-j12-lot-313-101?browse_all=1&page=1&q=Chanel", "info": {"Brand": "Chanel", "Model": "J12", "Reference": "Ref H1007", "Year": "Circa 2010", "Bracelet": "Ceramic Chanel bracelet with double deployant clasp", "Numbers": "Case N 76233", "Caliber": "2894-2", "Dimensions": "42 mm", "Signature": "Dial"}, "data_size": 31, "posts_count": 31}
         }
```
