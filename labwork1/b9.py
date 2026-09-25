A =input("Nhap mot so bat ky ma ban muon tinh giai thua")
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print("dap an la: ", factorial(int(A)))