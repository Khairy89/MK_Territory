#lesson 11 -formatting
# Define variables
age = 36

# Format a string using an f-string
a = f"my age is {age}"
# print(a)

# Define another variable
price = 78

# Format a string with two decimal places using an f-string
a = f'the price is {price:.2f}'
# print(a)

# Use escape characters in a string
message = 'he\'s a good person'
message = "she said \"python is nice\""

#print(message)

#lesson 12 -escape characters
# Use escape sequences for a new line and a tab
text = "hello, \n\t welcome to python"
#print(text)

# Commented Line
# She said, "It's amazing!"

#lesson 13 - Booleans
a =200
b = 300

# if b > a:
#     print("b is greater than a")
# else:
#     print("b is not greater than a")

#lesson 14 input() function

# Get user input
name = input("Enter your name: ")
print(f"Hello, {name}!")

age = input("Enter your age: ")
age = int(age)
print(f"You are {age} years old.")

# Get two numbers from the user
num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))

# Calculate the sum of the two numbers
sum = num1 + num2

# Display the result
print(f"The sum of {num1} and {num2} is {sum}")



