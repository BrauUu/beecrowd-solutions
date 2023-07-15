x, y = list(map(int, input().split()))

v1 = {
    x: 0,
    y: 0
}

v2 = {
    x: 432,
    y: 468
}

if x >= 0 and x <= 432 and y >= 0 and y <= 468:
    print('dentro')
else:
    print('fora')