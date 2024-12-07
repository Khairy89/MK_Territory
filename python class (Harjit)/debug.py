number = ""
total = 0

while number != "0":
    if total:
        number = input(f"Total now is {total}, would you like to add more? [Input 0 to exit]: ")
    else:
        number = input("Enter your first number to continue sum: ")

    total += int(number)
else:
    print(f"Your final total is {total}.")
