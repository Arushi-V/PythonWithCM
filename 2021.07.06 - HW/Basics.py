# Basic questions : https://www.w3resource.com/python-exercises/python-basic-exercises.php

#1 Write a Python program to print the following string in a specific format

print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")
print("")

#2 Write a Python program to get the Python version you are using

import sys

print("Python Version:", sys.version)
print("")

#3 Write a Python program to display the current date and time.

import datetime
now = datetime.datetime.now()
print ("Current date and time : ", now)

#4 Write a Python program which accepts the radius of a circle from the user and compute the area

r = float(input ("Enter the radius of the circle: "))
area = 3.14*r*r 
print("Area of the circle is: ", area)

#5 Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.

fname = input("Input your First Name : ")
lname = input("Input your Last Name : ")
print (lname + " " + fname)


