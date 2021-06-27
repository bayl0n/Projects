my_file = open("banana.txt", "w")

my_string = input("What do you want inside of your banana? ")

my_file.write(my_string)

another_file = open("test.txt")

print(another_file.read())

