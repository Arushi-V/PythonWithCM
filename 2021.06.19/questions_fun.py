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


# To check if a number is in given range or not

def testRange(n):
	if n in range(6,12):
		print("The number is in range")
	else:
		print("Given number is not in range.")	


testRange(11)


# To check the number of upper case and lower case characters in a string

def testString(s):
	u = 0
	l = 0

	for x in s:
		if x.islower():
			l+=1

		elif x.isupper():
			u+=1

	return {"upper": u, "lower": l}

print(testString("Python is a Programming LanguaGE"))


# to check how many times a character is being repeated in a string

def noOfChar(name):
	d = {}
	for x in name:
		if x in d:
			d[x] += 1
		else:
			d[x] = 1

	return d


print(noOfChar("Chander Mohan Pundhir"))


# WAP to print even numbers from a given list

def even(*e):

	for i in e :
		if i%2 == 0 :
			print(i)


even(2,3,5,7,6,8)


def oddEvenDiff(*n):
	d = {"odd": [], "even": []}
	for i in n:
		if i%2==0:
			d["even"].append(i)
		else:
			d["odd"].append(i)
	return d


res = oddEvenDiff(8,6,4,3,5,1,18,56,43,23)
print("even:", res["even"])
print("odd:", res["odd"])

