# global vs local

name = "Arushi"

def myPersonalIntro():
	name = "aru"
	print(name)	# this is printing local variable

def changeMyName():
	global name
	name = "Aru2"

myPersonalIntro() # function call
print(name) # printing global varibale

changeMyName()
print(name)