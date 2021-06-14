nm = input().split()

n = int(nm[0])

m = int(nm[1])

arr = []

for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))

k = int(input())

arr.sort(key = lambda a : a[k])

for x in arr:
    #print(x[0],x[1],x[2])
    for a in x:
        print(a, end=" ")
    print()