# Create a program that accepts an integer and prints the fibonacci sequence to that number

# This function returns the values of the terms within the fibonacci sequence up to a given number
def fibonacci(number):
    # A list is used to easily keep track of the terms in the sequence and to also easily add from previous terms
    fib_list = [0, 1]

    # Format table headings
    print("\nTerm:\tValue:")

    # Iterates to add up two numbers within the list to create a new third value "addedNumber" which is added in later iterations
    for unit in range(number + 1):

        addedNumber= fib_list[unit] + fib_list[unit + 1]
        fib_list.append(addedNumber)

        print("{}.\t{}".format(unit, fib_list[unit]))

# Title message
print("Fibonacci Sequence Generator - Nathan Baylon")
userInput = int(input("Which term would you like to display up to?  ")) # Prompts user to enter number for fibonacci function

# Call the fibonacci function
fibonacci(userInput)
