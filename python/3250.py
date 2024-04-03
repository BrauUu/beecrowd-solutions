f, s, g, u, d = list(map(int, input().split()))

leftDist = g - s
count = 0
actualFloor = s
lastDirection = ''

while True:
    try:
        if actualFloor == g:
            print(count)
            break
        if (actualFloor < g and g - actualFloor >= u) or lastDirection == 'down':
            temp = abs(leftDist) // u
            dist = temp * u
            count += temp
            leftDist -= dist
            actualFloor += dist
            lastDirection = 'up'
        elif (actualFloor > g and actualFloor - g >= d) or lastDirection == 'up':
            temp = abs(leftDist) // d
            dist = temp * d
            count += temp
            leftDist += dist
            actualFloor -= dist
            lastDirection = 'down'
        else:
            raise Exception()
    except:
        print('use the stairs')
        break