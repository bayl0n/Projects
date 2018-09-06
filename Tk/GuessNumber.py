from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random

# Application class which houses basic functions for application

class App:
    def __init__(self, master):
        self.master = master 
        
        # GUI
        self.masterFrame = Frame(self.master)
        self.topText = Label(self.masterFrame, text="The number is:")
        self.displayText = Label(self.masterFrame, text="TEST")

        self.numberEntry = Entry(self.masterFrame)
        self.submitBox = Button(self.masterFrame, text="Submit")

        # Pack widgets
        self.masterFrame.grid(row=0, column=0)
        self.topText.grid(row=0, column=0, columnspan=2)
        self.displayText.grid(row=1, column=0, columnspan=2)

        self.numberEntry.grid(row=2, column=0)
        self.submitBox.grid(row=2, column=1)

    def retrieveValue():
        pass

def main():
    root = Tk()
    root.resizable(False, False)
    root.title("Guessing Game")
    window = App(root)

    root.mainloop()

if __name__ == "__main__":
    main()
