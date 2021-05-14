# string is a sequence of characters
name = "arushi vohra"
print(name[3]) # we can access characters via there index

# we can loop through a string
for x in name:
	print(x, end=", ")

print()
# to calculate length of a sequence we have len() function
print("length=>", len(name))

message = "kuchh bhi chalega... thik hai"
if "thik" in message:
	print("All OK")
else:
	print("Something is wrong")

secretMessage = "we are going to have a party tonight"
if "party" not in secretMessage:
	print("All OK")
else:
	print("Something is wrong")


# slicing -> with help of [_:_]
print(name[2:5])
print(name[2:])
print(name[:6])
print(name[-5:])
print(name[-7:-4])
print(name[-1:])


# string methods
print(name.lower())
print(name.upper())
print(name.split(" "))