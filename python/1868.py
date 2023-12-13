def showMatrix(matrix):
    matrixLen = len(matrix)
    res = ''
    for i in range(matrixLen):
        line = ''
        for g in range(matrixLen):
            line += str(matrix[i][g])
        res += f'{line}\n'
    return res[:-1]

while True:
    n = int(input())
    if n == 0:
        break
    matrix = [['O' for _ in range(n)] for _ in range(n)]
    half = n//2
    matrix[half][half] = 'X'
    y = 0
    xActualPos = {
        'x': half,
        'y': half,
    }
    
    print(showMatrix(matrix))
    print('@')
    for i in range(half):
        y+=1
        for g in range(y):
            matrix[xActualPos['y']][xActualPos['x']] = 'O'
            xActualPos['x'] += 1
            matrix[xActualPos['y']][xActualPos['x']] = 'X'
            print(showMatrix(matrix))
            print('@')
        for g in range(y):    
            matrix[xActualPos['y']][xActualPos['x']] = 'O'
            xActualPos['y'] -= 1
            matrix[xActualPos['y']][xActualPos['x']] = 'X'
            print(showMatrix(matrix))
            print('@')
        y += 1
        for g in range(y):   
            matrix[xActualPos['y']][xActualPos['x']] = 'O'
            xActualPos['x'] -= 1
            matrix[xActualPos['y']][xActualPos['x']] = 'X'
            print(showMatrix(matrix))
            print('@')
        for g in range(y):   
            matrix[xActualPos['y']][xActualPos['x']] = 'O'
            xActualPos['y'] += 1
            matrix[xActualPos['y']][xActualPos['x']] = 'X'
            print(showMatrix(matrix))
            print('@')
            
    for g in range(y):
        matrix[xActualPos['y']][xActualPos['x']] = 'O'
        xActualPos['x'] += 1
        matrix[xActualPos['y']][xActualPos['x']] = 'X'
        print(showMatrix(matrix))
        print('@')       