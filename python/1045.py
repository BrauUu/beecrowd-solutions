x = input().split()
x = [float(x[0]), float(x[1]), float(x[2])]
x.sort()

a = x[2]
b = x[1]
c = x[0]

if a >= (b+c):
    print('NAO FORMA TRIANGULO')
else:
    if a * a == b * b + c * c:
        print('TRIANGULO RETANGULO')
    if a * a > b * b + c * c:
        print('TRIANGULO OBTUSANGULO')
    if a * a < b * b + c * c:
        print('TRIANGULO ACUTANGULO')
    if a == c and c == b:
        print('TRIANGULO EQUILATERO')
    if (a == c and b != a) or (a == b and a != c) or (b == c and b != a):
        print('TRIANGULO ISOSCELES')