import time

my_time = int(input("Enter your time : "))

for i in range(1,my_time):
    # print(i)
    seconds = i % 60
    minutes = int(i/60)%60
    hours = int(i /3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(0.25)
print("Times up!")

for j in range(my_time, 0 ,-1):
    # print(i)
    seconds = j % 60
    minutes = int(j/60)%60
    hours = int(j /3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(0.25)
print("Times up!")

