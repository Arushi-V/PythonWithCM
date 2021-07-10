# WAP to create BMI Calculator

weight = float(input("Enter your weight(in kg) : "))
height = input("Enter your height in feet (For example - if your height is 5 feet 5 inches, enter 5.5): ")

h1 = height.split(".",2)
print(h1)
		


height_inches = int(h1[0]) * 12 + (int(h1[1]) if len(h1)>1 else 0)
height_cm = height_inches * 2.54
height_m = height_cm / 100

print(height_m)

bmi = weight / (height_m **2)

print("You BMI is :", bmi)

if (bmi <= 18.5) :
	print("You need to have a pizza party")

elif (bmi >= 18.5 and bmi <= 24.9) :
	print("tusi change ho ji")	

elif (bmi >= 24.9 and bmi <= 29.9) :
	print("Control krlo")

else :
	print("Aap doctor se milo")		
