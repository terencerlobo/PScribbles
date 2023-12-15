import datetime
import sqlite3

with sqlite3.connect("BookInfo_PyTask_28_10_2.db") as db:
    cursor = db.cursor()


cursor.execute(""" CREATE TABLE if not exists datetime_TIMESTAMP(
   d1 TIMESTAMP, 
   d2 TIMESTAMP
);""")

date_var100 = datetime.datetime(2022,9,30,0,0,0)
cursor.execute("""INSERT INTO datetime_TIMESTAMP (d1, d2)
VALUES(?,?);""", (date_var100, datetime.datetime.now()))
db.commit()


query = """select * from datetime_TIMESTAMP where d1 < ?;"""
date_var200 = datetime.date(2022,10,1)
cursor.execute(query,[date_var200])
for record in cursor.fetchall():
    format = "%Y-%m-%d"
    date_var_n =  datetime.datetime.strptime(record[0].split(" ")[0], format)#datetime.date(str())
    print(date_var_n)
    print(record[0], ", ", record[1])

date_var1 = datetime.date(2022,8,10)
date_var2 = datetime.date(2022,9,11)

print(date_var2 > date_var1)

db.close()