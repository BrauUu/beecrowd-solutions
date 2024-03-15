while True:
    a, b, c = list(map(int, input().split()))
    if a == b == c == 0:
        break
    print(f'{int((a*b*c)**(1/3)//1)}')