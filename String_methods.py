# String Methods

# Take input from the user
name = input("Enter your Name : ")

print(name)

# Length function return the length of the string
print(len(name))

# Find function return the index of that element
print(name.find("q"))

# Capitalize function is used to convert the first character of a string into upper
print(name.capitalize())

# Upper function is used to convert the string into upper case
print(name.upper())

# Lower function is used to convert the string into lower case
print(name.lower())

# isdigit method is used to find the string have only digits or not it contains only digits it returns True else It returns False
print(name.isdigit())

# By using this isalpha function we can find the string having only characters or not
print(name.isalpha())

# by using this count function we can count the specific char or element in the string
print(name.count(" "))

# by using this replace we can replace the elements
print(name.replace(name,"loves"))

# by using this help function we saw all builtins functions
print(help(str))