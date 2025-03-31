# Lambda : Lambda functions are annonymous function means there is no definition for this function. normal function starts
#          with def keyword in this annonymos function there is no def keyword we use lambda keyword
#          1. In lambda function having only single expression.
#          2. it allows no.of arguments but it allows only single expression.

sum = lambda a,b:a+b
a = int(input("Enter a value : "))
b = int(input("Enter b value : "))
print(sum(a,b))
