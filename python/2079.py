def isCousin(number):
    if number < 2:
        return False
    for n in range(2, number):
        if number % n == 0:
            return False
    return True

gloriaWins = False

while gloriaWins == False:

    m = int(input())

    coins = []

    for i in range(m):
        coins.append(int(input()))
        
    n = int(input())

    sum = 0

    for i in range(len(coins) - 1, -1, -n):
        if i < 0:
            break
        sum += coins[i]
        
    if isCousin(sum):
        print('You’re a coastal aircraft, Robbie, a large silver aircraft.')
        gloriaWins = True
    else:
        print('Bad boy! I’ll hit you.')