#lesson17-elif.py
#Example 1: Using if-elif-else statements
a = 30
b = 20
# if b > a :
#     print ("b is greater than a")
# elif a == b :
#     print ("a and b are equal")
# else :
#     print ("a is greater than b")
#
# print ("yes") if a>b else print("no")

#Example 2: Using if-elif-else statements with multiple conditions
a = 10
b = 20
c = 30
# if a > b :
#     if a > c :
#         print ("a is the greatest")
#     else :
#         print ("c is the greatest")
# elif b > c :
#     print ("b is the greatest")
# else :
#     print ("c is the greatest")


#Assignment

age = 19

if age >= 20:
    if age > 30:
        print("You are in red group")
    else:
        print("You are in blue group")
else:
    if age < 15:
        print("You are in black group")
    elif age < 18:
        print("You are in green group")
    else:
        print("You are in no specific group")


#Example 3: Using if-elif-else statements with multiple conditions and logical operators
# Categorize a person into groups based on their age. Here are the groups:
# Red Group: Ages greater than 30
# Blue Group: Ages between 20 and 30 (inclusive)
# Black Group: Ages less than 15
# Green Group: Ages between 15 and 18 (inclusive)

age = 25

if age >= 20:
    if age > 30:
        print("You are in red group")
    else:
        print("You are in blue group")
elif age < 15:
    print("You are in black group")
else:
    print("You are in green group")
