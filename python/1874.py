while True:
    h, p, f = list(map(int, input().split()))
    if h == p == f == 0:
        break
    matrix = []
    for i in range(h):
        line = list(map(int, input().split()))
        matrix.append(line)
        
    itens = list(map(int, input().split()))
    itens.reverse()
    flag = False
    
    for i in range(p - 1, -1 ,-1):
        for g in range(h - 1, -1, -1):
            if matrix[g][i] == 0:
                item = itens.pop()
                matrix[g][i] = item
                if len(itens) == 0:
                    flag = True
                    break
        if flag == True:
            break      
                    
    for line in matrix:
        print(*line)
        