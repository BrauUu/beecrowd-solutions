i, n = list(map(int, input().split()))

playersMoney = {
    'D' : i,
    'E' : i,
    'F' : i
}

actions = {
    'C' : lambda x : -x,
    'V' : lambda x : +x,
    'A' : lambda x : [+x, -x]
}

for _ in range(n):
    entries = input().split()
    if len(entries) == 4:
        action, player1, player2, value = entries
        res = actions[action](int(value))
        playersMoney[player1] += res[0]
        playersMoney[player2] += res[1]
    else:
        action, player1, value = entries
        playersMoney[player1] += actions[action](int(value))
    
print(f"{playersMoney['D']} {playersMoney['E']} {playersMoney['F']}")