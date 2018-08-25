# Creating a person class
class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

        print("My name is {} {} and I have been created!".format(self.name, self.surname))

    def greeting(self):
        print("Greetings! My name is {} {} and I am {} years old.".format(self.name, self.surname, self.age))

    def changeName(self):
        self.name = str(input("What is my new name? "))
        print("My new name now is {} {}!".format(self.name, self.surname))

    def askPerson(self):
        self.answer = int(input("What would you like to do?\n1. Greet me\n2. Change my name\n"))
        return self.answer

person1 = Person("Steve", "Rogers", 24)

while True:
    print("if you want to quit, enter 0")
    choice = person1.askPerson()

    if choice == 0:
        break
    elif choice == 1:
        person1.greeting()
    elif choice == 2:
        person1.changeName()
    else:
        print("Sorry try again")
