# Class :
# Class is a collection of objects, it is a blueprint of objects.

class Animal:
	def __init__ (self, noOfLegs, sound):
		self.noOfLegs = noOfLegs
		self.sound = sound

	def intro(self, species):
		print("I am ",species, "I have",self.noOfLegs , " legs and I can",self.sound)

a = Animal(4, "bark")
a.intro("HomoSapiens")

class Human(Animal):
	def __init__(self, color):
		super().__init__(2, "speak")
		self.color = color

	def intro(self):
		super().intro("Insan")
		print(self.color)


h = Human("white")
h.intro()
h.greed = "extreme"
print(h.__dict__)

# Abstraction

from abc import ABC, abstractmethod
class Polygon(ABC):
	@abstractmethod 
	def NoOfSides(self):
	 pass

class Triangle(Polygon):
	def NoOfSides(self):
		return 3

t = Triangle()		 
print(t.NoOfSides())




