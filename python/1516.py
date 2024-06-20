while True:
    n, m = list(map(int, input().split()))
    if n == m == 0:
        break
    draw = []
    for _ in range(n):
        draw.append(input())
    a, b = list(map(int, input().split()))
    lineMultiplier = a // n
    charMultiplier = b // m
    newDraw = []
    for line in draw:
        newLine = ''
        for char in line:
            newLine += char * charMultiplier
        
        newDraw.append(((newLine + '\n') * lineMultiplier)[:-1])
    
    print(*newDraw, sep='\n')
    print()
