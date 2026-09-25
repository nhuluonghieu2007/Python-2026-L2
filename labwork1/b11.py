A=input("Nhap toa do diem A:")
B=input("Nhap toa do diem B:")
A=A.split(",")
B=B.split(",")
def distance(A,B):
    x1=int(A[0])
    y1=int(A[1])
    x2=int(B[0])
    y2=int(B[1])
    d=((x2-x1)**2+(y2-y1)**2)**0.5
    return d

print("Khoang cach giua hai diem A va B la:", distance(A, B))