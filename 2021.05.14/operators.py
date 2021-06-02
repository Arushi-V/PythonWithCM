# operators
# Operators are used to perform operations on variables and values.

# using + operator
print(10 + 5)

'''
@Tyes of OPerator

1. Arithmetic operators
2. Assignment operators
3. Comparison operators
4. Logical operators
5. Identity operators
6. Membership operators
7. Bitwise operators
'''

print("-------********--------")
print("Arithmetic Operators")
# Arithmetic
print(10 + 5)
print(10 - 5)
print(10 * 5)
print(10 / 5)
print(10 // 5)
print(10 % 5)
print(2 ** 2)

print("-------********--------")
print("Assignment Operators")
# Assignment operators


print("-------********--------")
print("Comparison Operators")
# Comparision Operators


print("-------********--------")
print("Logical Operators")
# Logical Operators
print(1>2 and 1>3)
print(1>2 or 1>3)
print(not 1>3)


print("-------********--------")
print("Indentity Operators")
#Identity Operators
a = 6
b = 5
x = a
print(b is a)
print(x is a)
print(a is not x)


print("-------********--------")
print("Membership Operators")
# Membership Operators
print("Aru" in "Arushi")
print(1 in range(1,10))
print("Apple" in ["Banana", "Apple", "Kiwi"])
print("Orange" not in ["Banana", "Apple", "Kiwi"])



print("-------********--------")
print("Bitwise Operators")
# Bitwise Operators
a = 10
b = 4
print(bin(a)) 
print(bin(b)) 
print(a & b, bin(a & b)) 
print(a | b, bin(a | b)) 
print(~a, bin(~a))
print(a<<3, bin(a<<3))
print(a>>3, bin(a>>3))
print(b>>3, bin(b>>3))
x = -23
print(x>>2, bin(x>>2))
