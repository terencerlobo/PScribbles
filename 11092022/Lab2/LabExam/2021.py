from tkinter import *
import sqlite3
from tkinter import messagebox as mbox 
import re
import csv

def csv_download_click():
    with sqlite3.connect("Punitha_user.db") as db:
        cursor = db.cursor()
    cursor.execute("select * from user_names")
    for record in cursor.fetchall():
        print(record, " ==> This is the record..")
        file = open("Records.csv", "a")
        file.write(record[0] + ", " + record[1] + "\n")
        file.close()
        user_name_list.insert(END, record)
    db.close()

def txt_download_click():
    with sqlite3.connect("Punitha_user.db") as db:
        cursor = db.cursor()
    cursor.execute("select * from user_names")
    for record in cursor.fetchall():
        print(record, " ==> This is the record..")
        file = open("Records_txt.txt", "a")
        file.write(record[0] + ", " + record[1] + "\n")
        file.close()
        user_name_list.insert(END, record)
    db.close()


def save_click():
    print("save_click called..")
    user_name = user_name_txt.get()
    pwd = pwd_txt.get()
    create_table(user_name, pwd)

def clear_click():
    print("clear_click called..")
    user_name_txt.delete(0, END)
    pwd_txt.delete(0, END)
    user_name_list.delete(0, END)
    user_name_txt.focus()

def display_click():
    print("Display clicked..")
    
    with sqlite3.connect("Punitha_user.db") as db:
        cursor = db.cursor()
    
    cursor.execute("select * from user_names")
    for record in cursor.fetchall():
        print(record, " ==> This is the record..")
        user_name_list.insert(END, record)
    db.close()
    
def create_table(user_name, pwd):
    print("Create table called..")
    with sqlite3.connect("Punitha_user.db") as db:
        cursor = db.cursor()

    cursor.execute(""" Create table if not exists user_names(user_name text, pwd text);""")

    cursor.execute("select * from user_names")
    user_name_found = False
    for record in cursor.fetchall():
        if(record[0] == user_name):
            user_name_found = True
            mbox.showinfo('User Already Exists','User Name already exists') 
            break

    if(user_name_found == False and password_check(pwd) == True):
        cursor.execute("""Insert into user_names(user_name, pwd) values('""" + user_name + """','"""+pwd+"""');""")
        user_name_txt.delete(0, END)
        pwd_txt.delete(0, END)
        user_name_txt.focus()
    db.commit()
    db.close()



def password_check(pwd):
    valid = False
    numbers = re.findall(r'[/\d/]', pwd)
    if(len(pwd) >= 8 and len(numbers) > 1):
        valid = True
    
    if(valid == False):
        mbox.showinfo('Password Requirements not met!!', 'Password Requirements are not met!!')
    return valid


window = Tk()

window.geometry("750x750")
user_name_lbl = Label(text = "Enter your username: ")
user_name_lbl.place(x=50, y=20)

user_name_txt = Entry(text = "")
user_name_txt.place(x=180, y=20, width=250, height=25)
user_name_txt.focus()


pwd_lbl = Label(text = "Enter your password: ")
pwd_lbl.place(x=50, y=50)

pwd_txt = Entry(text = "")
pwd_txt.place(x=180, y=50, width=250, height=25)

save_btn = Button(text = "Save", command = save_click)
save_btn.place(x=180, y=80, width=120, height=25)

clear_btn = Button(text = "Clear", command = clear_click)
clear_btn.place(x=320, y=80, width=120, height=25)

display_btn = Button(text = "Display", command = display_click)
display_btn.place(x=50, y=220, width=120, height=25)

download_btn = Button(text = "Download as CSV", command = csv_download_click)
download_btn.place(x=50, y=250, width=120, height=25)

download_btn = Button(text = "Download as Text", command = txt_download_click)
download_btn.place(x=50, y=280, width=120, height=25)


user_name_list = Listbox()
user_name_list.place(x=180, y = 140, width = 350, height = 250)

user_name_lbl = Label(text = "Display all usernames and associated passwords in the database")
user_name_lbl.place(x=180, y=120)


window.mainloop()