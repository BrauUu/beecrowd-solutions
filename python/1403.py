while True:
    n, m = list(map(int, input().split()))

    if n == m == 0:
        break

    players = {}

    for _ in range(n):
        l = list(map(int, input().split()))
        for player in l:
            players.update({player: (players.get(player) or 0) + 1})
    
    firsts = []
    seconds = []  
    biggest = 0 
    secondBiggest = 0
    
    for player, v in players.items():
        if v == biggest:
            firsts.append(player)
        elif v > biggest:
            secondBiggest = biggest
            biggest = v
            seconds = firsts.copy()
            firsts.clear()    
            firsts.append(player)  
        elif v == secondBiggest:
            seconds.append(player)
        elif v > secondBiggest:
            secondBiggest = v
            seconds.clear()    
            seconds.append(player)  

    seconds.sort()
    print(*seconds,"", sep=" ")