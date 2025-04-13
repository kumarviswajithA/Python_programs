def kth_string(s,k):
    s1 = s.split()
    for i in s1:
        if k == len(i):
            print(i,end = ' ')



s = input("Enter your string : ")
k = int(input("Enter your k value : "))
kth_string(s,k)