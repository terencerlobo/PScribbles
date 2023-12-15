import sqlite3

with sqlite3.connect("BookInfo_PyTask_28_10_2.db") as db:
    cursor = db.cursor()

def display_books(year):
    #quer = """select author, title, data_published from Books where data_published > ? order by data_published asc;"""
    cursor.execute("""select author, title, data_published from Books where data_published > ? order by data_published asc;""", [year])
    for record in cursor.fetchall():
        print(record[0], ", ", record[1], ", ", record[2])
    
    
year = int(input("Enter the published year: "))
display_books(year)


db.close()