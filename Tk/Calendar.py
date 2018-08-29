from tkinter import *
from tkinter import ttk
import time
import calendar

# Initialise root and its properties
root = Tk()
root.title("Calendar")
root.resizable(False, False)

# Defining basic functions
def closeapp():
    quit()

# This function is an event hence why it takes the event parameter
def dateverify(event):
    print("This is the date!")

# Creates a label based on what is read in entry_box
def createlabel():
    entry_text = entry_box.get()
    
    task = Label(root, text=entry_text)
    task.pack()

# Make the date label
date_label = Label(root, text=calendar.month(time.localtime()[0], time.localtime()[1]))
date_label.bind("<Button-1>", dateverify)
date_label.pack()

# Make an entry box
entry_box = Entry(root)
entry_box.pack()

# Make the close button
b1 = Button(root, text="Print", command=createlabel)
b1.pack()

# Run the application in the mainloop
root.mainloop()
