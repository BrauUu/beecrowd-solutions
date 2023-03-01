while True:
    n = int(input())
    
    if n == 0:
        break
    
    arr = [i for i in range(n, 0, -1)]
    discardedArr = []
    
    while len(arr) >= 2:
        x = len(arr) - 1
        discardedArr.append(arr.pop(x))
        y = arr.pop(x - 1)
        arr.insert(0, y)
    
    discardedArrStr = ''    
    
    for x in discardedArr:
        discardedArrStr += str(x) + ', ' 
        
    print(f'Discarded cards: {discardedArrStr[:len(discardedArrStr) - 2]}')
    print(f'Remaining card: {arr[0]}')