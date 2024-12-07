#lesson19-function.py

def greet (name):
    print("Hello, " + name + "!")
greet("khairi")

def calculate_sum(num1, num2, operator="+"):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2

print(calculate_sum(10, 5))

if __name__ == "__main__":
    #greet(input("What is your name? "))
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    operator = input("Enter operator (+, -, *, /): ")
    result = calculate_sum(num1, num2, operator)
    print("Result: ", calculate_sum(num1, num2, operator))