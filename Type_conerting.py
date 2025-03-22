#Type converting --> The Process of converting one data type to another data type is called Type casting.

name = "Anandam kumar viswajith"   #String
age = 22                           #Integer
cgpa = 7.32                        #Float
graduate = True                    #Boolean

# verify the type to the variable
print(type(name))
print(type(age))
print(type(cgpa))
print(type(graduate))

# in this code we can perform type convertion
age = float(age)
print(age)
print(type(age))

cgpa = int(cgpa)
print(cgpa)
print(type(cgpa))

graduate = str(graduate)
print(graduate)
print(type(graduate))
