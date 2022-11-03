from math import log

n = int(input())

min = n/ log(n)
max = (n/ log(n)) * 1.25506

print(f'{min:.1f} {max:.1f}')