n1, d1, v1 = list(map(int, input().split()))
n2, d2, v2 = list(map(int, input().split()))

print(n1 if d1 / v1 < d2 / v2 else n2)