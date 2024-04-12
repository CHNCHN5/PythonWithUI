from tkinter import *

def logout():
    window.destroy()
    import Login

def destroy():
    window.destroy()

window = Tk()

window.geometry('300x120')
window.resizable(False, False)
window.title('Account')
window.configure(bg="powderblue")
label = Label(window, text="Logged In!", font=("Arial", 20, "bold"), bg="powderblue")
label.place(x=80, y=10)
button1 = Button(window,command=logout, text="logout", font=("Arial", 10, "bold"), bg="white")
button1.place(x=120, y=70)

window.mainloop()
