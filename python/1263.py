while True:
    try:
        wordsArr = input().split()
        if len(wordsArr) < 1:
            break
        flag = False
        count = 0
        for i in range(len(wordsArr) - 1):
            actualItem = wordsArr[i][0].lower()
            nextItem = wordsArr[i + 1][0].lower()
            if actualItem == nextItem and flag == False:
                count += 1
                flag = True
            elif actualItem != nextItem and flag == True:
                flag = False
        print(count) 
    except:
        break