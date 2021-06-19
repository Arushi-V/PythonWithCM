# Questions

# Sum of numbers

def sum(*n):
	total = 0

	for x in n:
		total += x
	return total

print(sum(2, 3, 6, 8))	


# Product of numbers :

def multiply(*n):
	total = 1

	for x in n:
		total *= x
	return total

print(multiply(2, 3, 6, 8))		


# Reverse of String using Slice

def reverseStr(str):
	return str[::-1]


print(reverseStr("Arushi"))


# Reverse of String using For Loop

def revStr(str1):
	rStr =""	
	for i in range(len(str1)-1,-1,-1):
		rStr += str1[i]
	return rStr


print(revStr("Arushi"))

# Factoral of a number

def factorial(n):
	fact = 1
	for x in range(n,1,-1):
		fact *= x
	return fact


print(factorial(5))