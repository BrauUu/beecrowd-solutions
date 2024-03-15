from math import tan, radians

while True:
        try:
            a, b, c = list(map(float, input().split()))
            a = tan(radians(a))
            res = (a * b + c) * 5
            print(f'{res:.2f}')
        except:
            break