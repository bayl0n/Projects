# Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”.

# Iterate from 1 - 100 and print if conditions are met
for unit in range(100):
    number = unit + 1 # As range starts from 0 - 99, number adjusts this
    if number % 15 == 0: # If the number is divisible by 3 and 5
        print("FizzBuzz")
    elif number % 3 == 0: # If the number is divisible by 3
        print("Fizz")
    elif number % 5 == 0: # If the number is divisible by 5
        print("Buzz")
    else:
        print(number) # If these conditions aren't met then print out the number
