from abc import ABC, abstractmethod

class Animal(ABC):

	@abstractmethod
	def charateristic(self):
		pass

class Dog(Animal):
	def charateristic(self):
		print("I can bark")


d = Dog()
d.charateristic()

class Human(Animal):
	def charateristic(self):
		print("I can walk and talk")


h = Human()
h.charateristic()