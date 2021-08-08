
arr = list(map(int, [2,3,6,6,5]))
arr.sort()
largestNum = -999999999999999999999999
secLargestNum = largestNum
for x in arr:
	if largestNum<x:
		secLargestNum, largestNum = largestNum, x

print(secLargestNum)
