while True:
    try:
        n = int(input())
        gridStart = list(map(int, input().split()))
        gridEnd = list(map(int, input().split()))
        actualGrid = gridStart
        count = 0
        for i in range(n-1, -1, -1):
            item = gridEnd[i]
            actualInd = actualGrid.index(item)
            endInd = i
            if actualInd == endInd:
                continue
            temp = actualGrid[:actualInd] + actualGrid[actualInd+1:i+1] + [item] + actualGrid[i+1:]
            actualGrid = temp
            count += endInd - actualInd
        print(count)
    except:
        break