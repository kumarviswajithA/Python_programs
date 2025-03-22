# For Loop --> execute a block of code a fixed number of times.
#              You can iterate over a range,sequence,string,etc.
import time

# Example 1 :
for i in range(1,11):
    time.sleep(1)
    print(i,end=" ")

# Example 2:

credit_card = "1234-5678-9012-3456"

for x in credit_card:
    time.sleep(0.25)
    print(x)

# Example 3:
for i in range(1,21):
    if i == 13:
        continue
    else:
        print(i)

#Example 4:
for i in range(1,21):
    if i == 13:
        break
    else:
        print(i)