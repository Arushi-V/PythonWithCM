# WAP to find the average of numbers.

from functools import reduce

inp = map(int, input("Enter your marks of 5 subjects: ").split())
inp = list(inp)

avg = reduce(lambda x, y: (x+y) / 2, inp)
print(avg)




# 1 2 3 5 

#x = 1, y = 2, x + y / 2.0 = 1.5
#x = 1.5, y = 3, 4.5/2 = 2.25
#x = 2.25, y = 5, 7.25/2 = 3.625