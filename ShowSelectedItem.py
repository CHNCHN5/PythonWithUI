import tkinter as tk

# Create a window
window = tk.Tk()

def on_select(event):
    # Get the selected item
    item = listbox.get(listbox.curselection())

    # Display the details
    label.config(text=item)

# Create a listbox
listbox = tk.Listbox(window)
listbox.pack()

# Add some items to the listbox
listbox.insert(tk.END, "Item 1")
listbox.insert(tk.END, "Item 2")
listbox.insert(tk.END, "Item 3")

# Create a label to display the details
label = tk.Label(window)
label.pack()

# Bind an event to the listbox
listbox.bind("<<ListboxSelect>>", on_select)

# Define a function to handle the event


# Start the main loop
window.mainloop()
