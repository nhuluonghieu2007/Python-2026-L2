import math
print ("Enter a number")

n=int(input())
if n < 5:
    print (str(n) + " is not a perfect number")
    exit()
sum = 0
for i in range(1, n):
    if n % i == 0:
        sum += i
if sum == n:
    print (str(n) + " is a perfect number")
else:
    print (str(n) + " is not a perfect number")