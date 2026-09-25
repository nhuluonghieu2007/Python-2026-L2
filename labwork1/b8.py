I=[int(x) for x in input("Nhap day so bat ky: ").split(",")]
#day so cach nhau bang dau phay

def extract_even(I):
    even_numbers = []
    for num in I:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers

print("Cac so chan trong day so la:", extract_even(I))

