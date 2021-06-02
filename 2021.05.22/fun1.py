  
# A function is a block of organized, reusable code that is used to perform a single, related action.
# which returns a value or does not return a value.

def sayHello(fname = "Arushi", lname = "Vohra"): # function with a default param
	print(f'Hello {fname} {lname}, I am pyhton...nice to meet you...')


sayHello() 
sayHello("CM","Pundhir") # positional argument
sayHello(lname = "Pundhir", fname = "CM") # named arguments



# variable argument
def sayHelloAll(*names):
	for name in names:
		print(f'Hello {name}, I am pyhton...nice to meet you...')


sayHelloAll()
sayHelloAll("Arushi", "Shankar", "CM")



# keyword arguments function where kwargs is a dictionary
def sayHelloByK(**names):
	print(f'Hello {names["fname"]} {names["lname"]}, I am pyhton...nice to meet you...')


sayHelloByK(fname = "Arushi", lname = "Vohra")


def allTypeParamEx(name, *friends, **addr):
	print(f'Hello {name}')
	print("Dosto : ", end="")
	for frnd in friends:
		print(frnd, end=", ")
	print()
	print(f'HNo: {addr["h_no"]}, street: {addr["street"]}, state: {addr["state"]}')


allTypeParamEx("Arushi", "Sanya", "Vanshika", h_no="1", street="My Street", state="Himachal")
allTypeParamEx("Arushi", "Sanya", "Vanshika", h_no="1", street="My Street", state="Himachal")
