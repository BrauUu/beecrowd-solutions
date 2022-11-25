while True:
    try:
        dY, dX = input().split()
        dY = int(dY)
        dX = int(dX)
        
        board = []
        
        for i in range(dY):
            line = input().split()
            board.append(line)
        
        
        for i in range(dY):
            line = []
            count = 0
            for j in range(dX):
                count = 0
                if board[i][j] == '1':
                    line.append(9)
                else:
                    if j != dX - 1 and board[i][j+1] == '1':
                        count += 1
                    if j != 0 and board[i][j-1] == '1':
                        count += 1  
                    if i != dY - 1 and board[i+1][j] == '1':
                        count += 1
                    if i != 0 and board[i-1][j] == '1':
                        count += 1
                    
                    line.append(count)
            
            values = ''
            
            for value in line:
               values += str(value)
                            
            print(values)
    except:
        break