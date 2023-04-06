
n = int(input())

for i in range(n):
    qt, s = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    
    winner = 0
    smallerDiff = 0
    
    for i in range(qt):
        diff = abs(s - arr[i])
        if i == 0:
            smallerDiff = diff
            winner = i + 1
        if diff == 0:
            winner = i + 1
            break
        elif diff < smallerDiff:
            winner = i + 1
            smallerDiff = diff
    
    print(winner)