# Creating a person class
class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

        print("My name is {} {} and I have been created!".format(self.name, self.surname))

    # State the person's name, surname and age
    def greeting(self):
        print("Greetings! My name is {} {} and I am {} years old.".format(self.name, self.surname, self.age))

    # Changes the name of the user
    def changeName(self):
        self.name = str(input("What is my new name? "))
        print("My new name now is {} {}!".format(self.name, self.surname))

    # Interface to interact with Person object
    def askPerson(self):
        self.answer = int(input("What would you like to do?\n1. Greet me\n2. Change my name\n"))
        return self.answer

# Creating a Person object called "person1"
person1 = Person("Steve", "Rogers", 24)

# Conditional loop which allows user to interact with the person1 object indefinitely until the user decides to quit
while True:

    # Quit prompt 
    print("If you want to quit, enter 0")
    choice = person1.askPerson()

    # Conditional statements which allows user to choose which function are called
    if choice == 0:
        break
    elif choice == 1:
        person1.greeting()
    elif choice == 2:
        person1.changeName()
    else:
        #If there isn't a valid choice then the user is prompted again
        print("Sorry try again")
