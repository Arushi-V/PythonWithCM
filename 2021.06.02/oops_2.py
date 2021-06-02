# Polymorphism
# Poly + Morphism
# Poly : many, Morphism : forms
# means having many forms

# example : i need to go from Delhi to Kerala
#          option: 1. by walk
#		   option: 2. by car
#		   option: 3. by train
#		   option: 4. by air
#			
#		   ultimate goal:  To reach Kerala


# Example of inbuilt polymorphic functions :
print(len([1,322,33,4,3,45,5]))
print(len("Arushi"))



# exmample of a function with polymorphism
def addition(a, b, c = 0):
	return a + b + c

print(addition(10, 5))
print(addition(10, 5, 7))


# with class example
class Calculation:
	def add(self, a, b, c = 0):
		return a + b + c


cal = Calculation()
res = cal.add(10, 2)
print(res)

res = cal.add(10, 2, 4)
print(res)