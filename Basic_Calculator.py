import math

# take input from the user
num1 = int(input("Enter your number 1 : "))
num2 = int(input("Enter your number 2 : "))
# Select your arithmetic operation
operation = input("Enter your operation (+,-,*,/,%)")

if operation == "+":
    print(f"Addition is : ",num1 + num2)
elif operation == "-":
    print("Subtraction is : ",num1 - num2)
elif operation == "*":
    print("Multiplication is : ",num1 * num2)
elif operation == "/":
    print("Division is : ",num1 / num2)
elif operation == "%":
    print("Modules is : ",num1 % num2)
else:
    print(f"{operation} is invalid!")

