# lambda expression
# Small anonymous functions can be created with the lambda keyword. This function returns the sum of its two arguments: lambda a, b: a+b. 
# Lambda functions can be used wherever function objects are required

def add2Num(a, b):
	return a + b


res = add2Num(5, 12)
print(res)

add2NumL = lambda a, b: a+b

res = add2NumL(2,12)
print(res)


ageChecker = lambda age: True if age>=18 else False

print(ageChecker(18))

