from tkinter import *
import sqlite3



with sqlite3.connect("Users.db") as db:
    cursor = db.cursor()
cursor.execute("""
        CREATE TABLE IF NOT EXISTS names(
        username TEXT NOT NULL,
        password TEXT NOT NULL);
        """)
        
def check_record(usrname):
    cursor.execute("SELECT username FROM names")
    for name in cursor.fetchall():
        if name == usrname:
            return False
        else:
            continue
    return True
    
def save_record():
    usrname=username.get()
    passwrd=password.get()
    args=(username.get(),password.get())
    sql="INSERT INTO names (username,password)VALUES(?,?)"
    b=check_record(usrname)
    if b == False:
        window.messagebox.showinfo("Username already Exists")
    else:
        cursor.execute(sql,args)
        db.commit()
    
def clear():
    username.delete(0,END)
    password.delete(0,END)
    displaybox.delete(0, END)
    
def display():
    cursor.execute("SELECT * FROM names")
    for row in cursor.fetchall():
        displaybox.insert(END, row)
    
window=Tk()
window.title("Registration Page")
window.geometry("800x400")



label1=Label(text="Enter your username:")
label1.place(x=20,y=50)



username=Entry(text=0,bd=2)
username.place(x=150, y=50, width=200)





label2=Label(text="Enter your password:")
label2.place(x=20,y=80)

password=Entry(text=1,bd=2)
password.place(x=150, y=80, width=200)



save=Button(text="Save",command=save_record)
save.place(x=150, y=120, width=60)




clear=Button(text="Clear", command=clear)
clear.place(x=240, y=120, width=60)




display=Button(text="Display")
display.place(x=40, y=220, width=70)



label2=Label(text="Display all usernames and associated passwords in the database")
label2.place(x=150,y=170)



displaybox=Entry(bd=2)
displaybox.place(x=148,y=190,width=350,height=200)



window.mainloop()



db.close()