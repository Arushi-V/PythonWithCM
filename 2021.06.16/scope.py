# Local and global variables scope

# Local Scope
# A variable created inside a function belongs to the local scope of that function, and can only be used inside that function

def func():
	x = 20
	print(x)

func()	

# Function Inside Function
# As explained in the example above, the variable x is not available outside the function,
# but it is available for any function inside the function:

def new():
	x = 45
	def inner():
		print(x)

	inner()


new()

# Global Scope
# A variable created in the main body of the Python code is a global variable and belongs to the global scope.
# Global variables are available from within any scope, global and local.

x = 50

def glob():
	global x     # use the global keyword if you want to make a change to a global variable inside a function.
	x = 33
	print(x)


glob()
print(x)