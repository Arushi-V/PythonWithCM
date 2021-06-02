# Set
# its a collection of unique items
# A set is a collection which is both unordered and unindexed.

jwellerySet = {"earings", "necklace", "ring"}
print(type(jwellerySet))
print(jwellerySet)

# duplicates are not allowed in sets

print(len(jwellerySet))

# A set can contain different data types:
wallet = {100, "cheques", "photos", "dl", "card"}

# Loop through the set, and print the values:
for item in jwellerySet:
	print(item)

# add item in set
jwellerySet.add("bracelet")
print(jwellerySet)


# add sets 
wallet.update(jwellerySet)
print(wallet)

# remove items 
wallet.remove("cheques")
print(wallet)

# discard also remove items but don't raise error on item not found
wallet.discard("cheques")
print(wallet)

# union and update
# You can use the union() method that returns a new set containing all items from both sets, or the update() method that inserts all the items from one set into another
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set1)
print(set3)

#intersection_update : prints the common value of two sets.

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)