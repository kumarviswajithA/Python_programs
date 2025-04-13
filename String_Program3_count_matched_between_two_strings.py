s1 = input("Enter your first string : ")
s2 = input("Enter your second string : ")
s1.upper() , s2.upper()
count = 0
for i in s1:
    if i in s2:
        count += 1
print(count)