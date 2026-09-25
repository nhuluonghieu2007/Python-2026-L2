A =input("Hay nhap mot so bat ky:")

def divisors_of_number(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors
#cơ chế hoạt động:
#từ số A code sẽ tìm ra các ước số của nó bằng cách lặp từ 1 đến A và kiểm tra xem A có chia hết cho i hay không.
# Nếu chia hết, i sẽ được thêm vào danh sách các ước số.

print("Cac uoc cua so", A, "la:", divisors_of_number(int(A)))