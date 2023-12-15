import sqlite3

with sqlite3.connect("BookInfo_PyTask_28_10_2.db") as db:
    cursor = db.cursor()


def display_authors(author):
    cursor.execute("""select author, title, data_published from Books where author = ? order by data_published asc;""", [author])
    file = open("Booklist.txt", "w")
    file.write("This file contains the following record: \n")
    
    for record in cursor.fetchall():
        print(record[0], ", ", record[1], ", ", record[2])
        file.write(record[1] + " - " + record[0] + " - " + str(record[2])+ "\n")
    file.close()   

author = input("Enter the name of the author: ")
display_authors(author)

db.close()