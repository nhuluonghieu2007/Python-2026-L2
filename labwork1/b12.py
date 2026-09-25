m, n = map(int, input().split()) 
print("*" * m)
for i in range(n - 2):
    print("*" + " " * (m - 2) + "*")
print("*" * m)
