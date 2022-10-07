t = int(input())
i = 0

while i < 1000:
    for j in range(t):
        print(f'N[{i}] = {j}')
        i += 1
        if i >= 1000:
            break