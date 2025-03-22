# we wright voter eligiblity code

age = int(input("Enter your age : "))
if age >= 100:
    print("You are too old!")
elif age >= 18:
    print("Your are eligible for vote")
elif age == 0:
    print("Please Enter a valid age")
elif age < 0:
    print("Age must be positive")
else:
    print("Your not eligible for Vote!")