# While Loop -->  Execute some code while some condition is true

# Example 1 :
name = input("Enter your name : ")

while name == "":
    print("You did not enter your name ")
    name = input("Enter your name : ")

print(f"hello {name}")

# Example 2 :

age = int(input("Enter your age : "))
while age < 0:
    print("Age can't be a negative")
    age = int(input("Enter your are : "))
print(f"Ypu are {age} Years old")

# Example 3:

food = input("Enter a food u like (q to quit) : ")

while not food == "q":
    print(f"You like {food}")
    food = input("Enter a food u like (q to quit) : ")
print("bye")

# Example 3 :

num = int(input("Enter your number between 1 - 10 : "))
while num < 1 or num > 10:
    print(f"{num} is not valid!")
    num = int(input("Enter your number between 1 - 10 : "))
print(f"Your number is {num}")

