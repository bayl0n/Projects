from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import random

# Create a window
root = Tk()
# root.geometry("720x540")
root.resizable(False, False)
root.title("Password Generator by Nathan Baylon")

password_var = StringVar() 
password_var.set("Generate a password")

def generate_password():
    password_var.set(str(random.randint(1,10)))

################ INTERFACE ###################

##### DESCRIPTION FRAME #####

description_frame = Frame(root)
description_frame.grid(row=0, column=0, columnspan=2, sticky="nsew")

description_label = Label(description_frame, text="This is a password generator by Nathan Baylon.")
description_label.pack()


##### GUI #####

interface_frame = Frame(root)
interface_frame.grid(row=1, column=0)

password_display = Label(interface_frame, textvariable=password_var)
password_display.grid(row=0, column=0)

display_frame = Frame(root)
display_frame.grid(row=2, column=0)

# When this button is pressed, a new password is generated

password_generate_button = Button(display_frame, text="Generate", command=generate_password)
password_generate_button.grid(row=0, column=0)

#############################

# Run window in mainloop
root.mainloop()
