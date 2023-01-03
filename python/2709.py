def isPrimo(number):
    if number < 2:
        return False
    for n in range(2, number):
        if number % n == 0:
            return False
    return True

while True:
    try:
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
    
        if isPrimo(sum):
            print("You’re a coastal aircraft, Robbie, a large silver aircraft.")
        else:
            print("Bad boy! I’ll hit you.")
    except:
        break