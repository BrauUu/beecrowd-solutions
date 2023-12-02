n = int(input())
l = list(map(int, input().split()))
for i in range(n-1):
    newL = []
    for j in range(len(l) - 1):
        ballL = l[j]
        ballR = l[j + 1]

        if ballL == ballR:
            ball = 1
            newL.append(ball)
        else:
            ball = -1
            newL.append(ball)
    l = newL

ball = l[0]

print('branca' if ball == -1 else 'preta')