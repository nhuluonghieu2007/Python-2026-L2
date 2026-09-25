import math
print ("Enter a number")

n=float(input())
if n <= 1:
    print (str(n) + " is not a prime number")
    exit()
x = int(math.sqrt(n))
for i in range(2,x + 1):
    if n % i == 0:
        print (str(n) + " is not a prime number")
        exit()
print (str(n) + " is a prime number")