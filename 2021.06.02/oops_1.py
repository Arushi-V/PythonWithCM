# OOPs : Object oriented programming
# Concept 
# 1. Class
# 2. Object
# 3. Mehtod
# 4. Polymorphism
# 5. Inheritance
# 6. Encapsulation
# 7. Abstraction

# class
# Q. What ia a class?
# Ans. 1. Class is a collection of objects.
#      2. Class is a logical entity.
#      3. Class a blueprint of an Object.

# Python is an object oriented programming language.
# Almost everything in Python is an object, with its properties and methods.

# To create a class, use the keyword class:
class Animal:
	hobbis = "Ghoomna pasand hai."
	def __init__(self, noOLegs, speed, sound):
		self.noOLegs = noOLegs
		self.speed = speed
		self.sound = sound

	def intro(self):
		print(self.sound)


# Object
# Q. What is an Object?
# Ans. Object is an instance of a class.
# 	   Every Object has 3 key things in it
#          1. It can have varibales
#		   2. it can have methods
#		   3. Identity 

# object of Animal
tomy = Animal(4, 50, "bhoonk...")
print(tomy)
print("No of legs: ", tomy.noOLegs)
print("Speed: ", tomy.speed)
print("Sound: ", tomy.sound)
print(tomy.__dict__)


# method in class
# each method contains a self param as a reference of current object
tomy.intro() 


# let's take another example of class and object
class Human:
	pass


arushi = Human()
arushi.name = "Arushi Vohra"
arushi.followers = 100000
print(arushi.name)
print(arushi.followers)
print(arushi.__dict__)


print(Animal.hobbis)

fish = Animal("3", "10", "mann ki baate")
fish.intro()
print(fish.hobbis)
fish.hobbis = "Swimming..."
print(fish.hobbis)
print(Animal.hobbis)
