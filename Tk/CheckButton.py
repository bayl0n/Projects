from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()
root.geometry("500x500")

name = StringVar()

def submitvalue():
    if len(name.get()) == 0:
        messagebox.showinfo("Error", "You have submitted no name.")
    else:
        messagebox.showinfo("Name Submission", "You have submitted {}".format(name.get()))

# Determines if the user wants to set the Nathan or John 
enable_name = Checkbutton(root, text="Name", variable=name, onvalue="Nathan", offvalue="John")
enable_name.pack()
# enable_name.grid(row=0, column=0)

# Print out the value of number 
name_button = Button(root, text="Submit", command=submitvalue)
name_button.pack()

name_label = Label(root, textvariable=name)
name_label.pack()

root.mainloop()
