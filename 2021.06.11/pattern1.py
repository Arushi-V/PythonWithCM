# WAP to print following pattern
'''
*
**
***
****
*****
'''

n = int(input("Enter a number: "))

for i in range(0, n):
	for j in range(i+1):
		print("*", end="")
	print("")


print("----------***********------------")

for i in range(0, n):
	print("*"*(i+1))

