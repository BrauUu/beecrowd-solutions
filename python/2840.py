r, l = list(map(int, input().split()))

v = 4/3 * 3.1415 * r**3
qty = l // v

print(int(qty))