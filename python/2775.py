while True:
    try:
        n = int(input())
        idArr = input().split()
        moveArr = input().split()
        count = 0
        count2 = 0
        
        for g in range(n):
            flag = False
            count2 += 1
            for i in range(n - 1):
                x = int(idArr[i])
                y = int(idArr[i+1])
                if x > y:
                    idArr[i+1] = x
                    idArr[i] = y 
                    flag = True
                    count += int(moveArr[i]) + int(moveArr[i+1])
                    
                    temp = moveArr[i+1]
                    moveArr[i+1] = moveArr[i]
                    moveArr[i] = temp
                    
                      
                else:
                    if flag == False:
                        continue
                    break
        
        print(count)
        print(count2)
    except:
        break