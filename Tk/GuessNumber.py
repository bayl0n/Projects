from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random

# Application class which houses basic functions for application

class App:
    def __init__(self, master):
        self.master = master 

        # Game Variables
        self.guessNumber = random.randint(1, 100)
        self.guessDisplay = IntVar()
        self.guessCounter = 0

        print(self.guessNumber)

        # GUI
        self.masterFrame = Frame(self.master)
        self.topText = Label(self.masterFrame, text="Number of incorrect guesses:")
        self.displayText = Label(self.masterFrame, textvariable=str(self.guessDisplay))

        self.numberEntry = Entry(self.masterFrame)
        self.submitBox = Button(self.masterFrame, text="Submit", command=self.compareValue)

        # Pack widgets
        self.masterFrame.grid(row=0, column=0)
        self.topText.grid(row=0, column=0, columnspan=2)
        self.displayText.grid(row=1, column=0, columnspan=2)

        self.numberEntry.grid(row=2, column=0)
        self.submitBox.grid(row=2, column=1)

    def refreshGame(self):
        self.guessNumber = random.randint(1, 100)
        self.guessCounter = 0
        self.numberEntry.delete(0, END)

    def compareValue(self):

        self.userNumber = self.numberEntry.get()
        
        try:
            if int(self.userNumber) > self.guessNumber:
                self.guessCounter += 1
                messagebox.showinfo("Guess", "The number is lower!")
            elif int(self.userNumber) < self.guessNumber:
                self.guessCounter += 1
                messagebox.showinfo("Guess", "The number is higher!")
            elif int(self.userNumber) == self.guessNumber:
                result = messagebox.askquestion("You win!", "Do you want to play again?")

                if result == 'yes':
                    self.refreshGame()
                    print(self.guessNumber)
                else:
                    pass
            self.guessDisplay.set(self.guessCounter)
        except:
            messagebox.showinfo("Invalid Entry", "Please enter a valid number!")

def main():
    root = Tk()
    root.resizable(False, False)
    root.title("Guessing Game")
    window = App(root)

    root.mainloop()

if __name__ == "__main__":
    main()
