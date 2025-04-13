s = input("Enter your string : ")

vowels = "aeiouAEIOU"
s1 = ""
for i in s:
    if i in vowels:
        s1 += i
if s == s1:
    print("given string contains all vowels")
else:
    print("given string contains some consonants")
