import sqlite3

with sqlite3.connect("company1.db") as db:
    cursor = db.cursor()
cursor.execute("Create table students(id integer PRIMARY KEY);")
cursor.execute('INSERT INTO students(id) VALUES(1)')
db.commit()
db.close()
