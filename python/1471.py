while True:
    try:
        n, r = list(map(int, input().split()))

        returnedArr = list(map(int, input().split()))

        notReturned = ''

        if n != r:
            for i in range(1, n + 1):
                try:
                    returnedArr.index(i)
                except:
                    notReturned += str(i) + ' '
                    
            print(notReturned)
        else:   
            print('*')
    except:
        break