f1, f2 = list(map(float, input().split()))

s = ((1 + f1/100) * (1 + f2/100) - 1) * 100

print(f'{s:.6f}')