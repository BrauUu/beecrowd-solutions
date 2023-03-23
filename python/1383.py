n = int(input())

for i in range(n):
    flag = False
    
    colsMatrix = [[],[],[],[],[],[],[],[],[]]
    
    for g in range(9):
        lineArr = []
        line = input().split()
        if flag == False:
            for j in range(len(line)):
                item = line[j]
                try:
                    lineArr.index(item)
                    flag = True
                except:
                    lineArr.append(item)
                    try:
                        colsMatrix[j].index(item)
                        flag = True
                    except:
                        colsMatrix[j].append(item)                                                         
    
    print(f'Instancia {i+1}')
                     
    if flag == True:
        print("NAO\n")
    else:
        print("SIM\n")
        
    print()