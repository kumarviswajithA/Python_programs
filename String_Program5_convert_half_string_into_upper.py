s = input("Enter your string : ")

mid = len(s)//2

res = s[:mid].upper() + s[mid:]

print(res)