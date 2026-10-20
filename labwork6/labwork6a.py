import numpy as np
import matplotlib.pyplot as plt

# Tạo dữ liệu x trong khoảng [-5, 5]
x = np.linspace(-5, 5, 500)
y = 2 * x + (np.sin(x))**2 + 3

# Khởi tạo đồ thị
plt.figure(figsize=(8, 5))
plt.plot(x, y, label=r'$y = 2x + \sin^2(x) + 3$', color='blue', linewidth=2)

# Trang trí đồ thị theo yêu cầu đề bài
plt.title("hello, po!")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()

# Lưu kết quả ra file po.pdf
plt.savefig("po.pdf")
plt.close()
print("[+] Đã xuất đồ thị ra file po.pdf")
