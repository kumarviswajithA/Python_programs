def remove_elements(s):
    s1 = ""
    for i in s:
        if i not in s1:
            s1 += i
    print(s1)
s = input("Enter your string : ")
remove_elements(s)