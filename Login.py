from tkinter import *
from tkinter import messagebox

class login_form:

	def login(self):

		if user_inp.get() == "chan" and pass_inp.get() == "123":
			window.destroy()
			import logged_in
		elif user_inp.get() == "" and pass_inp.get() == "":
			messagebox.showinfo('Error', 'Please fill up the form')
			user_inp.set("")
			pass_inp.set("")
		elif user_inp.get() == "":
			messagebox.showinfo('Error', 'Please insert your username.')
			user_inp.set("")
			pass_inp.set("")
		elif pass_inp.get() == "":
			messagebox.showinfo('Error', 'Please insert your password.')
			user_inp.set("")
			pass_inp.set("")
		else:
			messagebox.showinfo('Error', 'Incorrect username or password')
			user_inp.set("")
			pass_inp.set("")

	def destroy(self):
		window.destroy()

	def __init__(self,window):
		self.window=window
		window.title("Login Form")
		window.configure(bg="powderblue")

		login_label=Label(window,text="Login",font="arial 30 bold",bg="powderblue")
		login_label.place(x=150,y=20)

		user_label=Label(window,text="User :",font="arial 15 ",bg="powderblue")
		user_label.place(x=100,y=90)

		global  user_inp
		global  pass_inp
		user_inp=StringVar()
		pass_inp=StringVar()

		user_e=Entry(window,textvariable=user_inp)
		user_e.place(x=170,y=93,height=25)

		pass_label=Label(window,text="Password :",font="arial 15 ",bg="powderblue")
		pass_label.place(x=52,y=140)

		pass_e=Entry(window,textvariable=pass_inp,show="*")
		pass_e.place(x=170,y=140,height=25)

		login_b=Button(window,text="Login",font="arial 12 ",bg="white",command=lambda :self.login())
		login_b.place(x=175,y=190)

		exit_b=Button(window,text="Exit",font="arial 10 ", bg="white",command=lambda :self.destroy())
		exit_b.place(x=183,y=230)

window = Tk()
obj=login_form(window)
window.geometry("400x300",)
window.resizable(False, False)
window.mainloop()
