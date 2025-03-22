# In this project we achieve the shopping cart


item = input("What item would you like to buy : ")
price = float(input("What's the price of the item : "))
quantity = int(input("How many would you like : "))

total = price * quantity

print(f"you buy {quantity} {item}'s")
print(f"Your Total is : {total}")