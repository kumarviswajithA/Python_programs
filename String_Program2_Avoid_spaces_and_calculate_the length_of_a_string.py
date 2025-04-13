s = input("Enter your string : ")

# Calculate the length of the string...
print(len(s))

# removing the spaces in a string...
res = s.replace(" ","")
print(len(res))


# Another approch

res = [i for i in s if i!= " "]
print(len(res))