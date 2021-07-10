# Python Datetime
# A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects.

import datetime

x = datetime.datetime.now()
print(x)


# to print year an d weekday

print(x.year)
print(x.strftime("%A"))

# The strftime() Method
# The datetime object has a method for formatting date objects into readable strings.
# The method is called strftime(), and takes one parameter, format, to specify the format of the returned string.

y = datetime.datetime(2018, 6, 1)

print(y.strftime("%B"))