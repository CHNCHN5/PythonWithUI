from tkinter import *

def plus():
    num1=int(entrybox1.get())
    num2=int(entrybox2.get())
    tl = num1 + num2
    label4["text"] = tl

def minus():
    num1=int(entrybox1.get())
    num2=int(entrybox2.get())
    tl = num1 - num2
    label4["text"] = tl

def mul():
    num1=int(entrybox1.get())
    num2=int(entrybox2.get())
    tl = num1 * num2
    label4["text"] = tl

def div():
    num1=int(entrybox1.get())
    num2=int(entrybox2.get())
    tl = num1 / num2
    label4["text"] = tl

def clear():
    entrybox1.delete(0, END)
    entrybox2.delete(0, END)
    label4["text"] = 0


window = Tk()
window.geometry('305x275')
window.title('Calculator')
window.configure(background='cyan')
label1 = Label(window, text="First Number", font=('Arial', 15, ' '), background='cyan')
label1.place(x=5, y=0)
label2 = Label(window, text="Second Number", font=('Arial', 15, ' '), background='cyan')
label2.place(x=5, y=60)
label3 = Label(window, text="Total", font=('Arial', 15, 'bold'), background='cyan')
label3.place(x=5, y=130)
entrybox1 = Entry(window, font=('Arial'))
entrybox1.place(x=5, y=30)
entrybox2 = Entry(window, font=('Arial'))
entrybox2.place(x=5, y=90)
label4 = Label(window, text="0", font=('Arial', 15, ' '), background='cyan')
label4.place(x=6, y=165)
button1 = Button(window, text="+",command=plus, font=('Arial', 15, 'bold'), height="2", width="5")
button1.place(x=5, y=200)
button2 = Button(window, text="-",command=minus, font=('Arial', 15, 'bold'), height="2", width="5")
button2.place(x=80, y=200)
button3 = Button(window, text="x",command=mul, font=('Arial', 15, 'bold'), height="2", width="5")
button3.place(x=155, y=200)
button4 = Button(window, text="/",command=div, font=('Arial', 15, 'bold'), height="2", width="5")
button4.place(x=230, y=200)
button5 = Button(window, text="Clear",command=clear, font=('Arial', 15, 'bold'), height="1", width="5")
button5.place(x=230, y=150)
window.mainloop()
