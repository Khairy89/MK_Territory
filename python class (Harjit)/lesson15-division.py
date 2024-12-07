#lesson 15 division
# Get two numbers from the user
num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))

# Calculate the sum of the two numbers
sum = int(num1 / num2)
remaining = (num1%num2)

# Display the result
if remaining == 0:
    output = f" {sum}"  # Append 'R' if remaining is not zero
else:
    output = f"{sum}R{remaining}"

print(f"{num1} / {num2} = {output}")  # Print the result

