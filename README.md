sudo apt install -y mongodb <br/>
sudo pip install pysocks <br/>
sudo pip install requests <br/>
sudo pip install bs4 <br/>
sudo pip install fake-useragent <br/>
sudo pip install pymongo <br/>
sudo pip install tornado <br/>
sudo pip install opencv-python <br/>

1 "POST", "http://178.158.131.41:8800/ - Загрузка больше картинок json: <br/>
```json
{"process":"loadMore", "data_size": data_size, "start": start}
```
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
{"process":"Search", "data_text": temp_x, "type": temp_y} 
```
пример: 
```json
{"process":"Search", "data_text": temp_x, "type": temp_y}
```
