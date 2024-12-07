#lesson18-whileloop.py

# While loop
# A while loop is used to execute a block of code repeatedly as long as a specified condition is true.

# count = 1
#
# while count <= 5:
#     print(count)
#     count += 1
# else:
#     print("The while loop is over.")

password = "" # initialize the password variable
attempts = 0 # initialize the number of attempts

# while password != "123456":
#     password = input("Enter your password: ") # keep asking for password until correct
#     attempts += 1 # increment the number of attempts
#     if password == "123456":
#         print("Access granted.")
#         break # exit the loop if correct password is entered
#
#     if attempts == 3: # if 3 attempts have been made, exit the loop
#         print("Too many attempts. Exiting the program.")
#         break
#
# print("Number of attempts:", attempts) # print the number of attempts

#write a program to find the sum of numbers entered by the user. stop when the user enters 0.
sum = 0

while True:
    num = int(input("Enter a number (0 to exit): "))
    if num == 0:
        break
    sum += num
#print(f"the sum is: {sum}")
print("The sum is:", sum)

#write a program where the user must guess a secret number. keep asking until they guess correctly.
secret_num = 7
guess = 0

while guess != secret_num:
    guess = int(input("Guess the secret number: "))
    if guess == secret_num:
        print("Congratulations! welcome to the secret society.")
    else:
        print("Sorry, wrong secret number.keep trying'!")

