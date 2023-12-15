import sqlite3

with sqlite3.connect("contacts.db") as db:
    cursor = db.cursor()

cursor.execute("""Create table if not exists Names(id INTEGER PRIMARY KEY, firstname text, lastname text, phonenumber text); """)

cursor.execute("""Insert into Names(id, firstname, lastname, phonenumber) values ("60", "Simon","Pierre", "4562301")""")
db.commit()

cursor.execute("""Insert into Names(id, firstname, lastname, phonenumber) values ("70", "Simon","Pierre", "4562301")""")
db.commit()

db.close()

def viewphonebook():
    cursor.execute("Select * from Names")
    for x in cursor.fetchall():
        print(x)

def deleterecord():
    selectedid = int(input("Enter ID: "))
    cursor.execute("Delete from Names where id = ? ", [selectedid])
    cursor.execute("select * from Names")
    for x in cursor.fetchall():
        print(x)
    db.commit()

def main():
    again = "y"
    while again == "y":
        print()
        print("Main Menu")
        print()
        print("1) View phone book")
        print("2) Dekete person from phone book")
        print("3) Quit")
        print()
        selection = int(input("Enter your selection: "))
        print()

        if selection == 1:
            viewphonebook()
        elif selection == 2:
            deleterecord()
        elif selection == 3:
            again = "n"
        else:
            print("Incorrect choice")

main()
db.close()
