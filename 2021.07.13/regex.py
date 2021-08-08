# Python Regex

''' A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
  RegEx can be used to check if a string contains the specified search pattern.
  Python has a built-in package called re, which can be used to work with Regular Expressions.

Import the re module:'''


# Example : Search the string to see if it starts with "The" and ends with "Spain"
import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")


# RegEx Functions

'''The re module offers a set of functions that allows us to search a string for a match:
   1) findall : Returns a list containing all matches
   2) search : Returns a Match object if there is a match anywhere in the string
   3) split : Returns a list where the string has been split at each match
   4) sub : Replaces one or many matches with a string
'''

# The findall() Function
# The findall() function returns a list containing all matches.
# Print a list of all matches:

import re

txt = "Regular Expressions in python programming language"
y = re.findall("s", txt)
print(y)

# The search() Function
# The search() function searches the string for a match, and returns a Match object if there is a match.

x = re.search("\s", txt)
print("The first white-space character is located in position:", x.start())

# The split() Function
# The split() function returns a list where the string has been split at each match:

z = re.split("\s", txt)
print(z)

# The sub() Function
# The sub() function replaces the matches with the text of your choice:

a = re.sub("\s", "_", txt)
print(a)

b = re.sub("\s", "_", txt, 2)   # controlling number of replacements using count
print(b)