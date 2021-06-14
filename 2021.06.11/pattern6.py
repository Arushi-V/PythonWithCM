# WAP to print following pattern
# for n = 5 , max row should be 5
'''
    *
   ***
  *****
   ***
    *
'''

n = int(input("Enter a number: "))
space = int(n/2)
star = 1


for i in range (1,n+1):
    for j in range (1, space+1):
        print (" ", end="")

    for j in range(1, star+1):
        print ("*", end="")

    if (i<=int(n/2)):
        space = space-1
        star = star+2
    else:
        space = space+1
        star = star-2    
    print()