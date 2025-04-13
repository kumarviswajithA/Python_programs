s = input("Enter your string : ")
digit = any(c.isalpha() for c in s)
char = any(c.isdigit() for c in s)

if digit and char:
    print("given string contain digits and alphabets...")
else:
    print("given string doesn't contains digits and alphabets...")
