from tkinter import *
import sqlite3

def calculate_fare_click():
    print("Inside calculate_fare_click..")
    with sqlite3.connect("TravelPrice.db") as db:
        cursor = db.cursor()
    
    cursor.execute("""select travel_price from travel_fare order by client_age asc""")
    total_fare = 0
    for record in cursor.fetchall():
        total_fare = total_fare + int(record[0])
    print(total_fare, " ==> total fare..")
    cost_list.delete(0, END)
    cost_list.insert(END, total_fare)        
    db.close()


def save_click():
    age = int(age_txt.get())
    ticket_fare = 0
    if(age == 2):
        ticket_fare = 0
    if(age >= 3 and age <= 12):
        ticket_fare = 7
    if(age > 12 and age <= 66):
        ticket_fare = 18
    if(age > 66):
        ticket_fare = 13
    create_table(age, ticket_fare)


def create_table(age, ticket_fare):
    with sqlite3.connect("TravelPrice.db") as db:
        cursor = db.cursor()

    cursor.execute(""" Create table if not exists travel_fare(client_age text, travel_price text);""")

    cursor.execute("""Insert into travel_fare(client_age, travel_price) values(?, ?);""", (str(age), str(ticket_fare)))
    age_txt.delete(0, END)
    db.commit()
    db.close()


def display_age_click():
    age_list.delete(0, END)
    with sqlite3.connect("TravelPrice.db") as db:
        cursor = db.cursor()
    
    cursor.execute("""select client_age from travel_fare order by client_age asc""")
    
    for record in cursor.fetchall():
        age_list.insert(END, record)
    db.close()

def display_fare_click():
    fare_list.delete(0, END)
    with sqlite3.connect("TravelPrice.db") as db:
        cursor = db.cursor()
    
    cursor.execute("""select travel_price from travel_fare order by client_age asc""")
    
    for record in cursor.fetchall():
        fare_list.insert(END, record)
    db.close()


def clear_click():
    with sqlite3.connect("TravelPrice.db") as db:
        cursor = db.cursor()
    
    cursor.execute("""delete from travel_fare;""")
    db.commit()
    db.close()
    
    age_txt.delete(0, END)
    age_list.delete(0, END)
    fare_list.delete(0, END)
    cost_list.delete(0, END)
    age_txt.focus()
    

window = Tk()

window.geometry("1000x1000")
window.title("Simple Journey Fare Calculator")



age_lbl = Label(text = "Enter the client's age, one at a time: ")
age_lbl.place(x=50, y=20)

age_txt = Entry(text = "")
age_txt.place(x=280, y=20, width=250, height=25)
age_txt.focus()

save_btn = Button(text = "Save Age", command = save_click)
save_btn.place(x=180, y=80, width=120, height=25)

clear_btn = Button(text = "Clear All", command = clear_click)
clear_btn.place(x=320, y=80, width=120, height=25)


display_btn = Button(text = "Display Age", command = display_age_click)
display_btn.place(x=50, y=220, width=120, height=25)

age_list = Listbox()
age_list.place(x=180, y = 140, width = 200, height = 250)

age_list_lbl = Label(text = "Client's age in years: ")
age_list_lbl.place(x=180, y=120)

display_btn = Button(text = "Display ticket price", command = display_fare_click)
display_btn.place(x=450, y=220, width=120, height=25)

fare_list = Listbox()
fare_list.place(x=600, y = 140, width = 200, height = 250)

fare_list_lbl = Label(text = "Price Per Client £: ")
fare_list_lbl.place(x=600, y=120)

total_cost_lbl = Label(text = "Display Total Cost of the journey: ")
total_cost_lbl.place(x=180, y=500)

display_cost_btn = Button(text = "Display cost £", command = calculate_fare_click)
display_cost_btn.place(x=50, y=540, width=120, height=25)

cost_list = Listbox()
cost_list.place(x=180, y = 520, width = 200, height = 75)

window.mainloop()