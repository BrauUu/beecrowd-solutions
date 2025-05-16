t = int(input())

d = {
    0 : 1,
    1 : 7,
    2 : 9,
    3 : 3
}

for _ in range(t):
    n = int(input())
    print(d[n%4])