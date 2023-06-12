SIDES = ['N', 'L', 'S', 'O']

while True:
    n, m, s = list(map(int, input().split()))
    
    if n == m == s == 0:
        break
    
    arenaMap = []
    count = 0
    actualPos = {}
    actualDirection = '' 
    
    for i in range(n):
        arenaMap.append([])
        line = input()
        for g in range(len(line)):
            cel = line[g]
            if SIDES.count(cel) > 0:
                
                actualPos = {
                    'x': g,
                    'y': i
                }
                
                actualDirection = cel
                
            arenaMap[i].append(cel)
    
    instructions = input()
    
    for i in range(len(instructions)):
        instruction = instructions[i]
        
        directionIndex = SIDES.index(actualDirection)
        if instruction == 'D':
            actualDirection = SIDES[directionIndex + 1 if directionIndex <= 2 else 0]
        elif instruction == 'E':
            actualDirection = SIDES[directionIndex - 1 if directionIndex >= 1 else 3]
        elif instruction == 'F':
            if actualDirection == 'N' and actualPos['y'] != 0 and arenaMap[actualPos['y'] - 1][actualPos['x']] != '#':
                actualPos['y'] -= 1
            elif actualDirection == 'S' and actualPos['y'] != n - 1 and arenaMap[actualPos['y'] + 1][actualPos['x']] != '#':
                actualPos['y'] += 1
            elif actualDirection == 'L' and actualPos['x'] != m - 1 and arenaMap[actualPos['y']][actualPos['x'] + 1] != '#':
                actualPos['x'] += 1
            elif actualDirection == 'O' and actualPos['x'] != 0 and arenaMap[actualPos['y']][actualPos['x'] - 1] != '#':
                actualPos['x'] -= 1
                
        if arenaMap[actualPos['y']][actualPos['x']] == '*':
            count += 1
            arenaMap[actualPos['y']][actualPos['x']] = '.'
     
    print(count)