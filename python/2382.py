*v, r = list(map(int, input().split()))

v.sort(reverse=True)

d = r * 2
p = (v[0] ** 2 + v[1] ** 2) ** (1/2)
r = d - p
print('S' if r >= 0 else 'N')