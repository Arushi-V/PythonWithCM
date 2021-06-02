# dictionary
# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and does not allow duplicates.
# Dictionaries are written with curly brackets, and have keys and values

myLife = {"Name": "Arushi", "Qualification": "Engineer", "BankBalance": 10000000000, "Vehicle": "camry", "hobbies":["singing", "drawing"], "IsAirplane": False}
print(type(myLife))
print(myLife)
print(myLife["Name"])
print(len(myLife["hobbies"]))
print(myLife["hobbies"][1])
print(myLife["IsAirplane"])

# get()

x = myLife.get("Qualification")
print(x)

# keys()

x = myLife.keys()
print(x)
print(type(x))

for keys in x:
	print(keys)

# values() : to get all the values

y = myLife.values()
print(y)

# change values

myLife["BankBalance"] = myLife["BankBalance"] + 1

print(myLife["BankBalance"])


hobbies = myLife["hobbies"]
hobbies.append("yoga")

print(hobbies)