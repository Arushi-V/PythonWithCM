n = int(input("Enter array length"))
arr = list(map(int, input("Enter your array").split()))
arr.sort()
print(arr[n-2])

