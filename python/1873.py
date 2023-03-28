n = int(input())

for i in range(n):
    x, y = input().split()
    res = ''
    
    if x == y:
        res = 'empate'
    elif x == 'tesoura':
        if y == 'papel' or y == 'lagarto':
            res = 'rajesh'
        else:
            res = 'sheldon'
    elif x == 'papel':
        if y == 'pedra' or y == 'spock':
            res = 'rajesh'
        else:
            res = 'sheldon'
    elif x == 'pedra':
        if y == 'lagarto' or y == 'tesoura':
            res = 'rajesh'
        else:
            res = 'sheldon'
    elif x == 'lagarto':
        if y == 'spock' or y == 'papel':
            res = 'rajesh'
        else:
            res = 'sheldon'
    elif x == 'spock':
        if y == 'tesoura' or y == 'pedra':
            res = 'rajesh'
        else:
            res = 'sheldon'
            
    print(res)