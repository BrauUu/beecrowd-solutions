import math

a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)

delta = (b * b) - 4 * a * c 

try :
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print(f'R1 = {x1:.5f}')
    print(f'R2 = {x2:.5f}')
except :
    print('Impossivel calcular')