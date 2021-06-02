
''' x = int(input("Please enter an integer: "))

if x < 0:
     print('Negative changed to zero')
elif x == 0:
     print('Zero')
elif x == 1:
     print('Single')n
else:
     print('More')'''


# For Statement
# Measure some strings:

words = ['cat', 'window', 'defenestrate']
for w in words:
     print(w, len(w), end=",")

# For range() Function

for i in range(5):
	print(i)
for i in range(5,10,1):
	print(i,end=",")
print("")
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
     print(i, a[i])
