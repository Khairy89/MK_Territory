#Part 1 : Basic
#Python Syntax

# print("Welcome to Python programming with Mr.Harjit")

#create 2 variable
course = "Python Fundamentals"
hours = 4

# print(f"You are enrolled in {course} for {hours}")

#Python Comments

"""
Benefits of commenting in code:
1. Improves code readability for others and yourself.
2. Helps in maintaining and updating the code.
3. Facilitates better understanding of the code's functionality and logic.
"""

def calculate_product(num1, num2):
    """
    This function takes two numbers as input and returns their product.
    """
    return num1 * num2

# Example usage
number1 = 3
number2 = 6
product = calculate_product(number1, number2)
#print(f"The product of {number1} and {number2} is {product}")

#Python Variables
# This script creates a simple student database with variables for name, age, GPA, and enrollment status.

# string because names are textual data.
student_name = "John Doe"

# age as an integer because age is a whole number.
student_age = 20

# GPA as a float because GPA can have decimal values.
student_gpa = 3.75

# status as a boolean because it represents a true/false value.
is_enrolled = True

# Printing each variable with a descriptive message.
# print(f"Student Name: {student_name}")
# print(f"Student Age: {student_age}")
# print(f"Student GPA: {student_gpa}")
# print(f"Is Enrolled: {is_enrolled}")

# Part 2 : Data Types and Operations
# Data Type

# This script processes survey data by creating variables for total participants, average age, survey feedback, and participant IDs.

# Storing the total number of participants as an integer because it represents a whole number.
total_participants = 150

# Storing the average age as a float because age can have decimal values.
average_age = 29.5

# Storing the survey feedback as a string because it is textual data.
survey_feedback = "Great session!"

# Storing participant IDs as a list because it is a collection of multiple values.
participant_ids = [101, 102, 103]

# Printing the data type of each variable using the type() function.
# print(f"Data type of total_participants: {type(total_participants)}")
# print(f"Data type of average_age: {type(average_age)}")
# print(f"Data type of survey_feedback: {type(survey_feedback)}")
# print(f"Data type of participant_ids: {type(participant_ids)}")

# Number and casting

# This script asks the user to enter two numbers, performs basic arithmetic operations, and demonstrates type casting.

# Asking the user to enter two numbers
# num1 = input("Enter the first number: ")
# num2 = input("Enter the second number: ")

# Converting the input strings to integers
# num1 = int(num1)
# num2 = int(num2)

# Calculating and printing the sum, difference, product, and quotient
# sum_result = num1 + num2
# difference_result = num1 - num2
# product_result = num1 * num2
# quotient_result = num1 / num2

# print(f"Sum: {sum_result}")
# print(f"Difference: {difference_result}")
# print(f"Product: {product_result}")
# print(f"Quotient: {quotient_result}")

# Casting one number to a float and one to an integer
# num1_float = float(num1)
# num2_int = int(num2)

# Printing the types of the casted numbers
# print(f"Type of num1 after casting to float: {type(num1_float)}")
# print(f"Type of num2 after casting to integer: {type(num2_int)}")


# String
# This script processes the book title "Harry Potter and the Philosopher's Stone" in various ways.

# Storing the book title in a variable
book_title = "Harry Potter and the Philosopher's Stone"

# # Printing the title in uppercase, lowercase, and title case
# print("Uppercase:", book_title.upper())
# print("Lowercase:", book_title.lower())
# print("Title case:", book_title.title())
#
# # Extracting and printing the first 5 characters and the last 5 characters
# print("First 5 characters:", book_title[:5])
# print("Last 5 characters:", book_title[-5:])
#
# # Replacing "Philosopher's" with "Sorcerer's" and printing the updated title
# updated_title = book_title.replace("Philosopher's", "Sorcerer's")
# print("Updated title:", updated_title)


#Part 3: Logical Structures
# Booleans and Operators
# This script assigns boolean variables for voter registration and voting status, and uses logical operators to check conditions.

# # Assigning boolean variables
# is_registered_voter = True
# has_voted = False
#
# # Checking if the person can vote (must be a registered voter and must not have already voted)
# can_vote = is_registered_voter and not has_voted
# if can_vote:
#     print("The person can vote.")
# else:
#     print("The person cannot vote.")
#
# # Checking if the person is either a registered voter or has already voted
# registered_or_voted = is_registered_voter or has_voted
# if registered_or_voted:
#     print("The person is either a registered voter or has already voted.")
# else:
#     print("The person is neither a registered voter nor has already voted.")


# if else
# # This program assesses exam grades based on the user's input.
#
# # Asking the user to input their exam score (out of 100)
# score = int(input("Enter your exam score (out of 100): "))
#
# # Checking the score and printing the appropriate message
# if score >= 90:
#     print("Excellent")
# elif 70 <= score < 90:
#     print("Good")
# else:
#     print("Needs Improvement")

#Part 4: Data Structures
# list

# This script manages a list of dishes for a food delivery app.

# # Creating a list of 5 dishes offered in the app
# dishes = ["Nasi Goreng", "Mee Bandung", "Koewteow Goreng", "Pasta", "Salad"]
#
# # Adding a new dish to the list
# dishes.append("Fries")
#
# # Removing the second dish from the list
# dishes.pop(1)
#
# # Printing the updated menu and the number of dishes
# print("Updated Menu:", dishes)
# print("Number of dishes:", len(dishes))

# Tuples

# This script manages a tuple of top-performing employees.

# Creating a tuple containing the names of 3 employees
# top_employees = ("Amin", "Khairy", "Jamal")
#
# # Trying to add another name to the tuple
# # Tuples are immutable, so you cannot add or change elements once they are created.
# # The following line would raise an error if uncommented:
# # top_employees.append("David")
#
# # Printing the second employee’s name
# print("The second employee is:", top_employees[1])

# Sets

# This script analyzes customer preferences using sets.

# # Creating two sets
# set1 = {'pizza', 'burger', 'pasta'}
# set2 = {'burger', 'sushi', 'pasta'}
#
# # Printing all unique dishes (union of the sets)
# unique_dishes = set1.union(set2)
# print("All unique dishes:", unique_dishes)
#
# # Printing common dishes (intersection of the sets)
# common_dishes = set1.intersection(set2)
# print("Common dishes:", common_dishes)
#
# # Printing dishes in set1 but not in set2
# dishes_in_set1_not_in_set2 = set1.difference(set2)
# print("Dishes in set1 but not in set2:", dishes_in_set1_not_in_set2)


# Dictionaries
# This script creates a contact management system using a dictionary.

# # Creating a dictionary with keys: "Name", "Phone", and "Email"
# contact = {
#     "Name": "John Wick",
#     "Phone": "014 - 44444444",
#     "Email": "johnwick@continental.com"
# }
#
# # Adding a new key "Address" with a sample value
# contact["Address"] = "1 Wall Street Court, USA"
#
# # Updating the phone number
# contact["Phone"] = "098-765-4321"
#
# # Printing all keys and their corresponding values
# for key, value in contact.items():
#     print(f"{key}: {value}")

# Part 5: Loops and Functions
# While loop
# This script automates a countdown timer using a while loop.

# # Initializing the countdown start number
# count = 10
#
# # Using a while loop to print numbers from 10 to 1 in descending order
# while count > 0:
#     print(count)
#     count -= 1
#
# # Printing "Blast off!" when the loop ends
# print("Blast off!")

# function

# This script defines a function to perform basic arithmetic operations and tests it with different inputs.

# def calculate(num1, num2, operator):
#     """
#     This function accepts two numbers and an operator, performs the operation, and returns the result.
#     """
#     if operator == '+':
#         return num1 + num2
#     elif operator == '-':
#         return num1 - num2
#     elif operator == '*':
#         return num1 * num2
#     elif operator == '/':
#         if num2 != 0:
#             return num1 / num2
#         else:
#             return "Error: Division by zero"
#     else:
#         return "Error: Invalid operator"
#
# # Testing the function with different inputs
# print(calculate(10, 5, '+'))  # Output: 15
# print(calculate(10, 5, '-'))  # Output: 5
# print(calculate(10, 5, '*'))  # Output: 50
# print(calculate(10, 5, '/'))  # Output: 2.0
# print(calculate(10, 0, '/'))  # Output: Error: Division by zero
# print(calculate(10, 5, '%'))  # Output: Error: Invalid operator


# Bonus Challenge
# import random
#
# # Creating a random number between 1 and 100
# target_number = random.randint(1, 100)
#
# # Asking the user to guess the number
# while True:
#     guess = int(input("Guess the number between 1 and 100: "))
#
#     if guess > target_number:
#         print("Too high!")
#     elif guess < target_number:
#         print("Too low!")
#     else:
#         print("You win!")
#         break

