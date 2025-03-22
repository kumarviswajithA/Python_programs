# Valid user input exercise
# 1. username is no more than 12 characters
# 2. username must not contains spaces
# 3. username must not contains digits


username = input("Enter your username : ")

if len(username) > 12:
    print("username must contains less than 12 characters ")
elif not username.find(" ") == -1:
    print("Username can't contain spaces")
elif not username.isalpha():
    print("your username can't contains numbers ")
else:
    print(f"Welcome {username}")