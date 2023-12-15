from tkinter import *

def add_on():
    print("This is the Add on function..")

window = Tk()

window.title("Adding Together")
window.geometry("400*350")

enter_lbl = Label(text = "Enter a number: ")
enter_lbl.place(x=50, y=20, width=100, height=20)

enter_txt = Entry(text = 0)
enter_txt.place(x=150, y=20, width=100, height=25)
enter_txt["justify"] = "center"
enter_txt.focus()

add_btn = Button(text = "Add", command=add_on)
