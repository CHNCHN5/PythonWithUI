import tkinter as tk
import sqlite3
from PIL import ImageTk, Image
from tkinter import messagebox, filedialog
import io

conn = sqlite3.connect('contacts.db')
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS contacts (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100),
                phone VARCHAR(100),
                email VARCHAR(100),
                address VARCHAR(100),
                relationship VARCHAR(100)
            )""")
conn.commit()

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()
    relationship = relationship_entry.get()
    #photo_path = photo_entry.get()

    # Convert photo to binary data
    #photo_data = None
    #if photo_path:
       #with open(photo_path, 'rb') as f:
            #photo_data = f.read()

    c.execute("INSERT INTO contacts (name, phone, email, address, relationship) VALUES (?, ?, ?, ?, ?)",
    (name, phone, email, address, relationship))
    conn.commit()

    clear_entries()

def search_contact():
    keyword = search_entry.get()

    search_result_lbl.config(text="")

    c.execute('''
        SELECT * FROM contacts
        WHERE name LIKE ? OR phone LIKE ? OR email LIKE ? OR address LIKE ? OR relationship LIKE ?
    ''', (keyword, keyword, keyword, keyword, keyword))

    search_results = c.fetchall()
    display_search_results(search_results)

def display_search_results(results):
    search_result_list.delete(0, tk.END)
    counter = 0

    if len(results) > 0:
        for contact in results:
            counter += 1
            contact_info = f"NAME: {contact[1]}\n   PHONE: {contact[2]}\n   ADDRESS: {contact[4]}"
            search_result_list.insert(tk.END, contact_info)
    else:
        search_result_list.insert(tk.END, "No results found.")
        search_result_list.selection_clear(0, tk.END)

    search_result_lbl.config(text=f"Total results: {counter}")

def delete_contact():
    global conn, c

    selected_index = all_contacts_list.curselection()
    if selected_index:
        selected_contact = all_contacts_list.get(selected_index)
        contact_name = selected_contact.split("\n")[0].split(": ")[1]
        contact_phone = selected_contact.split("\n")[1].split(": ")[1]

        confirm = messagebox.askyesno("Confirm Deletion",
                                      f"Are you sure you want to delete {contact_name} in your contacts?")

        if confirm:
            c.execute("DELETE FROM contacts WHERE name=? AND phone=?", (contact_name, contact_phone,))
            conn.commit()

            all_contacts_list.delete(selected_index)
        else:
            pass

def close_windows():
    try:
        if all_contacts_window:
            all_contacts_window.destroy()
    except NameError:
        pass

    try:
        if contact_details_window:
            contact_details_window.destroy()
    except NameError:
        pass

def view_contact_details():
    global contact_details_window

    selected_index = all_contacts_list.curselection()
    if selected_index:
        selected_contact = all_contacts_list.get(selected_index)
        contact_phone = selected_contact.split("\n")[1].split(": ")[1]

        c.execute("SELECT * FROM contacts WHERE phone=?", (contact_phone,))
        contact_details = c.fetchone()

        contact_details_window = tk.Toplevel(root)
        contact_details_window.config(bg='#555555')
        contact_details_window.title("Contact Detail")

        labelttl = tk.Label(contact_details_window, text='CONTACT DETAILS', bg='#555555',fg='white', font=('arial', 12, 'bold'))
        labelttl.grid(row=0, column=0, columnspan=2)

        tk.Label(contact_details_window, text="NAME :", font=('arial', 10, 'bold'), bg='#555555',fg='white').grid(row=1, column=0, sticky=tk.E)
        tk.Label(contact_details_window, text=contact_details[1], bg='#555555',fg='white').grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)

        tk.Label(contact_details_window, text="PHONE :", font=('arial', 10, 'bold'), bg='#555555',fg='white').grid(row=2, column=0, sticky=tk.E)
        tk.Label(contact_details_window, text=contact_details[2], bg='#555555',fg='white').grid(row=2, column=1, padx=10, pady=5, sticky=tk.W)

        tk.Label(contact_details_window, text="EMAIL :", font=('arial', 10, 'bold'), bg='#555555',fg='white').grid(row=3, column=0, sticky=tk.E)
        tk.Label(contact_details_window, text=contact_details[3], bg='#555555',fg='white').grid(row=3, column=1, padx=10, pady=5, sticky=tk.W)

        tk.Label(contact_details_window, text="ADDRESS :", font=('arial', 10, 'bold'), bg='#555555',fg='white').grid(row=4, column=0, sticky=tk.E)
        tk.Label(contact_details_window, text=contact_details[4], bg='#555555',fg='white').grid(row=4, column=1, padx=10, pady=5, sticky=tk.W)

        tk.Label(contact_details_window, text="RELATIONSHIP :", font=('arial', 10, 'bold'), bg='#555555',fg='white').grid(row=5, column=0, sticky=tk.E)
        tk.Label(contact_details_window, text=contact_details[5], bg='#555555',fg='white').grid(row=5, column=1, padx=10, pady=5, sticky=tk.W)

        #if contact_details[6]:
            #temp_file = contact_details[6]
            #with open(temp_file, "wb") as file:
                #file.write(image_blob)
            #image = Image.open(temp_file)
            #photo = ImageTk.PhotoImage(image)
            #label = Label(root, image=photo)
            #label.pack()

        contact_details_window.protocol("WM_DELETE_WINDOW", contact_details_window.destroy)

def display_all_contacts():
    global all_contacts_list, all_contacts_window, photo_delete, photo_details

    search_result_lbl.config(text="\"No Searched Contact\"")
    search_result_list.delete(0, tk.END)
    clear_entries()

    c.execute("SELECT * FROM contacts")
    all_contacts = c.fetchall()

    all_contacts_window = tk.Toplevel(root)
    all_contacts_window.config(bg='#777777')
    all_contacts_window.title("All Contacts")

    all_contacts_list = tk.Listbox(all_contacts_window, height=10, width=50, bg='#555555', fg='white')
    all_contacts_list.pack(padx=10, pady=10)

    for contact in all_contacts:
        contact_info = f" NAME: {contact[1]}\n  PHONE: {contact[2]}\n   ADDRESS: {contact[4]}"
        all_contacts_list.insert(tk.END, contact_info)

    #scrollbar = tk.Scrollbar(all_contacts_window)
    #scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    #all_contacts_list.config(yscrollcommand=scrollbar.set)
    #scrollbar.config(command=all_contacts_list.yview)

    image3 = Image.open("image_delete.png")
    new_size3 = (20, 20)
    resized_image3 = image3.resize(new_size3)
    photo_delete = ImageTk.PhotoImage(resized_image3)
    delete_button = tk.Button(all_contacts_window, image=photo_delete, text="Delete ", compound='right', command=delete_contact, border=1, bg='#cccccc', font=('arial', 10, 'bold'))
    delete_button.pack(pady=5)

    image4 = Image.open("image_details.png")
    new_size4 = (18, 18)
    resized_image4 = image4.resize(new_size4)
    photo_details = ImageTk.PhotoImage(resized_image4)
    view_details_button = tk.Button(all_contacts_window, image=photo_details, text="View Details ", compound='right', command=view_contact_details, border=1, bg='#cccccc', font=('arial', 10, 'bold'))
    view_details_button.pack(pady=10)

    all_contacts_window.protocol("WM_DELETE_WINDOW", close_windows)

    #for contact in all_contacts:
        #photo_path = contact[6]

        #if photo_path:
            #image = Image.open(photo_path)
            #image = image.resize((20, 20))  # Adjust the size as needed
            #photo = ImageTk.PhotoImage(image)
            #all_contacts_list.itemconfig(all_contacts.index(contact), image=photo)
            #all_contacts_list.image = photo
        #else:
            #placeholder_image = Image.open("placeholder.jpg")
            #placeholder_image = placeholder_image.resize((50, 50))  # Adjust the size as needed
            #placeholder_photo = ImageTk.PhotoImage(placeholder_image)
            #all_contacts_list.itemconfig(all_contacts.index(contact), image=placeholder_photo)
            #all_contacts_list.image = placeholder_photo

#def choose_photo():
    #file_path = tk.filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif")])

    #photo_entry.delete(0, tk.END)
    #photo_entry.insert(tk.END, file_path)

    #if file_path:
        #image = Image.open(file_path)
        #image = image.resize((100, 100))
        #photo = ImageTk.PhotoImage(image)
        #photo_label.configure(image=photo)
        #photo_label.image = photo

def choose_photo1():
    comingsoon = tk.Toplevel(root)
    comingsoon.geometry("200x100")
    comingsoon.config(bg='#777777')
    comingsoon.resizable(0, 0)
    comingsoon.title("Notice")

    labelcs = tk.Label(comingsoon, text='Wala pa po ツ', font=('impact', 20, 'bold'), bg='#777777')
    labelcs.grid(padx=15, pady=30)

def save_contact(contact_name):
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()
    relationship = relationship_entry.get()

    c.execute("UPDATE contacts SET name=?, phone=?, email=?, address=?, relationship=? WHERE name=?",
              (name, phone, email, address, relationship, contact_name))
    conn.commit()

    display_all_contacts()

def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
    relationship_entry.delete(0, tk.END)
    search_entry.delete(0, tk.END)
    search_result_list.delete(0, tk.END)
    search_result_lbl.config(text="No Searched Contact")
    #photo_entry.delete(0, tk.END)
    #photo_label.config(image="")
    #photo_label.image = None
    #photo_label.photo = None

    try:
        if onselect:
            onselect.destroy()
    except NameError:
        pass


def on_select(event):
    global onselect

    try:
        select = search_result_list.curselection()
        if select:
            selected_contact = search_result_list.get(select)
            contact_phone = selected_contact.split("\n")[1].split(": ")[1]

            c.execute("SELECT * FROM contacts WHERE phone=?", (contact_phone,))
            contact_details = c.fetchone()

            onselect = tk.Toplevel(root)
            onselect.resizable(0, 0)
            onselect.config(bg='#555555')
            onselect.title("Contact Details")

            labelttl = tk.Label(onselect, text='CONTACT DETAILS', font=('arail', 12, 'bold'), bg='#555555',fg='white')
            labelttl.grid(row=0, column=0, columnspan=2)

            tk.Label(onselect, text="NAME :", font=('arial', 10, 'bold'), bg='#555555',fg='white').grid(row=1, column=0, sticky=tk.E)
            tk.Label(onselect, text=contact_details[1], bg='#555555',fg='white').grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)

            tk.Label(onselect, text="PHONE :", font=('arial', 10, 'bold'), bg='#555555',fg='white').grid(row=2, column=0, sticky=tk.E)
            tk.Label(onselect, text=contact_details[2], bg='#555555',fg='white').grid(row=2, column=1, padx=10, pady=5, sticky=tk.W)

            tk.Label(onselect, text="EMAIL :", font=('arial', 10, 'bold'), bg='#555555',fg='white').grid(row=3, column=0, sticky=tk.E)
            tk.Label(onselect, text=contact_details[3], bg='#555555',fg='white').grid(row=3, column=1, padx=10, pady=5, sticky=tk.W)

            tk.Label(onselect, text="ADDRESS :", font=('arial', 10, 'bold'), bg='#555555',fg='white').grid(row=4, column=0, sticky=tk.E)
            tk.Label(onselect, text=contact_details[4], bg='#555555',fg='white').grid(row=4, column=1, padx=10, pady=5, sticky=tk.W)

            tk.Label(onselect, text="RELATIONSHIP :", font=('arial', 10, 'bold'), bg='#555555',fg='white').grid(row=5, column=0, sticky=tk.E)
            tk.Label(onselect, text=contact_details[5], bg='#555555',fg='white').grid(row=5, column=1, padx=10, pady=5, sticky=tk.W)

            onselect.protocol("WM_DELETE_WINDOW", onselect.destroy)

    except IndexError:
        pass

def disappear_text():
  addlabel.config(text="")
  root.after(3000, disappear_text)

root = tk.Tk()
root.title("Contact Application")
root.config(bg='#777777')
root.geometry("324x549")
root.resizable(0,0)

labelttl = tk.Label(root, text='Contacts', font=('impact', 20, 'bold'), bg='#777777')
labelttl.grid(row=0, column=0, columnspan=2, pady=5)

tk.Label(root, text='Name :', font=('roboto', -13, 'bold'), bg='#777777').grid(row=1, column=0, padx=0, pady=5)
name_entry = tk.Entry(root, bg='#555555', fg='white')
name_entry.grid(row=1, column=1)

tk.Label(root, text='Phone :', font=('roboto', -13, 'bold'), bg='#777777').grid(row=2, column=0, padx=0, pady=5)
phone_entry = tk.Entry(root, bg='#555555', fg='white')
phone_entry.grid(row=2, column=1)

tk.Label(root, text='Email :', font=('roboto', -13, 'bold'), bg='#777777').grid(row=3, column=0, padx=0, pady=5)
email_entry = tk.Entry(root, bg='#555555', fg='white')
email_entry.grid(row=3, column=1)

tk.Label(root, text='Address :', font=('roboto', -13, 'bold'), bg='#777777').grid(row=4, column=0, padx=0, pady=5)
address_entry = tk.Entry(root, bg='#555555', fg='white')
address_entry.grid(row=4, column=1)

tk.Label(root, text='Relationship :', font=('roboto', -13, 'bold'), bg='#777777').grid(row=5, column=0, padx=0, pady=5)
relationship_entry = tk.Entry(root, bg='#555555', fg='white')
relationship_entry.grid(row=5, column=1)

#photo_label = tk.Label(root)
#photo_label.grid(row=5, column=1)

image1 = Image.open("image_chPhoto.png")
new_size1 = (20, 20)
resized_image1 = image1.resize(new_size1)
photo_pic = ImageTk.PhotoImage(resized_image1)
choose_photo_button = tk.Button(root, image=photo_pic, text='Choose Photo ', compound='right', command=choose_photo1, font=('Roboto', -13, 'bold'), border=1, bg='#cccccc')
choose_photo_button.grid(row=6, column=0, padx=0, pady=5)

#photo_entry = tk.Entry(root, width=30)
#photo_entry.grid(row=9, column=1)

image2 = Image.open("image_plus.png")
new_size2 = (12, 12)
resized_image2 = image2.resize(new_size2)
photo_plus = ImageTk.PhotoImage(resized_image2)
add_button = tk.Button(root, image=photo_plus, text=' Add Contact', compound='left', command=lambda: [add_contact(), addlabel.config(text="Contact Saved!", state="normal", fg='white', font=('roboto', -15, ''))], font=('roboto', -13, 'bold'), border=1, bg='#cccccc')
add_button.grid(row=9, column=0, padx=0, pady=5)
addlabel = tk.Label(root, text="", bg='#777777')
addlabel.grid(row=9, column=1, padx=0, pady=5)

image5 = Image.open("image_clear.png")
new_size5 = (17, 17)
resized_image5 = image5.resize(new_size5)
photo_clear = ImageTk.PhotoImage(resized_image5)
clear_button = tk.Button(root, image=photo_clear, text='Clear ', compound='right', command=clear_entries, font=('roboto', -13, 'bold'), border=1, bg='#cccccc')
clear_button.grid(row=7, column=0, padx=0, pady=5)

frame = tk.Frame(root, bg='#444444')
frame.grid(row=10, column=0, columnspan=2, padx=0, pady=5)

show_all_button = tk.Button(frame, text='All Contacts', command=display_all_contacts, font=('roboto', -13, 'bold'), border=1, bg='#cccccc')
show_all_button.grid(row=2, column=0, columnspan=3, padx=10, pady=3, sticky="E")

search_entry = tk.Entry(frame, bg='#777777', fg='white')
search_entry.grid(row=0, column=0, columnspan=2, ipadx=5)

image4 = Image.open("image_search.png")
new_size4 = (15, 15)
resized_image4 = image4.resize(new_size4)
photo_search = ImageTk.PhotoImage(resized_image4)
search_button = tk.Button(frame, image=photo_search, text='Search ', compound='right',command=search_contact, font=('roboto', -13, 'bold'), border=1, bg='#cccccc')
search_button.grid(row=0, column=0, padx=15, pady=5, sticky='w')

search_result_list = tk.Listbox(frame, height=10, width=50, bg='#555555', fg='white')
search_result_list.bind("<<ListboxSelect>>", on_select)
search_result_list.grid(row=1, column=0, columnspan=2, padx=10, pady=0)

search_result_lbl = tk.Label(frame, text='No Searched Contact', font=('roboto', -13, 'bold'), bg='#444444', fg='white')
search_result_lbl.grid(row=2, column=0, columnspan=3, padx=7, pady=5, sticky="W")

#scrollbar = tk.Scrollbar(root)
#scrollbar.grid(row=11, column=2, sticky=tk.N+tk.S)
#search_result_list.configure(yscrollcommand=scrollbar.set)
#scrollbar.configure(command=search_result_list.yview)
root.after(3000, disappear_text)
root.mainloop()
