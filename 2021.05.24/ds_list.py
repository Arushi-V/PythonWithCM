# Data structure
# A data structure is a particular way of organizing data in a computer so that it can be used effectively

# Data structures in Python
# 1. List
# 2. Tuple
# 3. Set
# 4. Dictionary

# lets do something great with list
countries = ["India", "Pakistan", "USA", "UK"]
print(countries)

print(countries[1])
print(countries[1:3])
print(countries[:3])
print(countries[:])
print(countries[2:])


# len of a list
print("length =>", len(countries))


# list allow duplicate elements
furits = ["Apple", "Banana", "Oranges", "Apple"]
print(furits)

# check type
print(type(countries))

# change item in list
countries[1] = "Nepal"
print(countries)

countries.insert(2, "Pakistan")
print(countries)

# add item in list
countries.append("Spain")
print(countries)

# extend list
countries.extend(furits)
print(countries)

# list comprehension
onlyCountries = [x for x in countries if x not in furits]
print(onlyCountries)

# sorting
onlyCountries.sort()
print(onlyCountries)

# onlyCountries.sort(lambda x : true if "u" in x else false)