t = int(input())

for i in range(t):
    n, c, m = list(map(int, input().split()))
    floors = list(map(int, input().split()))
    floors.sort(reverse=True)
    sum = 0
    for g in range(0, m, c):
        sum += 2 * floors[g]
    print(sum)