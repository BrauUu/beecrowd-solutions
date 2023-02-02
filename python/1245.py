while True:
    try:
        n = int(input())

        leftBoots = []
        rightBoots = []

        for i in range(n):
            size, foot = input().split()
            
            if foot == 'E':
                leftBoots.append(int(size))
            elif foot == 'D':
                rightBoots.append(int(size))
                
        leftBoots.sort()
        rightBoots.sort()

        count = 0
        arr1 = []
        arr2 = []

        if len(leftBoots) < len(rightBoots):
            arr1 = leftBoots
            arr2 = rightBoots
        else:
            arr1 = rightBoots
            arr2 = leftBoots

        for x in arr1:
            try:
                ind = arr2.index(x)
                arr2.pop(ind)
                count += 1
            except:
                continue
            
        print(count)
    except:
        break