def rec(r, n, d):
    s = n + n * d
    if d > 26:
        return 'impossible'
    elif s >= r:
        return d
    else:
        return rec(r, n, d + 1)

i = 1
while True:
    r, n = list(map(int, input().split()))
    if r == n == 0:
        break
    d = rec(r, n, 0)
    print(f'Case {i}: {d}')
    i += 1