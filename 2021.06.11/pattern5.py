# WAP to print following pattern
'''
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
'''

n = int(input("Enter a number: "))

for i in range (1,n+1):
    print (" " * (n-i), end="")
    print ("*" * (2 * i - 1))

for j in range (n-1,0,-1):
    print (" " * (n-j), end="")
    print ("*" * (2 * j - 1))