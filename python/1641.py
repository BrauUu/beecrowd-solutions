count = 1
while True:
    x = input().split()
    if x[0] == '0':
        break
    r, w, l = list(map(int, x))
    r *= 2
    h = (w ** 2 + l ** 2) ** (1/2)
    print(f'Pizza {count} fits on the table.' if h <= r else f'Pizza {count} does not fit on the table.')
    count += 1