while True:
    n = int(input())
    
    if n == 0:
        break

    actualPos = 'C'
    movesSum = 0

    for i in range(n):
        l, c, r = input().split()
        l = int(l)
        c = int(c)
        r = int(r)

        if l == 0 and c == 1 and r == 1:
            if actualPos == 'C':
                movesSum += 1
            elif actualPos == 'R':
                movesSum += 2
            actualPos = 'L'
        elif l == 1 and c == 0 and r == 1:
            if actualPos == 'L' or actualPos == 'R':
                movesSum += 1
            actualPos = 'C'
        elif l == 1 and c == 1 and r == 0:
            if actualPos == 'C':
                movesSum += 1
            elif actualPos == 'L':
                movesSum += 2
            actualPos = 'R'

    print(movesSum)
