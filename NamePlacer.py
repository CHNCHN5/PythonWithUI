from tkinter import *

def mess():
    name=entrybox1.get()
    entrybox1.delete(0,END)
    entrybox1.insert(0, f"Hi {name} I'm Juan")
def delete():
    entrybox1.delete(0,END)

window = Tk()
window.geometry('300x120')
window.title('Activity 1')
label = Label(window, text="What is your name?", font=("Arial", 20, "bold"))
label.place(x=0, y=0)
entrybox1 = Entry(window, font=("Arial"))
entrybox1.place(x=5, y=40)
button1 = Button(window, text="Submit", command=mess, font=("Arial", 10, "bold"))
button1.place(x=5, y=70)
button2 = Button(window, text="Clear", command=delete, font=("Arial", 10, "bold"))
button2.place(x=75, y=70)
window.mainloop()
