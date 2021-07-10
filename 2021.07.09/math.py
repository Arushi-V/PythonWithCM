# Python Math 
# Built-in Math Functions
# The min() and max() functions can be used to find the lowest or highest value in an iterable.

x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)

# The abs() function returns the absolute (positive) value of the specified number:

a = abs(-7.00)
print(a)

# The pow(x, y) function returns the value of x to the power of y (xy).

b = pow(4, 3)
print(b)


# The Math Module
# Python has also a built-in module called math, which extends the list of mathematical functions.
# When you have imported the math module, you can start using methods and constants of the module.

# 1) The math.sqrt() method for example, returns the square root of a number:

import math

m = math.sqrt(64)

print(m)

# 2) The math.ceil() method rounds a number upwards to its nearest integer, and the 
#  math.floor() method rounds a number downwards to its nearest integer, and returns the result:

i = math.ceil(1.4)
j = math.floor(1.4)

print(i) # returns 2
print(j) # returns 1

# 3) The math.pi constant, returns the value of PI (3.14...):

p = math.pi

print(p)

