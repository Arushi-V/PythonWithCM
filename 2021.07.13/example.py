# Mobile Number Validation

import re

x = input("Please share your mobile number :" )
#x = "7234567890"

#z = re.match("[0-9]{10}", x)
z = re.match("^[6-9][0-9]{9}$", x)

#print(y)
print(z)

if z:
	print("Number is valid")

else :
	raise Exception("Number yaad krlo...")
	#print("Your mobile number is not valid.")

