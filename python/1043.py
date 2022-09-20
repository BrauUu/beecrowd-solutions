a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)

perimeter = a + b + c
area = ((a + b) * c) / 2

if a + b > c and b + c > a and a + c > b:
    print(f'Perimetro = {perimeter:.1f}')
else:
    print(f'Area = {area:.1f}')
