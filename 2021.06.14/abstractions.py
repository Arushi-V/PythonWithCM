# Abstract Classes in Python
# An abstract class can be considered as a blueprint for other classes. 
# It allows you to create a set of methods that must be created within any child classes built from the abstract class. 
# A class which contains one or more abstract methods is called an abstract class. 
# An abstract method is a method that has a declaration but does not have an implementation. 
# While we are designing large functional units we use an abstract class. 
# When we want to provide a common interface for different implementations of a component, we use an abstract class.
# By defining an abstract base class, you can define a common Application Program Interface(API) for a set of subclasses.



# How Abstract Base classes work : 
# By default, Python does not provide abstract classes. 
# Python comes with a module that provides the base for defining Abstract Base classes(ABC) and that module name is ABC 

from abc import ABC, abstractmethod

class Polygon(ABC):

	@abstractmethod
	def noofSides(self):
		pass


class Triangle(Polygon):
	
	def noofSides(self):
		return 3


class Quad(Polygon):
	
	def noofSides(self):
		return 4


t = Triangle()
print("Sides in a Triangle: ", t.noofSides())

q = Quad()
print("Sides in a Quad: ", q.noofSides())
