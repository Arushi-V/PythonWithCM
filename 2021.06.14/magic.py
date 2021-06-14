# Magic or Dunder Methods in Python
'''
Magic methods in Python are the special methods that start and end with the double underscores. 
They are also called dunder methods. Magic methods are not meant to be invoked directly by you, 
but the invocation happens internally from the class on a certain action. 
For example, when you add two numbers using the + operator, internally, the __add__() method will be called.
'''

print(dir(str))