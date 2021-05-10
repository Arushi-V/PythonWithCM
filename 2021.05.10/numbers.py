# Numbers
"""
@types

1. int
2. float
3. complex
"""

x = 1    # int
y = 2.8  # float
z = 1j   # complex

print(x)
print(y)
print(z)

# Random Number
"""
-> Python does not have a random() function to make a random number, 
-> but Python has a built-in module called random that can be used to make random numbers:
"""
# before using random we need to imprt it because its a modul
import random # it is recommended to put imports on top of file/module

x = random.randrange(1, 10)
print(x)
