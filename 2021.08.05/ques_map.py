# return cube of array using map function.

inp = input("Enter array: ")
print("type of inp: ",type(inp), inp)

inp = inp.split()
print("type of inp: ",type(inp), inp)

inp_2 = []
for x in inp:
	inp_2.append(int(x))

print("type of inp_2: ",type(inp_2), inp_2)


inp_3 = map(int, input("Enter array: ").split())
print("type of inp_3: ",type(inp_3), inp_3)

result = list(inp_3)

result = map(lambda x : x**3, result)

result = list(result)

print("Cube root :", result)