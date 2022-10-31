while True:
    n, m = input().split()
    n = int(n)
    m = int(m)
    
    if m == 0 and n == 0:
        break
    
    change = m - n
    billsCount = 0
    
    if change >= 100:
        change -= 100
        billsCount += 1
    if change >= 50:
        change -= 50
        billsCount += 1
    if change >= 20:
        change -= 20
        billsCount += 1
    if change >= 10:
        change -= 10
        billsCount += 1
    if change >= 5:
        change -= 5
        billsCount += 1
    if change >= 2:
        change -= 2
        billsCount += 1
        
    if billsCount == 2:
        print('possible')
    else:
        print('impossible')