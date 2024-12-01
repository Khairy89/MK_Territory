#lesson 8: Concatenation

# Define variables
first_name = "Khairy"
Second_name = "Fauzi"

# Concatenate first name and second name
full_name = first_name + " " + Second_name
# print(full_name)

# Repeat the word "Hi!" three times
word = "Hi!"
repeated = word * 3
# print(repeated)

# Create a sentence from a list of words
words = ["hello", "world", "today", "is", "rainy"]
sentence = " ".join(words)
# print(sentence)

#lesson 9: f-strings

# f-string example
name = "Khairy"
age = 35

# Create a greeting message using f-string
# greeting = f"My name is {name}, and I am {age} years old."

# Print the greeting message
# print(greeting)

language = "Python"
# print(f"I love {language}!")

#perform Expressions
a = 10
b = 20
# print(f"The sum of {a} and {b} is {a+b}.")

#call functions
def square(x):
    return x*x
num = 27
# print(f"The square of {num} is {square(num)}.")

#put in name and age, then display a message using an f-string
name = "Khairy"
age = 27
# print(f"Hello, {name}! You are {age} years old.")

#define cube(x) function
def cube(x):
    return x ** 3
# print(f"The cube of {num} is {cube(num)}.")

#Call functions cuber_root
cuber_root = int(num ** (1/3))
#print(f"The cube root of {num} is {cuber_root}")

#lesson 10: datetime module

from datetime import datetime

# Get the current date and time
now = datetime.now()
print(now)
print(f"Current date and time: {now.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"The current time now is {now:%H:%M:%S}")

#Time series analysis, aggregate dates, difference


# Joining dataframes

