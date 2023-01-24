while True:
    banksN, billsN = input().split()
    banksN = int(banksN)
    billsN = int(billsN)
    
    if banksN == billsN == 0:
        break

    tempArr = input().split()
    banksBalanceArr = [int(balance) for balance in tempArr]

    isPossible = True

    for i in range(billsN):
        bankDebtor, bankCreditor, value = input().split()
        bankDebtor = int(bankDebtor)
        bankCreditor = int(bankCreditor)
        value = int(value)
        
        banksBalanceArr[bankDebtor - 1] -= value
        banksBalanceArr[bankCreditor - 1] += value
    
    banksBalanceArr.sort()
        
    if banksBalanceArr[0] < 0:
        isPossible = False

    if isPossible == True:
        print('S')
    else:
        print('N')