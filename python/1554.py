n = int(input())
for _ in range(n):
    numBalls = int(input())
    whiteBall = list(map(int, input().split()))
    smallerDistance = 0
    nearestBall = 0
    for i in range(numBalls):
        x, y = list(map(int, input().split()))
        distance = (abs(x-whiteBall[0])**2+abs(y-whiteBall[1])**2)**1/2
        if i == 0:
            smallerDistance = distance
            nearestBall = i+1
            continue
        if distance < smallerDistance:
            smallerDistance = distance
            nearestBall = i + 1
    print(nearestBall)