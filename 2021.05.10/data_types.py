# Datatypes

"""
@ Built-in Data Types

Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
"""

# getting a data type

# int
x = 5
print(type(x))

# float
x = 5.2
print(type(x))

# complex
x = 1j
print(type(x))

# list 
x = ["apple", "banana", "cherry"]
print(type(x))

# tuple
x = ("apple", "banana", "cherry")
print(type(x))

# range
x = range(6)
print(type(x))

# dict
x = {"name" : "John", "age" : 36}
print(type(x))

# set
x = {"apple", "banana", "cherry"}
print(type(x))

# frozenset
x = frozenset({"apple", "banana", "cherry"})
print(type(x))

# bool
x = True
print(type(x))

# bytes
x = b"Hello"
print(x)
print(type(x))

# bytearray
x = bytearray(5)
print(x)
print(type(x))

# memoryview
x = memoryview(bytes(5))
print(x)
print(type(x))