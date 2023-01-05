n = int(input())

for i in range(n):
    jSum = 0
    mSum = 0
    for j in range(3):
        x, d = input().split()
        jSum += int(x) * int(d)
    for j in range(3):
        x, d = input().split()
        mSum += int(x) * int(d)
    print("MARIA" if mSum > jSum else "JOAO")