n = int(input())

for i in range(n):
    flag = False
    colsMatrix = [[] for _ in range(9)]
    sectionMatrix = [[] for _ in range(9)]
    
    for g in range(9):
        lineArr = []
        line = input().split()
        if flag == False:
            for j in range(len(line)):
                item = line[j]
                try:
                    lineArr.index(item)
                    flag = True
                    break
                except:
                    lineArr.append(item)
                    try:
                        colsMatrix[j].index(item)
                        flag = True
                        break
                    except:
                        colsMatrix[j].append(item)
                        ind = -1
                        try:
                            if j <= 2 and g <= 2:
                                ind = 0
                            elif j <= 5 and g <= 2:
                                ind = 1
                            elif j <= 8 and g <= 2:
                                ind = 2
                            elif j <= 2 and g <= 5:
                                ind = 3
                            elif j <= 5 and g <= 5:
                                ind = 4
                            elif j <= 8 and g <= 5:
                                ind = 5
                            elif j <= 2 and g <= 8:
                                ind = 6
                            elif j <= 5 and g <= 8:
                                ind = 7
                            elif j <= 8 and g <= 8:
                                ind = 8
                            sectionMatrix[ind].index(item)
                            flag = True
                            break
                        except:
                            sectionMatrix[ind].append(item)                                                  
        
    print(f'Instancia {i+1}')
                     
    if flag == True:
        print("NAO")
    else:
        print("SIM")
        
    print()