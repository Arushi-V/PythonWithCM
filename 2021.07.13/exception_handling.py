# Python Try Except

''' The try block lets you test a block of code for errors.
    The except block lets you handle the error.
    The finally block lets you execute code, regardless of the result of the try- and except blocks.'''

# Exception Handling
''' When an error occurs, or exception as we call it, Python will normally stop and generate an error message.
    These exceptions can be handled using the try statement:'''

# The try block will generate an exception, because x is not defined:

try:
  print(x)
except:
  print("An exception occurred")
print("")  


# Many Exceptions
# You can define as many exception blocks as you want, e.g. if you want to execute a special block of code for a special kind of error:


# Q - Print one message if the try block raises a NameError and another for other errors:

try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")  
print("")  


# Else : You can use the else keyword to define a block of code to be executed if no errors were raised:

# In this example, the try block does not generate any error:

try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
print("")  


# Finally : The finally block, if specified, will be executed regardless if the try block raises an error or not.

try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")
print("")  


