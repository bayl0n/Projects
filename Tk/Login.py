from tkinter import *
from tkinter import ttk

# Root properties
root = Tk()
root.geometry("400x400")
root.title("Login Window")

# Name label
name_label = Label(root, text="Name:")
name_label.grid(row=0, column=0)

# Name input
name_input = Entry(root)
name_input.grid(row=0, column=1)

# Password label
password_label = Label(root, text="Password:")
password_label.grid(row=1, column=0)

# Pasword entry
password_entry = Entry(root)
password_entry.config(show="*")
password_entry.grid(row=1, column=1)

root.mainloop()
