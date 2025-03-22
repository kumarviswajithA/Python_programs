# Email slicer by using slicing concept in python.

email = input("Enter your e-mail : ")

username = email[:email.index("@")]
domain = email[email.index("@") + 1:]
print(f"Your username is {username} and domain is {domain}")