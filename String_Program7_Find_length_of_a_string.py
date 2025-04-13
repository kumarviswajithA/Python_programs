# First method ....

s = input("Enter your string : ")
print(len(s))

# Second method ....
count = 0
for i in s:
    count +=1
print(count)

# Third Method.....

res = s.count("")-1
print(res)