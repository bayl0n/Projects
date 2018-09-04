from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# Create a window
root = Tk()
root.geometry("720x540")
root.resizable(False, False)
root.title("Password Generator by Nathan Baylon")

password_var = "TEXT"

################ INTERFACE ###################

password_label = Label(root, text="Password: ")
password_label.grid(row=0, column=0)

password_display = Label(root, text=password_var)
password_display.grid(row=0, column=1)

# Run window in mainloop
root.mainloop()
