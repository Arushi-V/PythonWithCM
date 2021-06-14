# Inheritance allows us to define a class that inherits all the methods and properties from another class
# Inheritance is a "is-a" relation.

class Animal :
	def __init__(self, species, motion, habitat) :
		self.species = species
		self.motion = motion
		self.habitat = habitat

	def intro(self) :
		print(f"I am {self.species}, I have {self.motion} and I live on {self.habitat}")


# Human is an Animal
class Human(Animal): 
	def __init__(self, name, gender, height) : 
		super().__init__("Homo sapiens", "2 leg motion", "land")
		self.name = name
		self.gender = gender
		self.height = height

	def intro(self) : 
		super().intro()
		print(f"My name is {self.name}, I am a {self.gender} and I am {self.height} tall.")

h1 = Human("Arushi", "Female", "5'5\"")
h1.intro()
print(h1.__dict__)
