a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

#print(a,b,c)

if a>b: # a is greater
	if a>c:
		if b>c:
			print(a, b, c)
		else:
			print(a, c, b)
	else:
		print(c, a, b)
else: # b is greater
	if b>c:
		if a>c:
			print(b, a, c)
		else: 
			print(b, c, a)
	else:
		print(c, b, a)

if a<b and a<c and b<c:
	print(a, b, c)
elif b<a and b<c and a<c:
	print(b, a, c)
elif c<a and c<b and a<b:
	print(c, a, b)