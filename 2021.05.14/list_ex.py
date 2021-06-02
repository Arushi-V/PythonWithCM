# List
# Lists are used to store multiple items in a single variable.
# Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

# @Features of a list
# lists are ordered
# The list is changeable, meaning that we can change, add, and remove items in a list
# Since lists are indexed, lists can have items with the same value

fruits = ["Apple", "Mango", "Banana"]
print(fruits)
print(type(fruits))
print("At Index 1: ",fruits[1])

# we can create different list with different data types
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

# a list can have different type of data as well
list3 = ["abc", 34, True, 40, "male"]
print(list3)

# list constructor
tp = ("apple", "banana", "cherry") # tuple
print(type(tp),"=>",tp)

fruits = list(tp) # using list constructor to create a list
print(type(fruits),"=>",fruits)

