# WAP to print following pattern
'''
    *
   ***
  *****
 *******
*********
'''

n = int(input("Enter a number: "))

for i in range (1,n+1):
    print (" " * (n-i), end="")
    print ("*" * (2 * i - 1))

'''
1 = 1 = 2 * 1 - 1 
2 = 3 = 2 * 2 - 1 
3 = 5 = 2 * 3 - 1 
4 = 7 = 2 * 4 - 1 
5 = 9 = 2 * 5 - 1 
.
.
.
'''