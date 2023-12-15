import sqlite3

with sqlite3.connect("BookInfo_PyTask_28_10_2.db") as db:
    cursor = db.cursor()

cursor.execute(""" Create table if not exists Authors(name text, place_of_birth text);""")

cursor.execute("""Insert into Authors(name, place_of_birth) values("Agatha Christie", "Torquay");""")
db.commit()

cursor.execute("""Insert into Authors(name, place_of_birth) values("J.K. Rowling", "Bristol");""")
db.commit()

cursor.execute("""Insert into Authors(name, place_of_birth) values("Oscar Wilde", "Dublin");""")
db.commit()

cursor.execute(""" Create table if not exists Books(ID integer primary key, title text, author text, data_published int);""")

cursor.execute("""Insert into Books(title, author, data_published) values("De Profundis", "Oscar Wilde", "1905");""")
db.commit()

cursor.execute("""Insert into Books(title, author, data_published) values("Harry Potter and the Chamber of secrets", "J.K Rowling", "1998");""")
db.commit()

cursor.execute("""Insert into Books(title, author, data_published) values("The seven dials mystery", "Agatha Christie", "1929");""")
db.commit()

cursor.execute("""Insert into Books(title, author, data_published) values("The picture of Dorian Gray", "Oscar Wilde", "1890");""")
db.commit()

cursor.execute("""Insert into Books(title, author, data_published) values("Murder on the Orient Express", "Agatha Christie", "1934");""")
db.commit()

cursor.execute("""Insert into Books(title, author, data_published) values("Harry Potter and the prisoner of Azkaban", "J.K. Rowling", "1999");""")
db.commit()

db.close()
