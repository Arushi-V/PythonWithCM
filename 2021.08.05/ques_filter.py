# WAP to filter prime numbers

inp = map(int, input("Enter an list:").split())
inp = list(inp)

print(inp)

def checkPrime(a):
	for i in range(2,a):
		if a % i == 0 :
			return False 
	return True		



result = list(filter(checkPrime, inp))
print("Prime numbers are :", result)

	