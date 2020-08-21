import pymysql

class connect_db():
     def __init__(self):
        self.connect = pymysql.connect(host='localhost', user='skynet', password='1qaz', database='pogosov', charset='utf8')
        self.cursor = self.connect.cursor()
     def see_dbs(self):
        self.cursor.execute("SHOW DATABASES")
        for i in self.cursor:
            print (i) 
     def see_table(self, x):
        self.cursor.execute("USE {}".format(x))        
        print (self.cursor.fetchall())
     def create_table(self, x):
        self.cursor.execute("""CREATE TABLE `brentoil` (pid varchar(255), lst_dir varchar(255),
                                                        lst_numeric varchar(255), bid varchar(255), lst varchar(255), 
                                                        sk varchar(255), high varchar(255), low varchar(255), 
                                                        lst_close varchar(255), pc varchar(255), 
                                                        pcp varchar(255), pc_col varchar(255), 
                                                        turnover varchar(255), turnover_numeric varchar(255), 
                                                        time varchar(255), timestmp varchar(255))""")     
                                                         
     def create_data(self, x):

        sql = """INSERT INTO `brentoil` (pid, lst_dir, lst_numeric, lst,bid,
                                         sk, high, low, lst_close, pc, pcp, 
                                         pc_col, turnover, turnover_numeric, time, timestmp) 
                                         VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        
        self.cursor.execute(x) 
        self.connect.commit() 
     #def see_data(self, x):  

#https://ru.investing.com/commodities/brent-oil
#https://ru.investing.com/commodities/crude-oil
