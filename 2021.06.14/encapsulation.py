# Encapsulation in Python
'''
Encapsulation is one of the fundamental concepts in object-oriented programming (OOP). 
It describes the idea of wrapping data and the methods that work on data within one unit. 
This puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data. 
To prevent accidental change, an object’s variable can only be changed by an object’s method. 
Those types of variables are known as private variable. 
A class is an example of encapsulation as it encapsulates all the data that is member functions, variables, etc.
'''

# Protected members
'''
Protected members (in C++ and JAVA) are those members of the class that cannot be accessed outside the class but can be 
accessed from within the class and its subclasses. 
To accomplish this in Python, just follow the convention by prefixing the name of the member by a single underscore “_”.
Note: The __init__ method is a constructor and runs as soon as an object of a class is instantiated. 
'''


# Python program to
# demonstrate protected members
 
 
# Creating a base class
class Base:
    def __init__(self):
         
        # Protected member
        self._a = 2
 
# Creating a derived class   
class Derived(Base):
    def __init__(self):
         
        # Calling constructor of
        # Base class
        Base.__init__(self)
        print("Calling protected member of base class: ")
        print(self._a)
 
obj1 = Derived()
         
obj2 = Base()
 
# Calling protected member
# Outside class will  result in
# AttributeError
 # print(obj2.a)


# Private members
'''
Private members are similar to protected members, the difference is that the class members declared private should neither be 
accessed outside the class nor by any base class. In Python, there is no existence of Private instance variables that cannot 
be accessed except inside a class. 
However, to define a private member prefix the member name with double underscore “__”.
'''

print(dir(Derived))