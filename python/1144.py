x = int(input())

for i in range(1, x + 1):
    print(f'{i} {pow(i, 2)} {i * pow(i, 2)}')
    print(f'{i} {pow(i, 2) + 1} {i * pow(i, 2) + 1}')