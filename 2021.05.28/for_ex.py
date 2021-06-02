# for loop
# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

for x in range(10):
	print(x)

r = range(10)
print(type(r))


fruits = ["Apple", "Banana", "Oranges"]
for x in fruits:
	print(x)


# we can use else with a for loop
for x in fruits:
	print(x, end=", ")
else:
	print("\nloop ended")