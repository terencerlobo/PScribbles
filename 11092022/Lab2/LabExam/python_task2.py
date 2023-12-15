import sqlite3

with sqlite3.connect("BookInfo_PyTask_28_10_2.db") as db:
    cursor = db.cursor()


def display_authors():
    cursor.execute("""select * from Authors""")
    print("Author Name       |   Place of Birth:")
    for record in cursor.fetchall():
        print(record[0], "  | " , record[1])
    

def fetch_details(location):
    print(location)
    quer = """select author, title, data_published from Books where author = (select name from Authors where lower(place_of_birth) = '"""+location.lower()+"""')"""
    cursor.execute(quer)
    for record in cursor.fetchall():
        print(record[0], ", ", record[1], ", ", record[2])
    

display_authors()

location = input("Enter the place of birth: ").lower()
fetch_details(location)


db.close()