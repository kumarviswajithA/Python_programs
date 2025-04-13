def even_words(s):
    s1 = s.split(" ")
    for i in s1:
        if len(i) % 2 == 0:
            print(i,end = " ")
s = input("Enter your content : ")
even_words(s)