from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("500x500")

name = StringVar()

def changevalue():
    print("The box is currently on {}!".format(name.get()))

# Determines if the user wants to set the Nathan or John 
enable_video = Checkbutton(root, text="Video", variable=name, onvalue="Nathan", offvalue="John")
enable_video.pack()
# enable_video.grid(row=0, column=0)

# Print out the value of number 
video_button = Button(root, text="Show value", command=changevalue)
video_button.pack()

video_label = Label(root, textvariable=name)
video_label.pack()

root.mainloop()
