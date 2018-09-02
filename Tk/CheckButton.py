from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()
root.geometry("500x500")

name = StringVar()

def submitvalue():
    messagebox.showinfo("Name Submission", "You have submitted {}".format(name.get()))

# Determines if the user wants to set the Nathan or John 
enable_video = Checkbutton(root, text="Video", variable=name, onvalue="Nathan", offvalue="John")
enable_video.pack()
# enable_video.grid(row=0, column=0)

# Print out the value of number 
video_button = Button(root, text="Submit", command=submitvalue)
video_button.pack()

video_label = Label(root, textvariable=name)
video_label.pack()

root.mainloop()
