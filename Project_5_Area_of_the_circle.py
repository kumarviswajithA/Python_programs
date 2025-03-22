# Area of the circle

import math

radius = float(input("Enter the radius : "))
# Area of the circle formula
# Area = math.pi * radius**2
Area = math.pi * pow(radius , 2)
print(f"Area of the circle is : {round(Area ,2)}cm^2")




# Calculate the Hypotenuse

a = float(input("Enter the a value : "))
b = float(input("Enter the b value : "))

Hypotenuse = math.sqrt(pow(a,2) + pow(b,2))

print(f"Hypotenuse of the circle is : {round(Hypotenuse , 2)}")