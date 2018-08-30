from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# Root properties
root = Tk()
root.resizable(False, False)
root.title("Login Window")

# Say that I'm gay
def gay():
    messagebox.askquestion("Are you gay?", "If a man were to go up to you and then offer some korean spicy garlic beef, would you accept it?")

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
password_entry.config(show="☻")
password_entry.grid(row=1, column=1)

# Submit button
submit_button = Button(root, text="Login", command=gay)
submit_button.grid(row=2, columnspan=2)

root.mainloop()
